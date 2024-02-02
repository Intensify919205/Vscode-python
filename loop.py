from turtle import*
t=Turtle()
s=Screen()
t.speed(40)
t.pu()
t.goto(10,10)
t.pd()
t.fillcolor("red")
t.begin_fill()
length = 50
for i in range(10):
  t.circle(length)
  t.fd(10)
t.fd(10)
t.rt(90)
for j in range(10):
  t.circle(length)
  t.fd(10)
t.fd(10)
t.rt(90)
for h in range(10):
  t.circle(length)
  t.fd(10)
t.fd(10)
t.rt(90)
for l in range(10):
  t.circle(length)
  t.fd(10)
t.end_fill()
t.clear()