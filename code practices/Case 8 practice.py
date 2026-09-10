# only when both values are true it will return true in AND operation otherwise it willshow false

print("----------- AND operation ----------")
a = True
b = False

c =True and False
print(c)



d = True and True
print("d:",d)

e = False and True
print(e)

f = False and False
print(f)



#-------------------

print("----------- OR operation ----------")

#or is used when any of the one values is true

True or True
print("True or True:", True or True)

True or False
print(True or False)

False or True
print(False or True)

False or False
print(False or False)

#NOT - alternates value of boolean value it changes true to false and false to true

print("----------- NOT operation ----------")

not True
print(not True)

not False
print(not False)

print("------------Operations ---------- ")

print((a == 10) and (b == 12))
print((a == 24) and (b == 24))


t = 10
k = 14
print((t <= 10) or (k == 12))

f = not True
print(f)