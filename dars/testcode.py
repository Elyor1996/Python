import turtle

#Screen
wn = turtle.Screen()
wn.bgcolor("lightblue")

#Turtle Player
spaceship = turtle.Turtle()
spaceship.color("red")
spaceship.penup()

#Constant
speed = 1

def up():
    spaceship.setheading(90)

def down():
    spaceship.setheading(270)
    
def left():
    spaceship.setheading(180)

def right():
    spaceship.setheading(0)

wn.listen()
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')

while True:
    spaceship.forward(speed)