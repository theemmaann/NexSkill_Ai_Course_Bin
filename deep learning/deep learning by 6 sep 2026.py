import tensorflow as tf
from tensorflow.keras.layers import Dense, MaxPool2D, Conv2D, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

# ---------------- CNN Model ----------------
cnn = Sequential()
cnn.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu'))
cnn.add(BatchNormalization())
cnn.add(MaxPool2D(pool_size=(2, 2)))

cnn.add(Conv2D(64, (3, 3), activation='relu'))
cnn.add(BatchNormalization())
cnn.add(MaxPool2D(pool_size=(2, 2)))

cnn.add(Flatten())

cnn.add(Dense(128, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(1, activation='sigmoid'))

cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ---------------- Data ----------------
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

train_mask = (y_train.flatten() == 0) | (y_train.flatten() == 1)   # 0=airplane, 1=automobile
test_mask = (y_test.flatten() == 0) | (y_test.flatten() == 1)

X_train, y_train = X_train[train_mask], y_train[train_mask]
X_test, y_test = X_test[test_mask], y_test[test_mask]

def limit_per_class(X, y, per_class):
    idx_0 = (y.flatten() == 0).nonzero()[0][:per_class]
    idx_1 = (y.flatten() == 1).nonzero()[0][:per_class]
    idx = list(idx_0) + list(idx_1)
    return X[idx], y[idx]

X_train, y_train = limit_per_class(X_train, y_train, per_class=2000)
X_test, y_test = limit_per_class(X_test, y_test, per_class=100)

print("Train images:", X_train.shape[0])
print("Test images:", X_test.shape[0])

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# ---------------- Data Augmentation ----------------
datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

datagen.fit(X_train)

# Apply the SAME normalization to test data (this was the bug)
X_test = datagen.standardize(X_test.copy())

# ---------------- Training ----------------
epochs = 25
batch_size = 32

cnn.fit(
    datagen.flow(X_train, y_train, batch_size=batch_size),
    steps_per_epoch=len(X_train) // batch_size,
    epochs=epochs,
    validation_data=(X_test, y_test)
)

# ---------------- Evaluation ----------------
loss, accuracy = cnn.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

y_pred = cnn.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int)

print("Unique predictions:", np.unique(y_pred_classes, return_counts=True))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_classes))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_classes))

# ---------------- Test on YOUR OWN image ----------------
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def predict_image(img_path):
    img = load_img(img_path, target_size=(32, 32))   # must match input_shape
    img_array = img_to_array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = datagen.standardize(img_array.copy())  # same normalization as training
    img_array = np.expand_dims(img_array, axis=0)      # add batch dimension

    prediction = cnn.predict(img_array)[0][0]
    label = "Automobile" if prediction > 0.5 else "Airplane"
    confidence = prediction if prediction > 0.5 else 1 - prediction

    print(f"Prediction: {label} (confidence: {confidence:.2%})")

# ---------------- Apni image ka path yahan daalo ----------------
predict_image(r"C:\Users\DELL\Documents\GitHub\Full-Stack-AI-Bootcamp-B-11-bin\aeroplane photo.jpg")
predict_image(r"C:\Users\DELL\Documents\GitHub\Full-Stack-AI-Bootcamp-B-11-bin\images 2.jpg")