# Use a while loop to print the factorial of a number
from itertools import product

n = int(input("Enter a number:"))

product = 1
i = 1

while (i<n+1):
    product = product*i
    i+=1
print(f"The factorial of number {n} is {product}")

