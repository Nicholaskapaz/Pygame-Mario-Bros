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

background = pygame.image.load('fundo_pygame.png').convert()
personagem_maciel = pygame.image.load('personagem_maciel.png')

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