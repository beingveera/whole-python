import pygame_sdl2
pygame_sdl2.import_as_pygame()

def screen(wh,pos):
	global RENDERER,spritecache
	Sprite(RENDERER.load_texture(wh).render(at))
	
def update_display():
	RENDERER.render_present()
	RENDERER.clear((0,0,0))
	
uses=False

from itertools import cycle
import random,sys

import pygame
from pygame.locals import *
from pygame.render import *

ls=30
screen_width=500
screen_hight=1000


pipe_gap=250
base=screen_hight*.70

image, sound,hit={},{},{}

player =(
 

)

background=(


)


pipe_list=(


)

try:
	xrange
except NameError:
	xrange=range

def veera():
	global screen,clock,RENDERER
	pugame.init()
	clock=pygame.time.clock()
	screen=pygame.display.set_mode((screen_width,screen_hight))
	RENDERER=Renderer(None)
	pygame.display.set_caption("Veera Bird")
	
	if uses:
		global screen_bilt,update_display
		screen_bilt=screen
		update_display=display.update
	IMAGES['numbers'] = (pygame.image.load('assets/sprites/0.png').convert_alpha(), pygame.image.load('assets/sprites/1.png').convert_alpha(), pygame.image.load('assets/sprites/2.png').convert_alpha(), pygame.image.load('assets/sprites/3.png').convert_alpha(), pygame.image.load('assets/sprites/4.png').convert_alpha(), pygame.image.load('assets/sprites/5.png').convert_alpha(), pygame.image.load('assets/sprites/6.png').convert_alpha(), pygame.image.load('assets/sprites/7.png').convert_alpha(), pygame.image.load('assets/sprites/8.png').convert_alpha(), pygame.image.load('assets/sprites/9.png').convert_alpha())
	
	IMAGES['gameover'] = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
	
	IMAGES['message'] = pygame.image.load('assets/sprites/message.png').convert_alpha()
	
	IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()
	
	if 'win' in sys.platform:
		soundExt = '.wav'
	else:
		soundExt = '.ogg'
	
	SOUNDS['die'] = pygame.mixer.Sound('assets/audio/die' + soundExt)
	SOUNDS['hit'] = pygame.mixer.Sound('assets/audio/hit' + soundExt)
	SOUNDS['point'] = pygame.mixer.Sound('assets/audio/point' + soundExt)
	SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt)
	SOUNDS['wing'] = pygame.mixer.Sound('assets/audio/wing' + soundExt)
	
	while True:
		randombg = random.randint(0, len(background) - 1)
		IMAGES['background'] = pygame.image.load(background[randbg]).convert()
		
		randomPlayer = random.randint(0, len(player) - 1)
		IMAGES['player'] = (
            pygame.image.load(player[randomPlayer][0]).convert_alpha(),
            pygame.image.load(player[randomPlayer][1]).convert_alpha(),
            pygame.image.load(player[randomPlayer][2]).convert_alpha(),
        )
        
     random_pipe = random.randint(0, len(pipe_list)-1)
       IMAGES['pipe'] = (
            pygame.transform.rotate(pygame.image.load(random_pipe[pipe_list]).convert_alpha(), 180),
            pygame.image.load(random_pipe[pipe_list]).convert_alpha(),
        )
	
		