from turtle import *
from random import randint
from turtle import TurtleGraphicsError

# Setup
colormode(255)
bgcolor("black")
speed(0)
hideturtle()

# Constants
MAX_RADIUS = 60
CYCLES = 5
STEP = 2

# Drawing loop
radius = 1
growing = True
cycles_completed = 0

try:
    while cycles_completed < CYCLES:
        # Random bright colors
        r = randint(100, 255)
        g = randint(100, 255)
        b = randint(100, 255)
        color(r, g, b)

        # Draw the pulse circle
        begin_fill()
        circle(radius)
        end_fill()

        # Glow/Spiral movement
        left(1)
        forward(2)

        # Radius growth/shrink logic
        if growing:
            radius += STEP
        else:
            radius -= STEP

        # Switch direction
        if radius >= MAX_RADIUS:
            growing = False
        elif radius <= 1:
            growing = True
            cycles_completed += 1

    # Draw center glow at end
    penup()
    goto(0, 0)
    setheading(0)
    color("white")
    dot(20)
    print("✅ Animation completed.")

except TurtleGraphicsError:
    print("Turtle graphics error.")
except Terminator:
    print("Turtle window was closed.")
