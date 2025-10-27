# Calculate the sum of digits of a number.

n = int(input("Enter a number:"))

i = 1
sum = 1

while (i<=n):
    sum+=i
    i+=1
print(f"Sum of Digits of number {n} is:",sum)

