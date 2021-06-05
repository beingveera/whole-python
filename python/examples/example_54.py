import tensorflow as tf
from tensorflow import keras

# Load data
imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# A dictionary mapping words to an integer index
word_index = imdb.get_word_index()

# The first indices are reserved
word_index = {k: (v + 3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

# Decode review to text
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])


def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text if i != 0])


# Pad all reviews to the same length
train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding='post', maxlen=256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding='post', maxlen=256)

# Create model
vocab_size = 10000
model = keras.Sequential([keras.layers.Embedding(vocab_size, 16), keras.layers.GlobalAveragePooling1D(), keras.layers.Dense(16, activation=tf.nn.relu), keras.layers.Dense(1, activation=tf.nn.sigmoid)])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

# Split data into validation and train sets
x_val, y_val = train_data[:10000], train_labels[:10000]
partial_x_train, partial_y_train = train_data[10000:], train_labels[10000:]

# Start learning
model.fit(partial_x_train, partial_y_train, batch_size=512, epochs=30, validation_data=(x_val, y_val))

results = model.evaluate(test_data, test_labels)
print(results)

COUNT = 5
test_data_print, test_labels_print = test_data[:COUNT], test_labels[:COUNT]
predictions = model.predict(test_data_print)

for i in range(COUNT):
    print("Review: " + decode_review(test_data_print[i]))
    pred = predictions[i][0]
    value = test_labels_print[i]
    print("Prediction / Value: " + str(pred) + " / " + str(value))
    if (pred < 0.5) != (value < 0.5):
        print('\x1b[1;31mIncorrect prediction')
    else:
        print('\x1b[1;32mCorrect prediction')
    print('\x1b[0m')
