import turtle
import random

random.seed()

randX = random.randrange(1, 6)
randY = random.randrange(1, 6)

fred = turtle.Turtle()
wn = turtle.Screen()

step = 50
steps = step

def up():
	fred.left(90)
	fred.forward(steps)
	fred.left(-90)
	if fred.xcor() == (randX * step) and fred.ycor() == (randY * step):
		print "Success!"

def down():
	fred.right(90)
	fred.forward(steps)
	fred.right(-90)
	if fred.xcor() == (randX * step) and fred.ycor() == (randY * step):
		print "Success!"

def left():
	fred.backward(steps)
	if fred.xcor() == (randX * step) and fred.ycor() == (randY * step):
		print "Success!"

def right():
	fred.forward(steps)
	if fred.xcor() == (randX * step) and fred.ycor() == (randY * step):
		print "Success!"
	
def travelto(Xsteps, Ysteps):
	fred.goto(Xsteps*step, Ysteps*step)

def dot():
	fred.dot()

fred.up()

travelto(randX, randY)

fred.down()

fred.dot()

fred.up()

travelto(0, 0)

fred.down()

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(quit, "q")
wn.onkey(dot, "space")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
turtle.mainloop()