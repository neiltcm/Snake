from screen import *
from classes import *
from random import randint

def bound(snakelist):
	for i in snakelist:
		if i.y < 0:
			i.y = height - scale 

		elif i.y >= height:
			i.y = 0 

		elif i.x < 0:
			i.x = width - scale

		elif i.x >= width:
			i.x = 0


def moveSnake(snakelist, direction, headlist, bodyimage):
	if direction == 'U':
		x = 0
		y = -1
		head = headlist[0]
	if direction == 'D':
		x = 0
		y = 1
		head = headlist[1]
	if direction == 'L':
		x = -1
		y = 0
		head = headlist[2]
	if direction == 'R':
		x = 1
		y = 0
		head = headlist[3]

	first = snakelist[0]
	screen = first.screen
	new_x = first.x + x * scale
	new_y = first.y + y * scale
	new_image = head
	newsnake = Snake(screen, new_x, new_y, new_image)
	snakelist[0].image = bodyimage
	snakelist.insert(0,newsnake)
	del snakelist[-1]

def apple_eat(head, apple):
	if (head.x == apple.x - 1 and head.y == apple.y - 1):
		return True

	else:
		return False

def eat(snakelist, apple):
	if apple_eat(snakelist[0], apple):
		apple.x = (randint(0,col-1) * scale) + 1
		apple.y = (randint(0,row-1) * scale) + 1
		
		last = snakelist[-1]
		secondlast = snakelist[-2]

		#going left
		if (last.y == secondlast.y and last.x < secondlast.x):
			snakelist.append(Snake(screen, last.x - scale, last.y, last.image))
		#going right
		elif (last.y == secondlast.y and last.x > secondlast.x):
			snakelist.append(Snake(screen, last.x + scale, last.y, last.image))
		#going up
		elif (last.y > secondlast.y and last.x == secondlast.x):
			snakelist.append(Snake(screen, last.x, last.y + scale, last.image))
		#going down
		elif (last.y < secondlast.y and last.x == secondlast.x):
			snakelist.append(Snake(screen, last.x, last.y - scale, last.image))

		return True
	return False




def snake_die(snakelist):
	first = snakelist[0]
	for i in range(1,len(snakelist)):
		if (first.x == snakelist[i].x and first.y == snakelist[i].y):
			return True
