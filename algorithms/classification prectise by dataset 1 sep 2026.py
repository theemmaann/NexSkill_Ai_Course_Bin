import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,ConfusionMatrixDisplay
df=pd.read_csv('breast_cancer_classification.csv')
print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())
X=df.iloc[:,:-1]
print(X)
y=df.iloc[:,-1]
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y, train_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)
preds = model.predict(X_test_scaled)
cr=classification_report(y_test,preds)
print(cr)
cm=confusion_matrix(y_test,preds)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Malignant", "Benign"])
disp.plot()
plt.show()
read=input('wait a minute')