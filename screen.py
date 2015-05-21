import pygame

pygame.init()

row = 25
col = 25
scale = 20

width = col * scale
height = row * scale
screen = pygame.display.set_mode((width,height))

line_color = 255,0,0


def draw_background(screen):
	for i in range(col):
		pygame.draw.line(screen, line_color, (i * scale, 0), (i * scale, height))
	for i in range(row):
		pygame.draw.line(screen, line_color, (0, i * scale), (width, i * scale))
