from turtle import *
import random

# from Cercle import Cercles

def Cercles():
  t.speed(100)
  x = 0
  while x != 4:
    a = 0
    Rayon = 10
    while a != 7:
      t.circle(Rayon)
      Rayon = Rayon + 10
      a = a + 1
    
    t.left(90)
    x = x + 1

h = random.randint(2, 7)
y = random.randint(2, 7)

t1 = Turtle()
x = 10
t1.penup()
t1.speed(10)
t1.goto(-100, 100)
t1.pendown()
t1.left(-90)

for i in range(21):
  
  t1.forward(200)
  t1.penup()
  t1.goto(-100 + x, 100)
  t1.pendown()
  
  i = i + 1
  x = x +10
t1.hideturtle()


t3 = Turtle()


t3.shape('turtle')
t3.color('blue')
t3.penup()
t3.goto(-100, -20)
t3.pendown()


t2 = Turtle()


t2.shape('turtle')
t2.color('red')
t2.penup()
t2.goto(-100, 60)
t2.pendown()
while t2.xcor() and t3.xcor() < 110 :
  
  t2.forward(h)
  t3.forward(y)

  
 


if t2.xcor() == 110:

  t = t2
  t1.clear()
  t2.clear()
  t3.clear()
  t1.hideturtle()
  
  Cercles()
  t3.hideturtle()
elif t3.xcor() == 110:
  
  t = t3
  t1.clear()
  t3.clear()
  t2.clear()
  t1.hideturtle()
  
  Cercles()
  t2.hideturtle()
  

