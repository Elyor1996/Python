# import math
#
# print(math.ceil(9.5))
# print(math.floor(9.5))
# print(math.sqrt(64))
# a = int(input('Enter the number:'))
# ______________________________________________
# variant 1 (3 xonali sonni raqamlar yigindisini hisoblaydi)
# d = a%10
# b = a//100
# c = a%100//10
# print(c+b+d)
#_______________________________________________
# variant 2 (3 xonali sonni raqamlar yigindisini hisoblaydi)
# n = input("3 xonali son kiriting: ")
# a = int(n[0])+int(n[1])+int(n[2])
# print(a)

#_____________________________________
#variant 3 (N xonali sonni raqamlar yigindisini hisoblaydi)
n = input ('n sonni kiriting: ')
s = 0

for i in n:
    s = s + int(i)
print(s)

