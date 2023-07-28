from turtle import *



def feu_rouge(activ=False):
  penup()
  goto(0, 110)
  color('red')
  pendown()
  if activ==True:
    begin_fill()
    circle(50)
    end_fill()  
  else:
    circle(50)
  hideturtle()

def feu_jaune(activ=False):
  penup()
  goto(0, 0)
  color('yellow')
  pendown()
  if activ==True:
    begin_fill()
    circle(50)
    end_fill()  
  else:
    circle(50)
  hideturtle()

def feu_vert(activ=False):
  penup()
  goto(0, -110)
  color('green')
  pendown()
  if activ==True:
    begin_fill()
    circle(50)
    end_fill()  
  else:
    circle(50)
  hideturtle()


ask = input('which one do you want to glow?')
if ask == 'red':
  feu_rouge(True)
else:
  feu_rouge()
  
if ask == 'jaune':
  feu_jaune(True)
else:
  feu_jaune()
  
if ask == 'vert':
  feu_vert(True)
else:
  feu_vert()