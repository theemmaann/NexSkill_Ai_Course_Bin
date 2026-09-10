import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

df=pd.read_csv('wine_deep_learning.csv')
print(df.head())
print(df.shape)
df.isnull().sum()
X=df.iloc[:,:-1]
print(X)
y=df.iloc[:,-1]
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42, test_size=0.2)


ss=StandardScaler()
X_train_scaled=ss.fit_transform(X_train)
X_test_scaled=ss.transform(X_test)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train_scaled.shape[1],)),     # <- comma yahan
    tf.keras.layers.Dense(32, activation="relu"),                 # <- comma yahan
    tf.keras.layers.Dense(16, activation="relu"),                 # <- comma yahan
    tf.keras.layers.Dense(3, activation="softmax")                # last layer - comma zaroori nahi
])

model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])
history = model.fit(X_train_scaled, y_train, epochs=100, batch_size=8, validation_split=0.1)

# Evaluate
test_loss, test_acc = model.evaluate(X_test_scaled, y_test)
print("Test Accuracy:", test_acc)