import pandas as pd


#THIS READS CSV FILE AND PRINTS FITST FIVE ROWS AND LAST FIVE ROWS OF DATAFRAME BY DEFAULT
df = pd.read_csv('FastFoodRestaurants.csv', delimiter = ',')
print('printing csv dataframe : ', df)



#PRINTING DATATYPE, INFO, HEAD AND TAIL OF DATAFRAME
print('printing datatypes : ' , df.dtypes)
print('printing infor: ', df.info())
print('printing 1st 10 rows by head method : ', df.head(10))
print('printing last 10 rows by tail method : ', df.tail(10))

print(df.columns)


#finding summary and counting rows and columns of df
print('summary of dataframe: ', df.describe())
print('counting rows and columns: ', df.shape)



#printing specific column by pulling its label as variable
longitude = df['longitude']
print('printing longitude column: ', longitude)


print() # to add new line in output

#printing multiple columns
#two brackets here one with list[] and other with df[]
city_country = df[["city", "country"]]
print('printing many columns together; ', city_country)


#printing rows on basic of index position using loc method
print(df.loc[0:4])

#printing rows on basis of their labels using loc method
print(df.loc[:,['city', 'country']])

#printing single row
city = df.loc[1]
print(city)

#printing multiple rows 
tworows = df.loc[[7,9]]
print(tworows)

# so if i do 4:6 it is going to print 4,5,6 all rows since it takes starting point to ending point
#however if i used iloc it would have printed 4,5 since iloc doesn't consider ending point

slicingrows = df.loc[4:6]
print(slicingrows)


'''#to check if leland exists in row you suggested
row = df.loc[16]          # the row you're interested in
exists = row.isin(['Leland']).any()
print(exists)   # True or False


#to check leland lies whereever in code it willprint those rows
conditional = df.loc[df['city'] == 'Leland']
print(conditional) '''
