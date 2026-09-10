import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
df=pd.read_csv('housing.csv', delimiter=',')

df.plot.scatter(x='total_rooms',y='population', title='Graph of housing');
plt.show()

y=df['population'].values.reshape(-1,1)
X=df['total_rooms','total_bedrooms'].values.reshape(-1,1)

print("y:", y)
print("X:", X)

SEED=66
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=SEED)
print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()


regressor.fit(X_train,y_train)
print(regressor.intercept_)
print(regressor.coef_)

def calc(slope,intersept,total_rooms):
    return slope*total_rooms+intersept

score= calc(regressor.coef_, regressor.intercept_, 7099)
print(score)

score=regressor.predict([[30]])
print(score)

y_pred=regressor.predict(X_test)
df_preds=pd.DataFrame({'Actual':y_test.squeeze(),'predicted': y_pred.squeeze()})
print(df_preds)
















from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
mae= mean_absolute_error(y_test, y_pred)
mse=mean_squared_error(y_test, y_pred)
rmse=np.sqrt(mse)
r2=r2_score(y_test,y_pred)

print(f"Mean absolute error:{mae:2f}")
print(f"Mean squared error:{mse:2f}")
print(f"Root mean squared error:{rmse:2f}")
print(f"R2score:{r2:2f}")

