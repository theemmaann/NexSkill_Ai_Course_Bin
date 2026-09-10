from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

X,y =make_regression(n_samples=100,n_features=10,n_informative=5,n_targets=1,random_state=42)
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2)
gbr=GradientBoostingRegressor()
gbr.fit(X_train,y_train)
y_pred1=gbr.predict(X_test)
print("Gradient boosting-R2:", r2_score(y_test,y_pred1))
mse=mean_squared_error(y_test,y_pred1)
print(f"mean squared error: {mse:.2f}")
mae=mean_absolute_error(y_test,y_pred1)
print(f"mean absolute error: {mae:.2f}")





from xgboost import XGBRegressor
xgb=XGBRegressor()
xgb.fit(X_train,y_train)
y_pred2=xgb.predict(X_test)
print('Gradient boosting-R2:', r2_score(y_test,y_pred2))
mse=mean_squared_error(y_test,y_pred2)
print(f"mean squared error: {mse:.2f}")
mae=mean_absolute_error(y_test,y_pred2)
print(f"mean absolute error: {mae:.2f}")


from sklearn.ensemble import AdaBoostRegressor
ada=AdaBoostRegressor()
ada.fit(X_train,y_train)
y_pred3=ada.predict(X_test)
print('gradient boosting-R2:',r2_score(y_test,y_pred3))
mse=mean_squared_error(y_test,y_pred3)
print(f"mean squared error: {mse:.2f}")
mae=mean_absolute_error(y_test,y_pred3)
print(f"mean absolute error: {mae:.2f}")



from catboost import CatBoostRegressor
cbr=CatBoostRegressor(iterations=100,depth=5,learning_rate=0.05,loss_function='RMSE',verbose=0)
cbr.fit(X_train,y_train)
y_pred4=cbr.predict(X_test)
print('gradient boosting-R2:', r2_score(y_test,y_pred4))
mse=mean_squared_error(y_test,y_pred4)
print(f"mean squared error: {mse:.2f}")
mae=mean_absolute_error(y_test,y_pred4)
print(f"mean absolute error: {mae:.2f}")




from lightgbm import LGBMRegressor
lgbm=LGBMRegressor()
lgbm.fit(X_train,y_train)
y_pred5=lgbm.predict(X_test)
print('gradient boosting-R2:',r2_score(y_test,y_pred5))
mse=mean_squared_error(y_test,y_pred5)
print(f"mean squared error: {mse:.2f}")
mae=mean_absolute_error(y_test,y_pred5)
print(f"mean absolute error: {mae:.2f}")




import matplotlib.pyplot as plt
import seaborn as sns
fig,ax=plt.subplots(figsize=(11,5))
ax=sns.lineplot(x=y_test,y=y_pred1,label='GradientBoosting')
ax1=sns.lineplot(x=y_test,y=y_pred2,label='xgboost')
ax2=sns.lineplot(x=y_test,y=y_pred3, label='AdaBoostRegressor')
ax3=sns.lineplot(x=y_test,y=y_pred4,label='catboost')
ax4=sns.lineplot(x=y_test,y=y_pred5,label='lightgbm')
ax.set_xlabel('y_test:', color='g')
ax.set_ylabel('y_pred:', color='g')
fig.figure.show()