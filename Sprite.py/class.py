import pygame 

class personagem_maciel(pygame.sprite.Sprite):
    x = 150
    y = 195 
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.maciel_padrao = True
        self.maciel_pular = False

        self.step_index = 0 
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



