# son = 45 
# print('son = ', son, type(son))
# sonlar = [45, 85, 25, 63, 95]
# print('sonlar = ', sonlar, type(sonlar) )

# sonlar = [25, 56, 85, 96, 'python', False]
# print(sonlar)
# print(len(sonlar))  #len() listning elementlar sonini chiqaruvchi funksiya
# sonlar.append('php') # append() bu listga yangi element qo'shib qoyadi
# print(sonlar)
#-----------------------------------------------------------------
# 12- dastur   Statistika malumotlari

# import pygal

# line_chart = pygal.Line()
# line_chart.title = 'Statistika'
# line_chart.x_labels = ['fevral', 'Mart', 'Aprel', 'May']
# line_chart.add('Facebook', [9.24, 14.11, 34.78, 20.43])
# line_chart.add('Instagram', [22.24, 35.11, 16.78, 8.43])
# line_chart.add('Youtube', [30.24, 20.11, 15.78, 17.43])
# line_chart.render_in_browser()

#------------------------------------------------------------------

# 12- topshiriq

import pygal

first = input('ijtimoiy tarmoq nomini kiriting: ')
first_list = list(input(f'{first}ning 3 ta qiymatini kiriting'))
second = input('ijtimoiy tarmoq nomini kiriting: ')
second_list = list(input(f'{second}ning 3 ta qiymatini kiriting'))
third = input('ijtimoiy tarmoq nomini kiriting: ')
third_list = list(input(f'{third}ning 3 ta qiymatini kiriting'))

line_chart = pygal.Line()
line_chart.title = 'Statistika'
line_chart.x_labels = ['yanvar','fevral','mart']
line_chart.add(f'{first}', first_list)
line_chart.add(f'{second}', second_list)
line_chart.add(f'{third}', third_list)

line_chart.render_in_browser()