
import turtle 
import time 
tut = turtle.Screen() 
tut.bgcolor("black") 
tut.title("Turtle") 
my_pen = turtle.Turtle() 
my_pen.color("blue") 
tut = turtle.Screen()

for i in range(4): 
    my_pen.forward(100) 
    my_pen.left(90) 
my_pen.goto(50,50)

for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)
my_pen.goto(150,50)
my_pen.goto(100,0)

my_pen.goto(100,100) 
my_pen.goto(150,150) 
my_pen.goto(50,150) 
my_pen.goto(0,100)

time.sleep(20)