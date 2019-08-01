global n
n = 0
global it
it = 0
global radius
radius = 300
global zoom
zoom = 1.0
global trans
trans = [350,350]
AUTO = False

def setup():
    size(700,700)
    global n
    
class dot_circle:
    def __init__(self, numOfDots, radius=300):
        self.numOfDots = numOfDots
        self.radius = radius
        self.angle_step = 2*PI/ self.numOfDots
        self.positions = [[self.radius*sin(angle-PI/2) for angle in [self.angle_step*i for i in range(numOfDots)]], [self.radius*sin(angle) for angle in [self.angle_step*i for i in range(numOfDots)]]]
         
    def _draw(self):
        for num in range(len(self.positions[0])):
            ellipse(self.positions[0][num], self.positions[1][num], 1,1)
            
    def times_table(self, whichTimesTable):
        for i in range(self.numOfDots):
            i2 = (i*whichTimesTable)%self.numOfDots
            stroke(255)
            if i2< self.numOfDots-1:
                if round(n) - n != 0:
                    line(self.positions[0][i], self.positions[1][i], self.positions[0][int(floor(i2))]+ abs(self.positions[0][int(ceil(i2))]-self.positions[0][int(floor(i2))])*(i2-floor(i2)), self.positions[1][int(floor(i2))]+ abs(self.positions[1][int(ceil(i2))]-self.positions[1][int(floor(i2))])*(i2-floor(i2)))
                else: 
                    i2 = int(i2)
                    line(self.positions[0][i], self.positions[1][i], self.positions[0][i2], self.positions[1][i2])

       
def keyP():
    global zoom
    if keyPressed ==True:
        if (key == CODED):
            if (keyCode == UP):
                trans[1] += 10
            if (keyCode == DOWN):
                trans[1] -= 10
            if (keyCode == RIGHT):
                trans[0] -= 10
            if (keyCode == LEFT):
                trans[0] += 10

        if (key == 'q'):
            global n
            n -= 0.05
        if (key == 'w'):
            global n
            n += 0.05
        if (key == '='):
            zoom *=1.05
        if (key == '-'):
            zoom *= 0.95
        circle = dot_circle(int(1000*zoom*zoom))
        strokeWeight(0.00001/zoom)


global circle
circle = dot_circle(700)

def draw():
    strokeWeight(0.00001)
    global n
    global it
    global circle
    global trans
    background(0)
    translate(trans[0], trans[1])
    global zoom
    scale(zoom)
    textSize(25)
    text(nf(n, 0, 2), width/2-150, height/2-50)

    keyP()
    if AUTO:
        n+=0.01
    circle._draw()
    circle.times_table(n)