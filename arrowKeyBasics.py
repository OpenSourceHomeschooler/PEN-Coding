import turtle

fred = turtle.Turtle()
wn = turtle.Screen()

step = 50
steps = step

def up():
	fred.left(90)
	fred.forward(steps)
	fred.left(-90)

def down():
	fred.right(90)
	fred.forward(steps)
	fred.right(-90)

def left():
	fred.backward(steps)

def right():
	fred.forward(steps)

def dot():
	fred.dot()

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