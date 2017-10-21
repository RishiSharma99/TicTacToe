WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (230,0,0)
BLUE  = (0,0,224)
turn  = 0
block_size = 120
n = 3

import pygame
pygame.init()

class Tile():
	def __init__(self):
		global block_size
		self.tile = pygame.Surface((block_size , block_size))

	def draw(self , row , col , value,screen):
		self.tile.fill(WHITE)
		global block_size , BLACK , BLUE , RED
		if value == 0:
			rect=pygame.Rect(0,0,block_size,block_size)
			pygame.draw.rect(self.tile , BLACK , rect ,5)
		if value == 1:
			pygame.draw.circle(self.tile , BLUE , (block_size//2 , block_size//2) , block_size//2 , 5)
			rect=pygame.Rect(0,0,block_size,block_size)
			pygame.draw.rect(self.tile , BLACK , rect ,5)
		if value == -1:
			pygame.draw.line(self.tile , RED , (0,0) , (block_size , block_size) , 5)
			pygame.draw.line(self.tile , RED , (block_size,0) , (0 , block_size) , 5)
			rect=pygame.Rect(0,0,block_size,block_size)
			pygame.draw.rect(self.tile , BLACK , rect ,5)
		screen.blit(self.tile , (row*block_size , col*block_size))
		pygame.display.flip()




class Board():
	def __init__(self):
		global n
		self.draw_board = [[0 for x in range(n)] for y in range(n)]
		self.win_board  = [0 for _ in range(2*n+2)]

	def test(self):
		print(self.win_board)

	def player_move(self , row , col):
		global turn , n
		a = 0
		if (turn%2==0):
			a = 1
		else:
			a = -1
		if self.draw_board[row][col]==0:
			
			self.draw_board[row][col] = a
			self.win_board[row]      += a
			self.win_board[n+col]    += a
			
			if (row==col):
				self.win_board[2*n]  += a
			
			if (row + col == n-1):
				self.win_board[2*n+1]+= a
			turn+=1

	def win(self):
		global n
		for e in self.win_board:
			if e==n or e==-n:
				return True
		return False

	def draw(self,screen):
		global n
		for row in range(n):
			for col in range(n):
				value = self.draw_board[row][col]
				box = Tile()
				box.draw(row , col , value , screen)

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
		if turn != n-1:
			text = font.render("PLAYER-"+str((turn-1)%2+1)+" WINS!!!!" , True , BLACK)
			screen.blit(text , (n*block_size/2-text.get_width()//2 , n*block_size/2-text.get_height()//2))
		else:
			text = font.render("DRAW!!!" , True , BLACK)
			screen.blit(text , (n*block_size/2-text.get_width()//2 , n*block_size/2-text.get_height()//2))
		pygame.display.flip()

	clock.tick(60)