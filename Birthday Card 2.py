from turtle import*
import time
t=Turtle()
s=Screen()
s.bgcolor("black")
t.color("white")
t.speed(100)
t.width(4)
t.ht()
#function
def star(x,y):
  t.pu()
  t.goto(x,y)
  t.pd()
  for i in range(5):
    t.fd(10)
    t.rt(144)
#creating stars
star(-10,150)
star(-100,100)
star(-30,190)
star(-120,163)
star(-193,69)
star(-123,199)
star(63,99)
star(-18,60)
star(1,191)
star(199,131)
star(13,145)





t.pu()
t.goto(-130,30)
#writing bday
t.write("Happy Birthday Mom!!!",font=("Arial",20,"bold"))

t.goto(-150,-10)

t.write("The more birthdays you have",font=("Arial",15,"bold"))
t.sety(-35)
t.write("the more beautiful you get",font=("Arial",15,"bold"))
t.sety(-60)
t.write("Have a great birthday.......",font=("Arial",15,"bold"))

time.sleep(2)
s.bgcolor("red")
time.sleep(2)
s.bgcolor("yellow")
time.sleep(2)
t.reset()

print("Choose a shape-diamond,triangle,circle,square")

shape = input()
print("Choose a color-red,purple,orange,blue")
color = input()
#color
if color =="red":
  color = "red"
elif color == "purple":
  color = "purple"
elif color == "orange":
  color = "orange"
elif color == "blue":
  color = "blue"


t.speed(20)

#Making the flower
t.color(color)
length = 20
if shape =="circle":
  for i in range(12):
    t.circle(-length,30)
    t.fd(20)
    t.begin_fill()
    t.dot(30)
    t.end_fill()
elif shape == "triangle":
  for i in range(12):
    t.circle(-length,30)
    t.fd(20)
    t.begin_fill()
    for j in range(3):
      t.fd(length)
      t.rt(120)
  t.end_fill()
elif shape == "square":
  for i in range(12):
     t.circle(-length,30)
     t.fd(20)
     t.begin_fill()

  for j in range(4):
    t.fd(length)
    t.rt(90)
  t.end_fill()


elif shape == "diamond":
  for i in range(12):
    t.circle(-length,30)
    t.fd(20)
    t.begin_fill()
    for i in range(2):
      t.fd(length)
      t.rt(120)
      t.fd(length)
      t.rt(60)
    t.end_fill()




#centre circle

t.pu()
t.goto(-10,-90)
t.pd()
t.begin_fill()
t.circle(20)
t.end_fill()




#Empty inner circle

t.pu()
t.sety(-100)
t.setx(-10)
t.pd()
t.circle(35)

#stem
t.pu()
t.sety(-70)
t.rt(90)
t.fd(30)
t.pd()
t.color("yellowgreen")
t.width(3)
t.fd(100)


#leaf right
t.fillcolor("green")
t.backward(30)
t.rt(20)
t.begin_fill()
for i in range(2):
  t.lt(120)
  t.fd(40)
  t.lt(60)
  t.fd(40)
t.end_fill()

#leaf left
t.lt(40)
t.begin_fill()
for i in range(2):
  t.rt(120)
  t.fd(30)
  t.rt(60)
  t.fd(30)

t.end_fill()


t.pu()
t.goto(-125,100)
t.pd()
t.color(color)
t.write("Have a Great Birthday, " ,font=("Arial",15,"bold"))
t.ht()
t.done()
