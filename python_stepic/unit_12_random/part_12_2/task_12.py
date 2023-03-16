import string
from random import choice

def generate_password(length):
    detected = ['l','I','O','o', 1, 0]
    password_char_up = set(string.ascii_uppercase) - {'I','O'}
    password_char_low = set(string.ascii_lowercase) - {'l','o'}
    password_digit = set(string.digits) - {1, 0}

    pasword = ''

    while len(password) < length:
        password += choice(password_char_up)
        password += choice(password_char_low)
        password += choice(password_digit)

    return password



n = int(input())
#len_password = int(input())

print(generate_password(n))
print(generate_password(n))
print(generate_password(n))
print(generate_password(n))
