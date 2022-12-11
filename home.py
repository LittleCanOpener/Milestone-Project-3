import pygame
import math
import random
pygame.init()
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
lives = 3
score = 0

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
    If, statement preventing the player to move off screen
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

class  asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid1
        elif self.rank == 2:
            self.image = asteroid2
        else:
            self.image = asteroid3
        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([(random.randrange(0, sw-self.width), random.choice([-1*self.h - 5, sh + 5])), random.choice([-1*self.w -5, sw + 5], random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1,3)
        self.yv = self.ydir * random.randrange(1,3)
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


"""
Update Function, Lives Size & Postioning
"""
def redrawGameWindow():
    win.blit(bg (0,0))
    font = pygame.font.SysFont("arial", 30)
    livesText = font.render("Lives: " +str(lives), 1, (255, 255, 255))
    playAgainText = font.render("Press Space to Play Again", 1, (255, 255, 255))
    scoreText = font.render("Score: " +str(score), 1, (255, 255, 255))

    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    
    if gameover:
        win.blit(playAgainText, (sw//2-playAgainText.get_width()//2, sh//2 - playAgainText.get_height()//2))
    win.blit(scoreText, (sw- scoreText.get_width() -25, 25))
    win.blit(livesText, (25, 25))
    pygame.display.update()


player = Player()
playerBullets = []
asteroids = []
count = 0    


"""
Main While Loop
"""
run = True
while run:
    clock.tick(60)
    count += 1
    if not gameover:
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        player.updateLocation()
        for b in playerBullets:
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))
        """
        Asteroid movement and collision with player
        """
        for a in asteroids:
            a.x += a.xv
            a.y += a.yv

            if (player.x >= a.x and player.x <= a.x + a.w) or (player.x + player.w >= a.x and player.x + player.w <= a.x + a.w):
                if (player.y >= a.y and player.y <= a.y + a.h) or (player.y + player.h >= a.y and player.y + player.h <= a.y + a.h):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    break

        """
        Bullet Collision & Spawn smaller asteroids, Score
        """
        for b in playerBullets:
            if (b.x >= a.x and b.x <= a.x + a.w) or  b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                    if a.rank == 3:
                        score += 10
                        na1 = Asteroid(2)
                        na2 = Asteroid(2)
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(Asteroid(na1))
                        asteroids.append(Asteroid(na2))
                    elif a.rank == 2:
                        score += 20
                        na1 = Asteroid(1)
                        na2 = Asteroid(1)
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(Asteroid(na1))
                        asteroids.append(Asteroid(na1))
                    else:
                        score += 30
                    asteroids.pop(asteroids.index(a))
                    playerBullets.pop(playerBullets.index(b))

        if lives <= 0:
            gameover            

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
                else: 
                    gameover = False
                    lives = 3
                    asteroids.clear()
    
    redrawGameWindow()
pygame.quit()