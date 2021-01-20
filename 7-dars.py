# shart operatorlari
# if ---- agar
# elif ---- aks holda agar
# else ----- aks holda
til = input('tilni tanlang: uz/en ?')

if til == 'uz':
    print('Assalomu alaykum')
elif til == 'en':
    print('Hello!')
else:
    print('xato tanlandi.')

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than ot equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b 
#--------------------------------------

# 2ta tasodifiy son yig`indisini toping

from random import randint

a = randint(1, 500)
b = randint(1, 500)

c = int(input('{} + {} = '.format(a, b)))

if c == (a + b):
    print('To`g`ri')
else:
    print('Xato!')