import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
df=pd.read_csv('insurance.csv', delimiter=',')
print(df)
print()
print('Data type of csv:', df.dtypes)
print()
print('Type of csv:', df.info())
print()
print('Last three row of data set:')
print(df.tail(3))
print('First three row of data set:')
print(df.head(3))

df.plot.scatter(x='age',y='charges', title='Graph of housing');
plt.show()

df.plot.scatter(x='children',y='charges', title='Graph of housing');
plt.show()


df.dropna(inplace=True)
y=df['charges']
X=df[['age','children']]

print("y:", y)
print("X:", X)

SEED=66
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=SEED)
print(X_train)
print(y_train)


from sklearn.tree import DecisionTreeRegressor

Tree_model = DecisionTreeRegressor(min_samples_split=10, min_samples_leaf=5, random_state=SEED)
Tree_model.fit(X_train, y_train)

print("Feature importances:", Tree_model.feature_importances_)
# trees mein coef_ / intercept_ nahi hote (wo linear model wali cheez thi)
# feature_importances_ batata hai har feature ne splits mein kitna contribute kia

score = Tree_model.predict([[1106, 7099]])
print(score)

y_pred = Tree_model.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'predicted': y_pred.squeeze()})
print(df_preds)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f'Mean absolute error:{mae:.2f}')
print(f'Mean Squared error:{mse:.2f}')
print(f'root mean squared error:{rmse:.2f}')
print(f'R2 score:{r2:.2f}')