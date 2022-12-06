import pygame
import math
"""
Screen width & height
"""
sw = 800
sh = 800
"""
Background, Player and Enemy Images
"""
bg = pygame.image.load('./assets/images/space.png')
spaceship = pygame.image.load('./assets/images/spaceship.png')
asteroid = pygame.image.load('./assets/images/asteroid1.png')
asteroid = pygame.image.load('./assets/images/asteroid2.png')
asteroid = pygame.image.load('./assets/images/asteroid3.png')
asteroid = pygame.image.load('./assets/images/asteroid4.png')
asteroid = pygame.image.load('./assets/images/asteroid5.png')
asteroid = pygame.image.load('./assets/images/asteroid6.png')
"""
Title
"""
pygame.display.set_caption('Asteroid')
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

gameover = False

class Player(object):
    def __init__(self):
        self.img = spaceship
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh //2
        self.angle = 0
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def draw(self, win):
        #win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)
    """
    Movement
    """
    def turnleft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)
    
    def turnright(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)
    
    def moveforward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)
"""
Update Function
"""
def redrawGameWindow():
    win.blit(bg (0,0))
    player.draw(win)
    pygame.display.update()


player = Player()    
"""
Main While Loop
"""
run = True
while run:
    clock.tick(60)
    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnleft()
        if keys[pygame.K_RIGHT]:
            player.turnright()
        if keys[pygame.K_UP]:
            player.moveforward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False