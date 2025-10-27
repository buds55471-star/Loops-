correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted ✅")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")
else:
    print("Too many failed attempts. Access denied 🚫")
