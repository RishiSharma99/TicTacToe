import pygame
from data import *
pygame.init()

n=int(input("No. Of tiles: "))
screen = pygame.display.set_mode((n*block_size , n*block_size))
screen.fill(WHITE)
board = Board()


done = False

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms" , 52)

row,col = 0,0

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			row = x//block_size
			col = y//block_size
			board.player_move(row , col)
	if not board.win():
		board.draw(screen)
	else:
		screen.fill(WHITE)
		if 0 in board.win_board:
			text = font.render("PLAYER-"+str((turn-1)%2+1)+" WINS!!!!" , True , BLACK)
			screen.blit(text , (n*block_size/2-text.get_width()//2 , n*block_size/2-text.get_height()//2))
		else:
			text = font.render("DRAW!!!" , True , BLACK)
			screen.blit(text , (n*block_size/2-text.get_width()//2 , n*block_size/2-text.get_height()//2))
		pygame.display.flip()
		
	clock.tick(60)