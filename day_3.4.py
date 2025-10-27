# Count how many vowels are in a string

# Input string from user
text = input("Enter a string: ")

# Initialize vowel count
count = 0

# Define vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    # Check if the character is a vowel
    if char in vowels:
        count += 1

# Print the total count
print(f"Number of vowels: {count}")
