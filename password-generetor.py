import random
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet)  for i in range(length))
    return password

password = generate_password(10)
print("Generated password: ", password)
