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
    Movement -
    Turn Left
    """
    def turnleft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    """
    Movement -
    Turn Right
    """

    def turnright(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    """
    Movement -
    Move Forward
    """

    def moveforward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transfrom.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    """
    If statement preventing the player to move off screen
    Player will appear on the opposite side of the board when moved out of view
    """
    def updateLocation(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = sw
        elif self.y < - 50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yw = self.s * 10

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])

    def checkOffScreen(self):
        if self.x <-50 or self.x > sw or self.y > sh or self.y <-50:
            return True

"""
Update Function
"""
def redrawGameWindow():
    win.blit(bg (0,0))
    player.draw(win)
    for b in playerBullets:
        b.draw(win)
    pygame.display.update()


player = Player()
playerBullets = []    
"""
Main While Loop
"""
run = True
while run:
    clock.tick(60)
    if not gameover:
        player.updateLocation()
        for b in playerBullets:
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    playerBullets.append(Bullet())
    
    redrawGameWindow()
pygame.quit()