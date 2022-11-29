# Importando as bibliotecas 
import pygame
import random
from os import path


pygame.mixer.init()
pygame.init()

# Tela principal 
titulo = 'SUPER MACIEL BROS'
width = 1200 #largura da tela 
height = 390 #altura da tela 
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('SUPER MACIEL BROS')
title_size = 100 #tamanho de cada titulo 
FPS = 30
w_m = 15
h_m = 30
w_p = 15
h_p = 15
x = 0 
y = 0

background = pygame.image.load('fundo_pygame.png').convert()
personagem_maciel = pygame.image.load('personagem_maciel.png')

def load_assets():
    assets = {}
    assets['mapa'] = pygame.image.load('sprite/fundo_pygame.png').convert_alpha()
    assets['mapa'] = pygame.transform.scale(assets['mapa'],(width,height)) 
    assets['personagem_maciel'] = pygame.image.load('sprite/personagem_maciel.png').convert_alpha()
    assets['personagem_maciel'] = pygame.transform.scale(assets['personagem_maciel'],(w_m,h_m))
    assets['pedra'] = pygame.image.load('sprite/pedra.png').convert_alpha()
    assets['pedra'] = pygame.transform.scale(assets['personagem_maciel'],(w_p,h_p))
    return assets

class pedra(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite_init_(self)

        self.image = assets['pedra']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.rect()
        self.rect.x = x
        self.rect.y = y 
        
    




#criando as classes 
class personagem_maciel(pygame.sprite.Sprite):


    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['personagem_maciel']
        self.maciel_padrao = True
        self.maciel_pular = False
        self.step_index = 0 
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.groups = groups
        self.assets = assets
        self.speedx = 0
        self.speedy = 0 
        
    def update(self):
        #inicia posçao
        posx = self.rect.x
        posy = self.rect.y
        #atualiza posiçao
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #mantendo dentro da tela 
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.blit(background, (0, 0))
    window.blit(personagem_maciel, (50, 216))
    pygame.display.update()


# Inicia estrutura de dados 
game = True
posicao_maciel = 1300

# Fazendo o personagem Pular 

# Fazendo o personagem andar
while game:
    clock = pygame.time.Clock()
    groups = dict
    all_sprites = pygame.sprite.Group()
    all_bricks = pygame.sprite.Group()
    groups['all_spites'] = all_sprites


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                personagem_maciel.speedx -= 8
            if event.key == pygame.K_RIGHT:
                personagem_maciel.speedx += 8 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                personagem_maciel.speedx -= 8
            if event.key == pygame.K_RIGHT:
                personagem_maciel.speedx += 8 
        

# Define algumas variaveis com as cores 


# Finalizaçao do jogo 
pygame.quit() # Funçao do pygame que Finaliza o jogo 


