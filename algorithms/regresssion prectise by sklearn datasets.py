import pandas as pd
import numpy as np
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import r2_score,root_mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

X,y=load_diabetes(return_X_y=True, as_frame=True,scaled=False,)
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=42)

lgb = LGBMRegressor(
    verbose=-1,
    n_estimators=200,
    num_leaves=7,        # chota dataset -> chote/simple trees
    min_child_samples=10, # default 20 zyada strict tha 353 rows ke liye
    learning_rate=0.05
)
lgb.fit(X_train, y_train)
y_pred = lgb.predict(X_test)
print("r2 score:", r2_score(y_test, y_pred))
print("root mean squared error:", root_mean_squared_error(y_test, y_pred))
print("mean absolute error:", mean_absolute_error(y_test, y_pred))

adrg=AdaBoostRegressor(estimator=None,  n_estimators=50, learning_rate=1.0, loss='linear', random_state=None)
adrg.fit(X_train,y_train)
y_pred=adrg.predict(X_test)
print("r2 score:", r2_score(y_test, y_pred))
print("root mean squared error:", root_mean_squared_error(y_test, y_pred))
print("mean absolute error:", mean_absolute_error(y_test, y_pred))

gbr=GradientBoostingRegressor(loss='squared_error', learning_rate=0.1, n_estimators=100, subsample=1.0, criterion='deprecated', min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, init=None, random_state=None, max_features=None, alpha=0.9, verbose=0, max_leaf_nodes=None, warm_start=False, validation_fraction=0.1, n_iter_no_change=None, tol=0.0001, ccp_alpha=0.0)
gbr.fit(X_train,y_train)
y_pred=gbr.predict(X_test)
print("r2 score:", r2_score(y_test, y_pred))
print("root mean squared error:", root_mean_squared_error(y_test, y_pred))
print("mean absolute error:", mean_absolute_error(y_test, y_pred))

from sklearn.linear_model import LinearRegression
lg=LinearRegression()
lg.fit(X_train,y_train)
y_pred=lg.predict(X_test)
print("r2 score:", r2_score(y_test, y_pred))
print("root mean squared error:", root_mean_squared_error(y_test, y_pred))
print("mean absolute error:", mean_absolute_error(y_test, y_pred))