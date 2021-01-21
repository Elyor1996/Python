# if da bir nechta shartlarni bir vaxtda berish
# va bilan berish un and so1zi ishlatiladi---------------- 
# a = input('Sonni kiritng: ')
# if int(a) > 0 and a.isdigit() and int(a) < 1000:
#     print('raxmat!')
# else:
#     print('Xato kiritdingiz!')
#---------------------------------------------------------
# yoki bilan ishlash OR deyiladi

# name = input('enter the name: ')
# surname = input('enter the surname: ')

# if name or surname:
#     print('thank you !')
# else:
#     print('enter name or surname..')
#----------------------------------------------------------
# 8-dastur
number = input('enter the number from 1 to 30 : ')
if number.isdigit():
    number = int(number)
    if number > 0 and number < 30:
        reminer = number%10
        letter = ''
        if number > 9 and number < 20: 
            letter = 'o`n '
        elif number > 20 and number < 30: 
            letter = 'yigirma ' 

        if reminer == 1:
            letter = 'bir'
        elif reminer == 2:
            letter = 'ikki'
        elif reminer == 3:
            letter = 'uch'
        elif reminer == 4:
            letter = 'to`rt'
        elif reminer == 5:
            letter = 'besh'
        elif reminer == 6:
            letter = 'olti'
        elif reminer == 7:
            letter = 'yetti'
        elif reminer == 8:
            letter = 'sakkiz'
        elif reminer == 9:
            letter = 'to`qqiz'
        elif reminer == 10:
            letter = 'o`n'
        
        print(letter)
    else:
        print('enter only number from 1 to 30')
else:
    ('enter only number not word')