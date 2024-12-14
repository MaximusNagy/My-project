import random
import string

try:
    while True:
        char_pool = string.ascii_letters + string.punctuation + string.digits
        length = int(input("Enter the length of the password: "))
        
        if length > 0:
            password = ''.join(random.choice(char_pool) for _ in range(length))
            print("\nGenerated password:", password)
        else:
            print("The length must be greater than 0.")

except ValueError:
    print("Please enter a valid number.")
