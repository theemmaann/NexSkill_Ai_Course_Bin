#putting in variable value of str and integer. 
# variable stores latest value so if we put new value old value gets replaced by new one
#we can chane int value to str value and vice versa 

Age = 25
Name = "Adil"
Age = 29

print("Age : " + str(Age))
#str((Age)) temporarily labels it as string but in final it will be int only
#to make it str permanently we need to write at start age(str((Age)) and 
# then it will be str permanently)

print("Name : " + Name)

#you cannot add type with a plus sign

print(type(Age))

print(type(Name))

print("the program ends here")