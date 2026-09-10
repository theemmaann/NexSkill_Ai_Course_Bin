import numpy as np
import pandas as pd
from keras.layers import Dense, Input,Dropout
from keras.models import Sequential
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.callbacks import EarlyStopping

df = pd.read_csv('pima_diabetes_ANN.csv')
print(df.head())
print(df.shape)
print(df.describe())
df.isnull().sum()
df.dropna(inplace=True)
print(df)

X = df.iloc[:, :-1]
print(X)

y = df.iloc[:, -1]
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

model = Sequential([
    Input(shape=(8,)),
    Dense(16, activation='relu'),
    Dropout(0.3),
    Dense(8, activation='relu'),
    Dropout(0.2),
    Dense(1, activation="sigmoid")
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
history = model.fit(X_train_scaled, y_train, epochs=150, batch_size=16,validation_split=0.1, callbacks=[early_stop] )
test_loss, test_acc = model.evaluate(X_test_scaled, y_test)
print('test_acc:', test_acc)