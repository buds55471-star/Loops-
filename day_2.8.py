'''Reverse Digits
Input a number and print its digits in reverse (e.g., 123 → 321)'''

n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10         # get last digit
    rev = rev * 10 + digit # build reversed number
    n = n // 10            # remove last digit

print("Reversed number:", rev)
