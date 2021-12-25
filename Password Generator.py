user=input('enter your name ')
import random
chars=user+'0123456789'
number=3
length=8
print('\n Here is some password')
for pwd in range(number):
  password=''
  for c in range(length):
    password += random.choice(chars)
  print(password)