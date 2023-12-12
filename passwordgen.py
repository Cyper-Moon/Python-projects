import random
import string

def generate_password(length):
  password_characters = string.ascii_letters + string.digits + string.punctuation
  return ''.join(random.choice(password_characters) for i in range(length))

# Generate a password with 15 characters
password = generate_password(15)
print(password)



