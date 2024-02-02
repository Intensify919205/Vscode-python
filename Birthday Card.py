from turtle import*
import time
import random 
t=Turtle()
s=Screen()
t.pu()
t.goto(-175,0)
t.pd()

#Welcome message

t.write("Hello i am Vihaan", font=("arial", 11 , "bold"))
t.pu()
t.goto(-30,5)
t.pd()
t.shape("triangle")
t.color("green")
t.stamp()
t.ht()
time.sleep(3)
#Welcome message2

t.color("black")
t.pu()
t.goto(-175,-20)
t.pd()
t.write("I have made a birthday card for you!")
time.sleep(2)
t.pu()
t.goto(-170,-40)
t.pd()
t.write("Please answer the questions in command propmt")
t.pu()
t.goto(-170,-60)
t.pd()


#Get user input

print("What is your name?")
name = input()
print("Choose a color - red,blue,yellow,cyan,green,orange")
color = input()
print("Choose a shape - Circle,triangle,square,diamond")
shape = input()

#Set color
if color == "red":
  color ="red"
elif color == "blue":
  color = "blue"
elif color == "yellow":
  color = "yellow"
elif color == "cyan":
  color = "cyan"
elif color == "green":
  color = "green"
elif color == "orange":
  color = "orange"

t.clear()

t.speed(5)

t.pu()
t.goto(-200,-
200)
t.pd()

t.fillcolor("black")
t.begin_fill()

#Making the outer border
for i in range(2):
  t.fd(660)
  t.lt(90)
  t.fd(400)
  t.lt(90)
t.end_fill()

t.pu()
t.goto(-150,160)
t.pd()

t.color("yellowgreen")
t.begin_fill()
for i in range(3):
  t.fd(250)
  t.rt(90)
  t.fd(50)
  t.rt(90)

t.circle(-25)
t.end_fill()


#Make dots under the title
t.pu()
t.fd(240)
t.lt(90)
t.fd(15)
t.lt(90)


t.pu()
t.goto(-140,105)
t.pd()


for i in range(13):
  t.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.begin_fill()
  t.circle(5)
  t.pu()
  t.fd(20)
  t.pd()
  t.end_fill()



#Write happy bday
t.pu()
t.goto(-130,130)
t.pd()
t.color("red")
t.write("Happy birthday ",font=("Araial",25,"bold"))
t.showturtle()
t.color("white")
t.pu()
t.goto(0,75)
t.pd()

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
t.goto(-10,0)
t.pd()
t.begin_fill()
t.circle(20)
t.end_fill()




#Empty inner circle

t.pu()
t.sety(-15)
t.pd()
t.circle(35)

#stem
t.pu()
t.sety(-15)
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
t.goto(-125,-165)
t.pd()
t.color(color)
t.write("Have a Lovely Day, " + name + "!",font=("Arial",15,"bold"))
t.ht()
t.done()
