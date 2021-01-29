# aylanma funksiyalarni malum bir vaziyatda to`xtatish uchun BREAK ishlatiladi
# continue esa bir qadam oldinga o`tqazadi 

# text = input('texni kiritig: ')

# for s in text:
    
#     if s.isdigit():
#         continue
    
#     print(s)

#---------------------------------------------------
# 11 - dastur

from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Yangi oyna')
panel = Turtle()
panel.pensize(3)
panel.speed(0)
chiziq = Turtle()
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.color('red')
chiziq.up()
chiziq.goto(300,300)
chiziq.down()
chiziq.goto(300,-300)
chiziq.goto(-300,-300)
chiziq.goto(-300,300)
chiziq.goto(300,300)

koptok = Turtle()
koptok.color('green')
koptok.shape('circle')
koptok.up()
koptok.goto(0, 0)
# koptok.onkey(lambda:oyna.setheading(90), 'up')
# koptok.onkey(lambda:oyna.setheading(270), 'down')
# koptok.onkey(lambda:oyna.setheading(180), 'left')
# koptok.onkey(lambda:oyna.setheading(0), 'right')

panel.up()
panel.goto(150,-300)
panel.down()
panel.goto(150, -260)
panel.goto(0,-260)
panel.goto(0,-300)
panel.hideturtle()
step_x = 3
step_y = 2
while True:
    x, y = koptok.position()
    if x + step_x >= 300 or x + step_x <= -300:
        step_x = -step_x
    if y + step_y >= 300 or y + step_y <= -300:
        step_y = -step_y
    if y + step_y == -260:
        break

    koptok.goto(x+step_x, y+step_y)

  
oyna.mainloop()
