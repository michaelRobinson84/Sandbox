MINIMUM_LENGTH = 8

password = input("Please enter a password, minimum length 8 characters: ")

while len(password) < 8:
    print("Password is too short!")
    password = input("Please enter a password, minimum length 8 characters: ")

print(len(password) * "*")
