import numpy as np
import pandas as pd

df=pd.read_csv('credit_record.csv')
print(df.head())
print('df.shape:', df.shape)
from sklearn import metrics


y = df['class_encoded']
X = df[['ID','MONTHS_BALANCE']]

print("y:", y)
print("X:", X)

SEED=500
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=SEED)
print(X_train)
print(y_train)

from sklearn.linear_model import LogisticRegression
log=LogisticRegression(random_state=500)

log=log.fit(X_train,y_train)
y_pred=log.predict(X_test)
print("Acurracy:", metrics.accuracy_score(y_test,y_pred))




from sklearn.metrics import classification_report,confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))