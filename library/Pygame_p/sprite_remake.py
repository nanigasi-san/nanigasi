import pygame
import random

WIDTH  = 640
HEIGHT = 480
BLUE   = (0,0,255)
GREEN  = (0,255,0)

#
number = 5
speed = 1000
#
class Spclass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("library/Pygame_p/SAKANA_x.png").convert()
        colorkey = self.image.get_at((0,0))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(WIDTH)
        self.rect.centery = random.randrange(HEIGHT)
        self.x1 = random.randrange(-3,3)
        self.y1 = random.randrange(-3,3)

    def update(self):
        self.rect.centerx += self.x1
        self.rect.centery += self.y1
        if self.rect.centerx >= WIDTH or self.rect.centerx < 0:
            self.x1 *= -1
        if self.rect.centery >= HEIGHT or self.rect.centery < 0:
            self.y1 *= -1

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
myclock = pygame.time.Clock()
allgroup = pygame.sprite.Group()
for i in range(number):
    allgroup.add(Spclass())

endflag = 0

while endflag == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: endflag = 1
    screen.fill(BLUE)
    allgroup.update()
    allgroup.draw(screen)
    myclock.tick(speed)
    pygame.display.flip()

pygame.quit()
