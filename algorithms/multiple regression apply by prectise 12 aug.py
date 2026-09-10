import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score,mean_absolute_error,root_mean_squared_error
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

X,y=make_regression(n_samples=100,n_features=10,n_targets=1,random_state=42)
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2)

from sklearn.linear_model import Lasso
leg=Lasso(alpha=1.0)
leg.fit(X_train,y_train)
y_pred=leg.predict(X_test)
r2=r2_score(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
rmse=root_mean_squared_error(y_test,y_pred)
print(f"root mean squared error:{rmse:.2f}")
print(f"mean absolute error:{mae:.2f}")
print(f"r2 score acc: {r2:.2f}")


knn=KNeighborsRegressor()
knn.fit(X_train,y_train)
y_pred1=knn.predict(X_test)
r2=r2_score(y_test,y_pred)
rmse=root_mean_squared_error(y_test,y_pred1)
mae=mean_absolute_error(y_test,y_pred1)
print(f"r2 score: {r2:.2f}")
print(f"root mean squared error: {rmse:.2f}")
print(f"mean absolute error:{mae:.2f}")


lg=LinearRegression()
lg.fit(X_train,y_train)
y_pred2=lg.predict(X_test)
r2=r2_score(y_test,y_pred)
rmse=root_mean_squared_error(y_test,y_pred2)
mae=mean_absolute_error(y_test,y_pred2)
print(f"r2 score: {r2:.2f}")
print(f"root mean squared error: {rmse:.2f}")
print(f"mean absolute error:{mae:.2f}")

rg=Ridge()
rg.fit(X_train,y_train)
y_pred3=rg.predict(X_test)
rmse=root_mean_squared_error(y_test,y_pred3)
mae=mean_absolute_error(y_test,y_pred3)
print(f"r2 score: {r2:.2f}")
print(f"root mean squared error: {rmse:.2f}")
print(f"mean absolute error:{mae:.2f}")