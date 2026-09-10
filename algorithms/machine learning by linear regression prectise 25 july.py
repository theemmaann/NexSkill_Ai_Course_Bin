import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('FastFoodRestaurants (1).csv')
print(df.head())
print('df.shape():', df.shape)

df.plot.scatter(x='latitude', y='longitude', title='Scatter plot of bed and bath percentages')
plt.show()

print('df.describe:', df.describe())
print('df[latitude]:', df['latitude'])
print('df[longitude]:', df['longitude'])

y=df['latitude'].values.reshape(-1,1)
X=df['longitude'].values.reshape(-1,1)
print('y:', y)
print('X:', X)

print(df['latitude'].values)
print(df['longitude'].values.shape)
print(X.shape)
print(X)


SEED = 42
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)
print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(X_train,y_train)
print(regressor.intercept_)
print(regressor.coef_)

def calc(slope,intercept,hours):
    return slope*hours+intercept
score= calc(regressor.coef_, regressor.intercept_,9.5)
print(score)

score=regressor.predict([[9.5]])
print(score)

y_pred=regressor.predict(X_test)
df_pred=pd.DataFrame({'Actual':y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_pred)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
r2=r2_score(y_test,y_pred)
print(f'Mean absolute erroe:{mae:.2f}')
print(f'Mean Squared error:{mse:.2f}')
print(f'root mean squared erroe:{rmse:.2f}')
print(f'R2 score:{r2:.2f}')