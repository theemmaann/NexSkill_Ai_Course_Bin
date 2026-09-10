import numpy as np
import pandas as pd
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from keras.metrics import R2Score,RootMeanSquaredError,mean_absolute_error
import matplotlib.pyplot as plt
from keras.regularizers import l1
from keras.layers import BatchNormalization

df=pd.read_csv('diabetes_deep_learning.csv')
print(df.head())
print(df.shape)
df.isnull().sum()
print(df.describe())

X=df.iloc[:,:-1]
y=df.iloc[:,-1]

print('X:', X)
print('y:', y)


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)
# Polynomial features - interactions banayein
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Ab isi X_train_poly, X_test_poly ko Neural Network mein use karein

from keras.layers import Dropout
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Dropout, Input
model = Sequential([
    Input(shape=(X_train_poly.shape[1],)),
    Dense(48, activation="relu"),      # thora zyada neurons
    Dropout(0.3),
    Dense(24, activation="relu"),
    Dropout(0.2),
    Dense(12, activation="relu"),      # ek extra layer
    Dense(1)
])

from keras.optimizers import Adam
model.compile(optimizer=Adam(learning_rate=0.0005), loss='mse', metrics=['mae'])   # learning rate kam kiya

early_stop = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    epochs=300,
    batch_size=8,                      # chota batch size
    validation_split=0.15,
    callbacks=[early_stop],
    verbose=1
)

plt.plot(history.history['loss'], label='Train Loss')          # <- history.history
plt.plot(history.history['val_loss'], label='Validation Loss')  # <- history.history
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Train vs Validation Loss')
plt.legend()
plt.show()
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error
y_pred = model.predict(X_test_poly).flatten()
r2 = r2_score(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"R2 (accuracy jaisa): {r2:.4f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")