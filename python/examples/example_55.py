import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Download data
dataset_path = keras.utils.get_file("auto-mpg.data", "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")

# Load data with pandas
column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
dataset = pd.read_csv(dataset_path, names=column_names, na_values="?", comment='\t', sep=" ", skipinitialspace=True)

# Remove lines with unknown values
dataset = dataset.dropna()

# Origin column is categorical, make it numeric
origin = dataset.pop('Origin')
dataset['USA'] = (origin == 1) * 1.0
dataset['Europe'] = (origin == 2) * 1.0
dataset['Japan'] = (origin == 3) * 1.0

# Split data into validation and train sets
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# Separate the target value from features
train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

# Normalize
train_stats = train_dataset.describe().transpose()


def norm(x):
    return (x - train_stats['mean']) / train_stats['std']


train_data = norm(train_dataset)
test_data = norm(test_dataset)

# Create model
model = keras.Sequential([layers.Dense(64, activation=tf.nn.relu, input_shape=[len(train_dataset.keys())]), layers.Dense(64, activation=tf.nn.relu), layers.Dense(1)])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.RMSprop(0.001), metrics=['mean_absolute_error', 'mean_squared_error'])

# Stop training when the validation score doesn't improve
# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

# Start learning
model.fit(train_data, train_labels, epochs=1000, validation_split=0.2, callbacks=[early_stop], verbose=False)

import matplotlib.pyplot as plt
loss, mae, mse = model.evaluate(test_data, test_labels, verbose=0)
test_predictions = model.predict(test_data).flatten()
plt.scatter(test_labels, test_predictions)
plt.title("Mean Abs Error: %.2f MPG" % (mae, ))
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
_ = plt.plot([-100, 100], [-100, 100])

plt.show()
