import pygame, sys
from random import randint
from pygame.locals import *
from screen import *
from classes import *
from functions import *
from time import sleep

pygame.init()
global screen

clock = pygame.time.Clock()
tick = 15

#images
body = pygame.image.load("body.png")
headleft = pygame.image.load("head.png")
headright = pygame.transform.rotate(headleft, 180)
headup = pygame.transform.rotate(headleft, -90)
headdown = pygame.transform.rotate(headleft, 90)
headlist = [headup, headdown, headleft, headright]

appleicon = pygame.image.load("apple.jpg")

background = pygame.image.load("bg.jpg")

losefont = pygame.font.Font(None,100)
losetext = losefont.render("YOU LOSE!", 2, (0,0,0))
textbox = losetext.get_rect()
X = width/2 - textbox[2]/2
Y = height/2 - textbox[3]/2

scorefont = pygame.font.Font(None, 20)

#variables
direction = 'R'
slow = 60
collision = False
score = 0
changed = False

randx = randint(0,col)
randy = randint(0,row)

snakelist = [Snake(screen, randx * scale, randy * scale, headright),
Snake(screen, (randx - 1) * scale, randy * scale, body),
Snake(screen, (randx - 2) * scale, randy * scale, body),
Snake(screen, (randx - 3) * scale, randy * scale, body),
Snake(screen, (randx - 4) * scale, randy * scale, body),
Snake(screen, (randx - 5) * scale, randy * scale, body)]

apple = Apple(screen, 301, 301, appleicon)

time = 0

k = 1
while k:
	clock.tick(tick)
	screen.blit(background, (0,0))
	k += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			k = 0
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				k = 0
			elif event.key == K_w and direction !='D':
				direction = 'U'
			elif event.key == K_s and direction !='U':
				direction = 'D'
			elif event.key == K_a and direction !='R':
				direction = 'L'
			elif event.key == K_d and direction !='L':
				direction = 'R'

	draw_background(screen)
	scoretext = scorefont.render("SCORE: "+str(score), 2, (0,0,0))
	screen.blit(scoretext, (5,5))

	if collision == False:
		moveSnake(snakelist,direction, headlist, body)
		bound(snakelist)
		if eat(snakelist, apple):
			score += 10

			#speed increase
			if score == 300 and changed == False:
				tick += 3
				changed = True
			if score == 600 and changed == True:
				tick += 3
				changed = False
		

	for i in snakelist:
		i.draw()
	apple.draw()
	

	if snake_die(snakelist):
		collision = True
		if collision:
			screen.blit(losetext, (X,Y))


	pygame.display.flip()