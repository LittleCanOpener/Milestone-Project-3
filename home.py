"""
The Classic Asteroid game 
"""
import pygame

"""
Screen width & height
"""
sw = 800
sh = 800
"""
Importing images onto the screen.
"""
bg = pygame.image.load('#')
spaceship = pygame.image.load('./assets/images/spaceship.png')
asteroid = pygame.image.load('./assets/images/#')
asteroid = pygame.image.load('./assets/images/#')
asteroid = pygame.image.load('./assets/images/#')
asteroid = pygame.image.load('./assets/images/#')
asteroid = pygame.image.load('./assets/images/#')
asteroid = pygame.image.load('./assets/images/#')

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

    def draw(self, win):
        win.blit(self.img, [self.x, self.y, self.w, self.x])

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
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False