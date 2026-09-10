import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import certifi
import ssl

print(certifi.where())

# Fix: force Python to use certifi's certificate bundle for HTTPS requests
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

california_housing = fetch_california_housing()
california_data = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
california_data['MEDV'] = california_housing.target

X = california_data.drop('MEDV', axis=1)
y = california_data['MEDV']

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=42)
rf_egressor=RandomForestRegressor(n_estimators=100,random_state=42)
rf_egressor.fit(X_train,y_train)
y_pred=rf_egressor.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

single_data=X_test.iloc[0].values.reshape(1,-1)
predicted_values=rf_egressor.predict(single_data)

print(f"predicted_value: {predicted_values[0]:.2f}")
print(f"actual_values: {y_test.iloc[0]:.2f}")
print(f"Mean Squared error:{mse:.2f}")
print(f"R-2 squared error:{r2:.2f}")