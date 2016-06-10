#!usr/bin/env python
def setup():
    size(500, 500)
    frameRate(10)
    background(255)

z = 30
y = 250
d = 2
x = 0.80
c = -0.05
def draw():
    global x, y, c, d, z
    stroke(0)
    fill(255, 220, 178)
    ellipse(250, y, 200, 200)
    fill(255)
    ellipse(280, 220, 20, z)
    if( x >= 0.75 or x <= 0.50):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(280+2*x, 223, 9, 13)
    fill(255)
    stroke(0)
    ellipse(220, 220, 20, z)
    if( x >= 0.75 or x <= 0.50):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(220+2*x, 223, 9, 13)

    fill(255)
    stroke(0)
    arc(250, 218, 120, 200, x, PI - x)
    fill(255, 220, 178)
    noStroke()
    quad(250, 218, 250, 257, 200, 300, 180, 270)
    quad(250, 218, 250, 257, 300, 300, 320, 270)
    stroke(0)
    arc(250, 257, 104, 104, x-0.1,PI - (x-0.1))
    line(250, 308, 250, 317)
    line(272, 303, 268, 311)
    line(226, 303, 230, 311)
    x = x + c
    if( x <= 0.45 or x >= 0.80):
        c = -c
    fill(0, 0, 255)
    #textSize(30)
    #text("HAHA !!", 200, 120)
    fill(255)
    y = y + d
    z = z + d
    if( y>= 266 or y <= 244):
        d = -d
