print("First Practice")
Property_Id=784 
print(Property_Id) 
print(type(Property_Id))
Property_Price=20000 
print(Property_Price)
print(type(Property_Price))
Property_Area="Gulberg"
print(Property_Area)
print(type(Property_Area))

Property_Price5 = Property_Price*5
print(Property_Price5)
print(type(Property_Price5)) #type tells the data type of variable

Property_City= input("Enter the city name: ")
print(Property_City)
print(type(Property_City))

Property_Info= input("Please enter property info: ")
print(Property_Info) 
print(len(Property_Info)) #len tells length

for x in Property_Info: #for loop to print each character of the string
    print(x)

st=Property_Info
print(st[2:4:1])
#print(st[2:4:2]) #it will print 2nd index and then skip 2 and print 4th index
#Start me 2 chorega phir 4 letters print krega aur ye chlega 2 br