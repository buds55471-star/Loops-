'''Factorial Calculator
Input a number and calculate its factorial using a loop.'''

n = int(input("Enter a number:"))

i = 1
product = 1

while(i<=n):
    product=product*i
    i+=1
print(f"The factorial of number {n} is {product}")
