import pygame
from config import widht, height
class personagem_maciel(pygame.sprite.Sprite):


    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img 
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



