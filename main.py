import turtle as tur
from  time import sleep

tur.bgcolor('black')
tur.pensize(4)
tur.speed(10)

for i in range(4):
      
    for color in ('red', 'green', 'blue'):
        tur.color(color)
        tur.circle(100)
        tur.left(30)

    tur.hideturtle()

sleep(1)