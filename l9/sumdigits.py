# enter a no and sum of its digits
n = int(input("enter the no:"))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(f"Sum of digits: {sum}")