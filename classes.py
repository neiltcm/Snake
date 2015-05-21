import pygame
from screen import *

pygame.init()

class Snake:
	def __init__(self, screen, x, y, image):
		self.screen = screen
		self.x = x
		self.y = y
		self.image = image

	def draw(self):
		self.screen.blit(self.image, (self.x, self.y))

class Apple(Snake):
	def __init__(self, screen, x, y, image):
		Snake.__init__(self, screen, x, y, image)




