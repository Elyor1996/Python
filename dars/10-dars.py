# 1 dan 30 gacha bo'lgan sonlarni ketma ket chiqarish

# son = 1

# while son <= 30:
#     print(son)
#     son += 1

#-----------------------------------------

# 10  masala

# from random import randint
# kod = [132,133,134]
# new_kod = randint(130,135)

# while new_kod in kod:
#     new_kod = randint(130, 135)
    
# print(new_kod)

#-----------------------------------------

# Topshiriq

a = input()

while True:
    if a.isdigit():
        print ("Butun son")
        break
    elif isinstance(float(a),float):
        print ("Bu haqiqiy son")
        break
    else:
        print('Enter again!')
        a = input()
