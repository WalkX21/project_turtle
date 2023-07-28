from turtle import *


def maison(couleur):

  width(5)
  color(couleur)
  left(90)
  forward(50)
  left(-90)
  forward(25)
  left(90)
  forward(50)
  left(-90)
  forward(25)
  left(270)
  forward(50)
  left(90)
  forward(25)
  left(270)
  forward(50)
  left(90)
  forward(10)

def residence(couleur):
  
  penup()
  goto(-300, -200)
  pendown()
  for i in range(4):
    maison(couleur)
    forward(10)


