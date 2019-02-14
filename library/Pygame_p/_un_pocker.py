import pygame
import random

WIDTH = 640
HEIGHT = 480
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,128,0)
YELLOW = (255,255,0)
CARDW = 30
CARDH = 48
OUTSIDE = 999

class Cardclass(pygame.sprite.Sprite):
    def __init__(self,num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((CARDW,CARDH))
        self.rect = self.image.get_rect()
        self.num = num

def initcard():
    for sp in allgroup.sprites():
        sp.rect.centerx = OUTSIDE
        sp.rect.centery = OUTSIDE
    for pl in range(plmax):
        for i in range(5):
            opened = False
            if pl == plmy: opened = True
            setcard(pl,i,rndcard(),opened)
    sortcard(plmy)

def selectcard(cursor):
    x = cardx(cursor)
    y = cardy(plmy)
    pygame.draw.rect(screen,YELLOW,(x-(50/2),y-(68/2),50,68))
カードと日本語フォント用意してないや
