import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

Keras = tf.keras

cf10 = Keras.datasets.cifar10
Kutils = Keras.utils
klayers = Keras.layers

from keras.utils import to_categorical
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.metrics import Precision, Recall

(train_images, train_labels), (test_images, test_labels) = cf10.load_data()

def show_images(train_images,
                 class_names,
                 train_labels,
                 nb_samples=12, nb_row=4):

    plt.figure(figsize=(12, 12))
    for i in range(nb_samples):
        plt.subplot(nb_row, nb_row, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i][0]])
    plt.show()


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

show_images(train_images, class_names, train_labels)
