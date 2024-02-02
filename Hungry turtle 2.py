from turtle import*
import random
t=Turtle()
s=Screen()
t.speed(100)
s.bgcolor("cyan")
t.pu()
t.goto(-180,70)
t.pd()
t.color("black")
t.begin_fill()
for i in range(2):
  t.fd(350)
  t.rt(90)
  t.fd(200)
  t.rt(90)
t.end_fill()
t.pu()
t.goto(-190,120)
t.pd()
t.color("red")
t.write("Hungry Turtle",font= ("Aerial",20,"bold"))
t.pu()
t.goto(-185,100)
t.pd()
t.color("orange")
t.write("Use the arrow keys to move turtle & touch the food to score",font=("Aerial",9,"bold"))
t.pu()
t.goto(-100,80)
t.pd()
t.color("purple")
t.write("Score:",font=("Aerial",15,"bold"))
t.ht()
score = 0
sc = Turtle()#for score
sc.pu()
sc.goto(-30,80)
sc.pd()
sc.color("purple")
sc.write(score,font=("Aerial",15,"italic"))
sc.ht()
f = Turtle()#food
f.shape("circle")
f.color("red")
h= Turtle()#player
h.color("yellow")
h.shape("turtle")
h.pu()
h.goto(0,-100)
h.lt(90)
s.listen()
def up():
  h.setheading(90)
  h.fd(20)
def down():
  h.setheading(270)
  h.fd(20)
def right():
  h.setheading(0)
  h.fd(20)
def left():
  h.setheading(180)
  h.fd(20)
  #moving
s.onkey(up,"Up")
s.onkey(left,"Left")
s.onkey(down,"Down")
s.onkey(right,"Right")

dx=random.randint(1,3)
dy=random.randint(-3,-1)
while (True):
  if(h.distance(f)<=25 or f.distance(h)<=25):
    f.pu()
    f.ht()
    t.clear()
    score += 1
    t.write(score,font=("Aerial",10,"bold"))
    newx= random.randint(-180,180)
    newy= random.randint(-100,80)
    f.setpos(newx,newy)
    f.st()

