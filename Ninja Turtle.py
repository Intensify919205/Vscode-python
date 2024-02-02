from turtle import*
import random
t=Turtle()
s=Screen()
sc=Turtle()
score = 0 
t.speed(30)
s.bgcolor("cyan")
t.pu()
t.goto(-195,100)
t.pd()
t.begin_fill()
for i in range(2):
  t.fd(380)
  t.rt(90)
  t.fd(280)
  t.rt(90)
t.end_fill()
t.pu()
t.goto(-120,170)
t.pd()
t.color("red")
t.write("Shooting Ninja",font=("Aerial",20,"Bold"))
t.pu()
t.goto(-150,150)
t.pd()
t.color("Orange")
t.write("Use Mouse Click to Shoot. Left/Right keys to turn the turtle",font=("Aerial",10,"Bold"))
t.pu()
t.goto(-150,130)
t.pd()
t.write("Shoot the paddle to get the score",font=("Aerial",10,"Bold"))
t.color("red")
t.pu()
t.goto(-150,110)
t.pd()
t.write("Score: ",font=("Aerial",15,"Bold"))
sc.pu()
sc.goto(-90,110)
sc.pd()
sc.write(score,font=("Aerial",15,"Bold"))
sc.ht()
t.ht()
n=Turtle()
n.shape("turtle")
n.color("red")
n.pu()
n.goto(-40,-160)
n.lt(90)
p=Turtle()
s.register_shape("paddle",((0,30),(0,-30),(8,-30),(8,30)))
p.shape("paddle")
p.color("blue")
def right():
  n.rt(10)
def left():
  n.lt(10)
def up(x,y):
  for i in range(600):
    n.fd(30)
    if n.ycor()>90:
      n.ht()
      n.sety(-160)
      n.setx(0)
      n.st()
      break
s.listen()
s.onkey(right,"Right")
s.onkey(left,"Left")
s.onclick(up,1)
while True:
  s.update()
  if n.distance(p)<40 or p.distance(n)<40:
    sc.clear()
    score=score+1
    sc.write(score,font=("Aerial",15,"bold"))
    an=random.randint(-180,180)
    any=random.randint(-40,80)
    p.pu()
    p.setpos(an,any)








