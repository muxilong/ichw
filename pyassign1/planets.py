import turtle
import math
wn = turtle.Screen()
sun = turtle.Turtle()
sun.hideturtle()
sun.dot(100,"yellow")

mercury =turtle.Turtle()
mercury.color("brown")
mercury.shape("circle")
mercury.pensize(1)

venus =turtle.Turtle()
venus.color("yellow")
venus.shape("circle")
venus.pensize(1)

earth =turtle.Turtle()
earth.color("blue")
earth.shape("circle")
earth.pensize(1)

mars =turtle.Turtle()
mars.color("red")
mars.shape("circle")
mars.pensize(1)

jupiter =turtle.Turtle()
jupiter.color("orange")
jupiter.shape("circle")
jupiter.pensize(1)

saturn =turtle.Turtle()
saturn.color("brown")
saturn.shape("circle")
saturn.pensize(1)

uranus =turtle.Turtle()
uranus.color("sea green")
uranus.shape("circle")
uranus.pensize(1)

neptune =turtle.Turtle()
neptune.color("blue")
neptune.shape("circle")
neptune.pensize(1)



mercury.up()
mercury.goto(6000**(1/2),0)
mercury.down()

venus.up()
venus.goto(12000**(1/2),0)
venus.down()

earth.up()
earth.goto(18000**(1/2),0)
earth.down()

mars.up()
mars.goto(24000**(1/2),0)
mars.down()

jupiter.up()
jupiter.goto(50000**(1/2),0)
jupiter.down()

saturn.up()
saturn.goto(70000**(1/2),0)
saturn.down()

uranus.up()
uranus.goto(90000**(1/2),0)
uranus.down()

neptune.up()
neptune.goto(110000**(1/2),0)
neptune.down()

    
for i in range(10000000):
    mercury.speed(0)
    mercury.goto(6000**(1/2)*math.cos(i*math.pi/100),4000**(1/2)*math.sin(i*math.pi/100))
    venus.speed(0)
    venus.goto(12000**(1/2)*math.cos(i*math.pi/120),10000**(1/2)*math.sin(i*math.pi/120))
    earth.speed(0)
    earth.goto(18000**(1/2)*math.cos(i*math.pi/140),15000**(1/2)*math.sin(i*math.pi/140))
    mars.speed(0)
    mars.goto(24000**(1/2)*math.cos(i*math.pi/160),20000**(1/2)*math.sin(i*math.pi/160))
    jupiter.speed(0)
    jupiter.goto(50000**(1/2)*math.cos(i*math.pi/180),45000**(1/2)*math.sin(i*math.pi/180))
    saturn.speed(0)
    saturn.goto(70000**(1/2)*math.cos(i*math.pi/200),60000**(1/2)*math.sin(i*math.pi/200))
    uranus.speed(0)
    uranus.goto(90000**(1/2)*math.cos(i*math.pi/220),80000**(1/2)*math.sin(i*math.pi/220))
    neptune.speed(0)
    neptune.goto(110000**(1/2)*math.cos(i*math.pi/240),100000**(1/2)*math.sin(i*math.pi/240))
    
