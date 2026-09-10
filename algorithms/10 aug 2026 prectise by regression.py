import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df=pd.read_csv('insurance.csv')
print(df.head())



from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['sex_encoded']=le.fit_transform(df['sex'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['sex'].head())

df['smoker_encoded']=le.fit_transform(df['smoker'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['smoker'].head())

df['region_encoded']=le.fit_transform(df['region'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['region'].head())



X = df[['age', 'bmi', 'sex_encoded', 'smoker_encoded', 'region_encoded']]
y=df['charges']
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=42)
gbr=GradientBoostingRegressor()
gbr.fit(X_train,y_train)
y_pred=gbr.predict(X_test)
print('linear regression r2:', r2_score(y_test,y_pred))

from xgboost import XGBRegressor
xgb=XGBRegressor()
xgb.fit(X_train,y_train)
y_pred=xgb.predict(X_test)
print('gradient boosting regressor:', r2_score(y_test,y_pred))
