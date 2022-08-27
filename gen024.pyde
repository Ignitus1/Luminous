movers = []
pg = None
saveIt = False

def setup():
    global pg, movers, c
    
    size(900, 900, P2D)
    pg = createGraphics(1080, 1080, P2D)
    pg.smooth(8)
    pg.beginDraw()
    pg.noStroke()
    pg.colorMode(HSB, 360, 100, 100, 100)
    pg.background(225, 100, 10)
    pg.blendMode(ADD)
    pg.ellipseMode(RADIUS)    
    
    #c = random(0, 360)
    
    for i in range(40):
        p = PVector(random(pg.width), random(pg.height))
        movers.append(Mover(p.copy()))
        
def draw():
    global saveIt, pg, movers
    
    pg.beginDraw()
    
    if frameCount < 3:
        pg.background(225, 100, 10)
        
    for mover in movers:
        mover.update()
        mover.show()
        
    if saveIt:
        pg.save(str(year()) + str(month()) + str(day()) + str(hour()) + str(minute()) + str(second()) + str(millis()) + '.png')
        saveIt = False
        
    pg.endDraw()
    image(pg, 0, 0, width, height)

def mouseClicked():
    global saveIt
    saveIt = True

class Mover:
    
    offset = 0
    steps = 0
    speed = 0
    
    def __init__(self, pos):
        self.pos = pos
        self.offset = random(TAU)
        self.speed = random(0.05, 0.6)
        self.c = random(0, 360)
        
    def update(self):
        if self.steps >= 200:
            self.steps = 0
            self.pos = PVector(random(pg.width), random(pg.height))
        th = self.offset + sin(radians(frameCount * self.speed)) * TAU
        self.pos.add(PVector.fromAngle(th).mult(1))
        self.steps += 1
        
    def show(self):
        th = self.offset + sin(radians(frameCount * 0.2))
        ft = 0.5 * (1 + sin(radians(frameCount * 3)))
        pg.fill(self.c, 60 + 30 * sin(th), 60, 4)
        pg.circle(self.pos.x, self.pos.y, 2 + 30 * pow(float(self.steps) / 200, 2))
