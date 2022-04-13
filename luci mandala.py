import turtle

luci = turtle.Turtle()

luci.screen.bgcolor('black')
luci.pencolor('white')
luci.pensize(4)
luci.speed(3)
def pen(x,y):
    luci.penup()
    luci.goto(x,y)
    luci.pendown()
def pattern():
    for i in range(23):
        luci.forward(360)
        luci.fillcolor('red')
        luci.begin_fill()
        luci.circle(30)
        luci.end_fill()
        luci.left(219)
def sun():
    for i in range(9):
        luci.forward(80)
        luci.left(160)
        
pen(-180, 100)
pattern()
pen(-40, 30)
sun()
pen(-10, -184)
luci.circle(220)
pen(-10, -194)
luci.circle(230)
pen(-10, -144)
luci.circle(180)
pen(-2, -10)
luci.circle(46)
luci.hideturtle()


luci.done()         