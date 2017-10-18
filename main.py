WHITE  = (255,255,255)
BLACK  = (0,0,0)
BLUE   = (0,128,255)
ORANGE = (255,100,0)
block_size=200
n = 3
import pygame,math
from copy import deepcopy as copy
BOARD = [[0]*n]*n

def win():
	global BOARD
	for i in range(n):
		if BOARD[i][0]==BOARD[i][1]==BOARD[i][2]!=0:
			return True
		if BOARD[0][i]==BOARD[1][i]==BOARD[2][i]!=0:
			return True
	if BOARD[0][0]==BOARD[1][1]==BOARD[2][2]!=0:
		return True
	if BOARD[0][1]==BOARD[1][1]==BOARD[2][1]!=0:
		return True
	return False

pygame.init()
screen = pygame.display.set_mode((n*block_size,n*block_size))
screen.fill(WHITE)

done = False


pygame.display.flip()
clock = pygame.time.Clock()

turn=0
x,y=0,0

font = pygame.font.SysFont("comicsansms" , 72)
match_draw = font.render("DRAW!!!", True , BLUE)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y=pygame.mouse.get_pos()
			x = math.floor(x/block_size)
			y = math.floor(y/block_size)
			if BOARD[y][x]==0:	
				temp=copy(BOARD[y])
				temp[x]=turn%2+1
				BOARD[y]=temp
				turn+=1				
	
	screen.fill(WHITE)
	if not win() and turn != n**2:
		for x in range(n):
			for y in range(n):
				if BOARD[y][x]==0:
					rect=pygame.Rect(x*block_size,y*block_size,block_size,block_size)
					pygame.draw.rect(screen,BLACK,rect,5)
				elif BOARD[y][x]==1:
					rect=pygame.Rect(x*block_size,y*block_size,block_size,block_size)
					pygame.draw.rect(screen,BLUE,rect)
					pygame.draw.rect(screen,BLACK,rect,5)
				elif BOARD[y][x]==2:
					rect=pygame.Rect(x*block_size,y*block_size,block_size,block_size)
					pygame.draw.rect(screen,ORANGE,rect)
					pygame.draw.rect(screen,BLACK,rect,5)
	elif win():
		text = font.render("PLAYER-"+str((turn-1)%2+1)+" WINS!!!!" , True , BLUE)
		screen.blit(text , (n*block_size/2-text.get_width()//2 , n*block_size/2-text.get_height()//2))
	elif not win() and turn == n**2:
		screen.blit(match_draw , (n*block_size/2-match_draw.get_width()//2 , n*block_size/2-match_draw.get_height()//2))
	pygame.display.flip()
	clock.tick(60)
print("PLAYER-"+str(turn%2+1)+" WINS!!!!")