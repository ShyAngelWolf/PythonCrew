import random
import string


all_characters = string.ascii_letters + string.digits + string.punctuation
length  = int(input("Enter the length of password: "))

password ="".join(random.choices(all_characters, k=length))

print(password)
