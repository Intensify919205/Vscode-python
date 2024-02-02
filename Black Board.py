
from turtle import*
t=Turtle()
s=Screen()
s.bgcolor("black")
t.shape("turtle")
t.color("white")
#functions
def up():
  t.setheading(90)
  t.fd(50)
def down():
  t.setheading(270)
  t.fd(50)
def right():
  t.setheading(0)
  t.fd(50)
def left():
  t.setheading(180)
  t.fd(50)
def eraser():
  t.color("black")
def penup():
  t.pu()

def pendown():
  t.pd()
  t.color("white")
#events
s.listen()
s.onkey(up,"Up")
s.onkey(down,"Down")
s.onkey(right,"Right")
s.onkey(left,"Left")
s.onkey(penup,"U")
s.onkey(pendown,"P")
s.onkey(eraser,"E")
s.mainloop()

