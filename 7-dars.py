# shart operatorlari
# if ---- agar
# elif ---- aks holda agar
# else ----- aks holda
# til = input('tilni tanlang: uz/en ?')
# -----------------------------------
# if til == 'uz':
#     print('Assalomu alaykum')
# elif til == 'en':
#     print('Hello!')
# else:
#     print('xato tanlandi.')
# -----------------------------------
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
c = input('{} + {} = '.format(a, b))
k = 0
m = 0
while c.isdigit():
   
    if int(c) == (a + b):
        print('To`g`ri')
        k+=1
    else:
        print('Xato!')
        m+=1
    a = randint(1, 500)
    b = randint(1, 500)
    c = input('{} + {} = '.format(a, b))

print('Dastur tugadi!')
print('To`g`ri javoblar: {}'.format(k))
print('Xato javoblar: {}'.format(m))

#-------------------------------------------
#Masala
# a = int(input('yilni kiriting: '))
# c = a%4
# if c == 0:
#     print('bu kabisa yili:') 
# else:
#     print('bu kabbisya yili emas:')