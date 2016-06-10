#!usr/bin/env python

def setup():
    size(500, 500)

x = 250
c = 0.3
def draw():
    global x,c
    background(255)
    fill(255, 220, 178)
    ellipse(x, 250, 200, 200)
    fill(255)
    ellipse(280, 220, 20, 40)
    if( x >= 262 or x <= 238):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(280+x/500.0, 223, 9, 13)
    fill(255)
    stroke(0)
    ellipse(220, 220, 20, 40)
    if( x >= 262 or x <= 238):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(220+x/500.0, 223, 9, 13)
    fill(255)
    stroke(0)
    arc(250, 230, 130, 170, 0.5, PI - 0.5)
    fill(255, 220, 178)
    arc(250, 228, 140, 140, 0.61, PI - 0.61)
    line(250, 299, 250, 314)
    line(280, 292, 275, 307)
    line(220, 292, 225, 307)
    x = x + c
    if( x >= 263 or x <= 237):
        c = -c
    fill(0, 0, 255)
    #textSize(30)
    #ext("HEY, I AM LISTENING YOU !!", 40, 120)
    fill(255)
