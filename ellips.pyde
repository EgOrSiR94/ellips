x=10
y=10
def setup():
    size(800,800)
def draw():
    global x,y
    background(10)
    ellipse(x,y,x,y)
    x += 1
    y += 1
