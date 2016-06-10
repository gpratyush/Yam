#!usr/bin/env python
def setup():
    size(500, 500)
    background(255)
y = 250
x = 350
c = 1
d = 1
z = 250
e = 0.25
def draw():
    global x, c, y, d, z, e
    fill(255, 220, 178)
    ellipse(z, z, 200, 200)
    fill(255)
    ellipse(280, 220, 20, 40)
    if( x >= 390 or x <= 310):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(280+x/500.0, 223, 8, 23)
    fill(255)
    stroke(0)
    ellipse(220, 220, 20, 40)
    if( x >= 390 or x <= 310):
        fill(255)
        noStroke()
    else:
        fill(0)
    ellipse(220+x/500.0, 223, 8, 23)
    fill(255)
    stroke(0)
    #arc(250, 350, 120 + x/10.0, 90 + x/10.0, PI + 0.65, 2*PI - 0.65)
    arc(250, 350, 115 + x/10.0, 120 + x/10.0, PI + 0.8, 2*PI - 0.8)
    fill(255, 220, 178)
    noStroke()
    triangle(195, 294, 305, 294, 250, 350)
    stroke(0)
    line(199, 293, 301, 293)
    line(304, 202, 311, 211)
    line(311, 211, 318, 202)
    line(313, 213, 320, 204)
    line(313, 213, 320, 222)
    line(311, 215, 318, 224)
    line(311, 215, 304, 224)
    line(309, 213, 302, 222)
    line(309, 213, 302, 204)
    line(250, 272, 250, 292)
    line(285, 281, 280, 292)
    line(215, 281, 225, 292)
    x = x + c
    y = y + d
    if( x >= 390 or x <= 310):
        c = -c
    if( x <= 247 or x >= 353):
        d = -d
    fill(0, 0, 255)
    #textSize(30)
    #text("YOU SON OF A BITCH !!", 110, 120)
    noFill()
    #arc(220, 210, 25, 40 , PI + 0.7, 2*PI - 0.7)
    #arc(280, 210, 25, 40 , PI + 0.7, 2*PI - 0.7)
    line(205,205, 220, 190)
    line(220, 190, 235, 205)
    line(265,205, 280, 190)
    line(280, 190, 295, 205)
    stroke(0)
    fill(255)
    line(280, 180, 280, 188)
    line(267, 182, 271, 190)
    line(292, 182, 288, 190)
    line(220, 180, 220, 188)
    line(207, 182, 211, 190)
    line(232, 182, 228, 190)
    z = z + e
    if(z >= 255 or z <= 247):
        e = -e
    
    