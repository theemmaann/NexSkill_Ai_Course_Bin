print("Calculating Compound Interest")

p = float(input("Enter the principal amount: "))
r = float(input("Enter the amount of rate in percentage : "))
t = float(input("Enter the time in year: "))

CL = p * (1 + r/100) ** t - p
print("Compound Interest is: ", CL)