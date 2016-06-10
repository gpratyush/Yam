#!usr/bin/env python
def setup():
    size(500, 500)
    background(255)

x = 350
c = 1
def draw():
    global x, c
    fill(255, 220, 178)
    ellipse(250, 250, 200, 200)
    fill(255)
    ellipse(280, 220, 20, 40)
    if( x >= 390 or x <= 310):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(280+x/500.0, 223, 9, 13)
    fill(255)
    stroke(0)
    ellipse(220, 220, 20, 40)
    if( x >= 390 or x <= 310):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(220+x/500.0, 223, 9, 13)
    stroke(0)
    fill(255)
    arc(250, 350, 120 + x/10.0, 140 + x/10.0, PI + 0.5, 2*PI - 0.5)
    fill(255, 220, 178)
    arc(250, 351, 130 + x/10.0, 110 + x/10.0, PI + 0.62, 2*PI - 0.62)
    line(250, 264, 250, 278)
    line(285, 271, 280, 281)
    line(215, 270, 225, 280)
    x = x + c
    if( x >= 390 or x <= 310):
        c = -c
    fill(0, 0, 255)
    #textSize(30)
    #text("OH, NO !!", 180, 120)
    fill(255)
