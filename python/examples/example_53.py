import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import tkinter, sys

# Sometimes training takes longer with eager execution enabled
tf.compat.v1.disable_eager_execution()

# We don't have a terminal available in GUI mode, so let's simulate it
class stdredir(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.widget = tkinter.Text(self.root)
        self.widget.pack(fill='both', expand=True)
        self.text = ''

    def write(self, string):
        self.text += string.replace('\b', '')
        if '\r' in string:
            cutto = self.text.rindex('\r')
            sfrom = -1
            try:
                sfrom = self.text.rindex('\n', 0, cutto)
            except:
                pass
            self.text = self.text[:sfrom + 1] + self.text[cutto + 1:]

    def flush(self):
        self.widget.delete(1.0, tkinter.END)
        self.widget.insert(tkinter.END, self.text)
        self.widget.see(tkinter.END)
        self.widget.update()


sys.stdout = stdredir()

# The actual example
# Load data
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Class names are not included in the dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Normalize data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Create model
model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)), keras.layers.Dense(128, activation=tf.nn.relu), keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Start learning
model.fit(train_images, train_labels, epochs=5)

# Predict results
predictions = model.predict(test_images)


# Helper functions
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label], 100 * np.max(predictions_array), class_names[true_label]), color=color)


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


# Close the text window
sys.stdout.root.destroy()

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
    plot_value_array(i, predictions, test_labels)
plt.show()
