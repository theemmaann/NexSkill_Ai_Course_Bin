import pandas as pd

df = pd.read_csv('FastFoodRestaurants.csv', delimiter = ';', parse_dates = [14], date_format = '%Y-%m-%d', skiprows = 1)

print(df)