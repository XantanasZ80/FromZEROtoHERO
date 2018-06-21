import pygame
from pygame.locals import *
import random
#import sys

pygame.init()
fpsClock = pygame.time.Clock()

width = 480
height = 640

surface = pygame.display.set_mode((width, height))


archivo = open("marcianitos.txt")

contenido = archivo.readlines()

largo = len(contenido)
contador = 0
sprite = 1 #variable control de animacion
while contador < largo:
	elemento = contenido[contador].split()

	if elemento[0] == "nave":
		print("Cargando grafico nave:", elemento[1])
		nave_img = pygame.image.load(elemento[1])
		#Obtenemos el tamano y lo dividimos por 2
		nave_w,nave_h = nave_img.get_rect().size[0], nave_img.get_rect().size[1]
		nave_img = pygame.transform.scale(nave_img, (nave_w,nave_h))
	elif elemento[0] == "nave2": #Segunda nave para la animacion
		print("Cargando grafico nave2:", elemento[1])
		nave2_img = pygame.image.load(elemento[1])
		#Obtenemos el tamano y lo dividimos por 2
		nave_w,nave_h = nave_img.get_rect().size[0], nave_img.get_rect().size[1]
		nave2_img = pygame.transform.scale(nave2_img, (nave_w,nave_h))	
	elif elemento[0] == "marcianito1":
		print("Cargando grafico m1:", elemento[1])
		mar1_img = pygame.image.load(elemento[1])
		mar1_w,mar1_h = int(mar1_img.get_rect().size[0]/2),int(mar1_img.get_rect().size[1]/2)
		mar1_img = pygame.transform.scale(mar1_img, (mar1_w,mar1_h))
		mar1_w,mar1_h = mar1_img.get_rect().size[0],mar1_img.get_rect().size[1]
	elif elemento[0] == "marcianito2":
		print("Cargando grafico m2:", elemento[1])
		mar2_img = pygame.image.load(elemento[1])
		mar2_w,mar2_h = int(mar2_img.get_rect().size[0]/2),int(mar2_img.get_rect().size[1]/2)
		mar2_img = pygame.transform.scale(mar2_img, (mar2_w,mar2_h))
		mar2_w,mar2_h = mar2_img.get_rect().size[0],mar2_img.get_rect().size[1]
	elif elemento[0] == "marcianito3":
		print("Cargando grafico m3:", elemento[1])
		mar3_img = pygame.image.load(elemento[1])
		mar3_w,mar3_h = int(mar3_img.get_rect().size[0]/2),int(mar3_img.get_rect().size[1]/2)
		mar3_img = pygame.image.load(elemento[1])
	elif elemento[0] == "nodriza":
		print("Cargando grafico nave nodriza:", elemento[1])
		nodriza_img = pygame.image.load(elemento[1])
		nodriza_w,nodriza_h = int(nodriza_img.get_rect().size[0]/2),int(nodriza_img.get_rect().size[1]/2)
		nodriza_img = pygame.transform.scale(nodriza_img, (nodriza_w,nodriza_h))
	elif elemento[0] == "fondo":
		print("Cargando grafico fondo:", elemento[1])
		fondo_img = pygame.image.load(elemento[1])
		fondo_w,fondo_h = fondo_img.get_rect().size[0], fondo_img.get_rect().size[1]


	contador = contador + 1

nave_desp = 8
nave_x = 0

nodriza_x,nodriza_y = -2*nodriza_w ,0
nodriza_desp = 6
nodriza_dir = 1
nodriza_mov = False


mar1_x = 0
mar2_x = int(mar2_w)
marcianos_dir = 1

salir = False
while not salir:
	surface.fill((0,0,0))

	surface.blit(fondo_img, (0,0))

	surface.blit(nodriza_img, (nodriza_x, nodriza_y))

	if nodriza_mov:
		nodriza_x = nodriza_x + nodriza_dir * nodriza_desp
		if nodriza_x >= width:
			nodriza_mov = False
			nodriza_x = -2*nodriza_w
	else:
		modulo = random.randint(1,1000) % 500
		#print(modulo)
		if modulo == 0:
			nodriza_mov = True



	surface.blit(mar1_img, (mar1_x, height/2 - mar1_h/2))
	surface.blit(mar2_img, (mar2_x, height/2 - mar2_h/2))

	mar1_x = mar1_x + marcianos_dir * nave_desp/2
	mar2_x = mar2_x + marcianos_dir * nave_desp/2
	if mar2_x >= width - mar2_w:
		marcianos_dir = -1
	elif mar1_x <= 0:
		marcianos_dir =1

	if sprite == 1: #Animacion
		surface.blit(nave_img, (nave_x, height - nave_h))
	else:
		surface.blit(nave2_img, (nave_x, height - nave_h))
   
	pygame.display.update()
	fpsClock.tick(30)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and nave_x > 0:
		if sprite == 1: #Cambio de sprite cada LEFT
			sprite = 2
		else:
			sprite = 1
		nave_x = nave_x - nave_desp
	elif keys[pygame.K_RIGHT] and nave_x < width - nave_w:
		if sprite == 1: #Cambio de sprite cada RIGHT
			sprite = 2
		else:
			sprite = 1
		nave_x = nave_x + nave_desp

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			pygame.quit()
			salir = True
		
