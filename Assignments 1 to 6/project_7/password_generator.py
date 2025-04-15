import random
import string

def generated_password(length=12):
    characters =string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#users inputs
length = int(input('Enter the length of the password: '))
password = generated_password(length)
print("your Desired Generated Password", password)
print("Password has been generated successfully.")