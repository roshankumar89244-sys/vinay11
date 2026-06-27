# enter a no and count its digits
n = int(input("enter the no:"))
count = 0
while n > 0:
    n //= 10
    count += 1
print(f"Number of digits: {count}")