import pygame,random,sys


GRAVITY=.05
SWIDTH=int(input("Enter Screen Width:"))
SHEIGHT=int(input("Enter Screen Height:"))
BALLSNUM=int(input("Enter Balls Number:"))
COLLISIONFACTOR=.98
class ball:
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.speedy=0
        self.color=color
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def updatePos(self):
        #next position 
        if self.y+self.speedy+self.radius>=SHEIGHT:
            self.y=SHEIGHT-self.radius
            self.speedy*=-1*COLLISIONFACTOR
        else:
            self.speedy+=GRAVITY
            self.y+=self.speedy

pygame.init()
screen=pygame.display.set_mode((SWIDTH,SHEIGHT))
balls=[]
for _ in range(BALLSNUM):
    radius=random.randint(15,40)
    x=random.randrange(radius,SWIDTH-radius)
    y=random.randrange(radius,SHEIGHT-radius)
    color=(random.randrange(20,255),random.randrange(20,255),random.randrange(20,255))
    ball_gen=ball(x,y,radius,color)
    balls.append(ball_gen)

print("Simulation Started press any key to stop")
while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT , pygame.KEYDOWN):
            sys.exit()
    for ball in balls:
        ball.updatePos()
    screen.fill((0,0,50))
    for ball in balls:
        ball.draw(screen)
    pygame.display.update()
    