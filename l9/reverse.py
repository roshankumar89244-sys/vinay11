#enter a no and print reverse of that no using while loop
n = int(input("enter the no:"))
reverse = 0
while n > 0:
    reverse = (reverse * 10) + (n % 10)
    n //= 10
print("reverse of the no is:", reverse)
