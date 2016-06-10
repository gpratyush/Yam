#!usr/bin/env python
def setup():
    size(500, 500)
    background(255)

y = 1
x = 250
c = 0.3
d = 1
#string = { 'mail':'I AM READING YOUR MAIL !!','normal':'  I AM SAYING SOMETHING!!', }
def draw():
    global x, y, c, d
    fill(255, 220, 178)
    ellipse(x, 250, 200, 200)
    fill(255)
    ellipse(280, 220, 20, x/10.0)
    if( x >= 262 or x <= 238):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(280+x/500.0, 223, 9, 13)
    fill(255)
    stroke(0)
    ellipse(220, 220, 20, x/10.0)
    if( x >= 262 or x <= 238):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(220+x/500.0, 223, 9, 13)
    stroke(0)
    fill(255)
    arc(250, 229 , 130 - y, 170+y, 0.5, PI - 0.5)
    fill(255, 220, 178)
    arc(250, 228, 140, 140, 0.63+(y-3)/100.0, PI - 0.63-(y-3)/100.0)
    line(250, 299, 250, 314+y/1.5)
    line(280, 292, 275, 307+y/1.3)
    line(220, 292, 225, 307+y/1.3)
    x = x + c
    if( x >= 263 or x <= 237):
        c = -c
    fill(0, 0, 255)
    #textSize(30)
    #text(string['normal'], 40, 120)
    fill(255)
    y = y + d
    if( y >= 10 or y<= -10):
        d = -d
