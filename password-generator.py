import random
import string

def generate_password(min_length, numbers, special_characters):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number == True
        elif new_char in special:
            has_special == True
        
        meets_criteria = False
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria or has_special

    return pwd

strip = " 1234567890.,-=_+qwertuiopasdfghjklzxcvbm}"
min_length = int(input("Enter the minimum length for your password: "))
has_number = input("Do you want to have numbers? (y/n) ").lower().strip(strip) == "y"
has_special = input("Do you want to have special characters? (y/n) ").lower().strip(strip) == "y"
pwd = generate_password(min_length, has_number, has_special)
print(F"The generated password is: { pwd }")
input("Press any key to exit.")