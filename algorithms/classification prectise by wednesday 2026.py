import numpy as np
import pandas as pd

df=pd.read_csv('bank.csv')
print(df.head())
print('df.shape:', df.shape)
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['job_encoded']=le.fit_transform(df['job'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['job'].head())

le=LabelEncoder()
df['marital_encoded']=le.fit_transform(df['marital'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['marital'].head())

le=LabelEncoder()
df['education_encoded']=le.fit_transform(df['education'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['education'].head())

le=LabelEncoder()
df['default_encoded']=le.fit_transform(df['default'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['default'].head())

le=LabelEncoder()
df['housing_encoded']=le.fit_transform(df['housing'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['housing'].head())

le=LabelEncoder()
df['loan_encoded']=le.fit_transform(df['loan'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['loan'].head())

le=LabelEncoder()
df['contact_encoded']=le.fit_transform(df['contact'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['contact'].head())

le=LabelEncoder()
df['month_encoded']=le.fit_transform(df['month'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['month'].head())

le=LabelEncoder()
df['poutcome_encoded']=le.fit_transform(df['poutcome'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['poutcome'].head())

le=LabelEncoder()
df['deposit_encoded']=le.fit_transform(df['deposit'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['deposit'].head())



y = df['deposit_encoded']
X = df[['age', 'balance', 'day','duration','campaign','pdays','previous']]

print("y:", y)
print("X:", X)

SEED=500
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=SEED)
print(X_train)
print(y_train)

from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# SVM distance-based hai, isliye scaling zaroori hai
# (balance ~ -6800 to 81000, day ~ 1-31 — scale mismatch hi hang ki wajah tha)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svc = LinearSVC(max_iter=5000, random_state=SEED)
svc.fit(X_train_scaled, y_train)
y_pred = svc.predict(X_test_scaled)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
from sklearn.metrics import classification_report,confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))