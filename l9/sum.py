# sum of all numbers upto that number using while loop
n = int(input("enter the no:"))
i = 1
sum = 0 
while i <= n:
    sum += i
    i += 1
print(f"Sum: {sum}")