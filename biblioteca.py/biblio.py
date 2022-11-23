# Importando as bibliotecas 
import pygame
import random
from os import path

pygame.mixer.init()
pygame.init()

# Tela principal 
titulo = 'SUPER MACIEL BROS'
width = 1000 #largura da tela 
height = 800 #altura da tela 
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('SUPER MACIEL BROS')
title_size = 100 #tamanho de cada titulo 
FPS = 30

background = pygame.image.load('fundo_pygame.png').convert()

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.blit(background, (0, 0))
    pygame.display.update()
