import pygame
from pygame.locals import *
import sys

pygame.init()
fpsClock = pygame.time.Clock()

surface = pygame.display.set_mode((800,600))

#while True:
 #   for event in pygame.event.get():
  #      if event.type == QUIT:
   #         pygame.quit()
    #        sys.exit()
anchura = 0
while anchura < 100: 
    pygame.draw.circle(surface, (0,0,255), (100+anchura,500), 10, 7)
    anchura += 1
anchura = 0
while anchura < 100: 
    pygame.draw.circle(surface, (255,150,0), (300+anchura,100), 10, 7)
    anchura += 1
pygame.display.update()
fpsClock.tick(30)
    
altura = 50

while altura < 550:       
    pygame.draw.circle(surface, (255,0,0), (150,altura), 40, 7)
    pygame.display.update()
    fpsClock.tick(30)
    pygame.draw.circle(surface, (0,0,0), (150,altura), 40, 7)
    altura += 5
anchura = 0
while anchura < 100: 
    pygame.draw.circle(surface, (0,0,255), (100+anchura,500), 10, 7)
    anchura += 1
pygame.display.update()
fpsClock.tick(30)
altura = 150
while altura < 600:       
    pygame.draw.circle(surface, (255,0,0), (350,altura), 40, 7)
    pygame.display.update()
    fpsClock.tick(30)
    pygame.draw.circle(surface, (0,0,0), (350,altura), 40, 7)
    altura += 5

   