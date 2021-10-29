import random

'''
square(how many sides, radius, color)

hex(how many sides, radius, color)

shapedef(how many sides, radius, how much you want to turn left, color)

star(color)

multi(shape, radius, shape, radius)

spamcir(how many, radius, color, filled? ('true', 'false'))
'''
# square function
def square(x, y, z, a):
    color(z)
    if a == 'true':
        begin_fill()
        for i in range(x):
            left(90)
            forward(y)
        end_fill()
    else:
        for i in range(x):
            left(90)
            forward(y)

#hexagon function
def hex(x, y, z, a):
    color(z)
    if a == 'true':
        begin_fill()
        for i in range(x):
            forward(y)
            left(60)
    else:
        for i in range(x):
            forward(y)
            left(60)

#custom shape function
def shapedef(x,y,z,s,a):
    color(s)
    if a == 'true':
        begin_fill()
        for i in range(x):
            forward(y)
            left(z)
        end_fill()
    else:
        for i in range(x):
            forward(y)
            left(z)
# star function
def star(s, a):
    color(s)
    if a == 'true':
        begin_fill()
        circle(40,2500,5)
        end_fill()
    else:
        circle(40, 2500, 5)
    
# multiple shapes in 1 function, this can be used as a quick way to get 2 shapes on screen
def multi(x, y, z, f):
    if x == 'square':
        square(4, y, 'black')
    else:
        if x == 'hex':
            hex(6, y, 'black')
        else:
            if x == 'shapedef':
                shapedef(50, y, 20, 'black')
    if z == 'square':
        square(4, f, 'black')
    else:
        if z == 'hex':
            hex(6, f, 'black')
        else:
            if z == 'shapedef':
                shapedef(50, f, 20, 'black')
# spams circles in random places
def spamcir(x,y,z,a):
    color(z)
    # if they want it filled
    if a == 'true':
        begin_fill()
        for i in range(x):
            penup()
            setposition(random.randrange(-100,100), random.randrange(-100,100))
            pendown()
            circle(y)
        end_fill()
    else:
        # if they dont want it filled
        for i in range(x):
            penup()
            setposition(random.randrange(-100,100), random.randrange(-100,100))
            pendown()
            circle(y)
