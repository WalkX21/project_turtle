from turtle import *

def Cercles():
  speed(100)
  x = 0
  while x != 4:
    a = 0
    Rayon = 10
    while a != 7:
      circle(Rayon)
      Rayon = Rayon + 10
      a = a + 1
    
    left(90)
    x = x + 1