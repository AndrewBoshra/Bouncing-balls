import pygame,random,sys


gravity=.05
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
        if self.y+self.speedy+self.radius>=720:
            self.y=720-self.radius
            self.speedy*=-.98
        else:
            self.speedy+=gravity
            self.y+=self.speedy

pygame.init()
screen=pygame.display.set_mode((1280,720))
balls=[]
for _ in range(200):
    radius=random.randint(15,40)
    print(radius)
    x=random.randrange(radius,1280-radius)
    y=random.randrange(radius,720-radius)
    color=(random.randrange(20,255),random.randrange(20,255),random.randrange(20,255))
    ball_gen=ball(x,y,radius,color)
    balls.append(ball_gen)

while True:

    for ball in balls:
        ball.updatePos()
    screen.fill((0,0,50))
    for ball in balls:
        ball.draw(screen)
    pygame.display.update()
    