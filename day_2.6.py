'''Sum of N Numbers
Ask the user for a number n, and print the sum of numbers from 1 to n.'''

n = int(input("Enter a number:"))
sum=1
for i in range(1,n+1):
    sum+=i
    print(sum)