# facctorial of a no using while loop 
num = int (input("enter the no:"))
fac = 1
while num>=1:
    fac *= num
    num -=1
print("Factorial:", fac)