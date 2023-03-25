from turtle import *
from time import sleep
from random import randint

speed(100)
hideturtle()
penup()
goto(-140,140)
for step in range(16):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

t1=Turtle()
t1.speed(100)
t1.color("red")
t1.shape ("turtle")
t1.penup()
t1.goto(-160,100)

t2=Turtle()
t2.speed(100)
t2.color("blue")
t2.shape ("turtle")
t2.penup()
t2.goto(-160,80)

t3=Turtle()
t3.speed(100)
t3.color("orange")
t3.shape ("turtle")
t3.penup()
t3.goto(-160,60)

t4=Turtle()
t4.speed(100)
t4.color("pink")
t4.shape ("turtle")
t4.penup()
t4.goto(-160,40)

t5=Turtle()
t5.speed(100)
t5.color("green")
t5.shape ("turtle")
t5.penup()
t5.goto(-160,20)

t6=Turtle()
t6.speed(100)
t6.color("brown")
t6.shape ("turtle")
t6.penup()
t6.goto(-160,0)

for turn in range(100):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
    t4.forward(randint(1,5))
    t5.forward(randint(1,5))
    t6.forward(randint(1,5))
sleep (10)