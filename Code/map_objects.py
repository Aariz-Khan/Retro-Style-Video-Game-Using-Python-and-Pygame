import pygame
from settings import *
class tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        
        #self.rect_full_image = self.image.get_size()[0] * 0.125
        #self.hitbox = self.rect.inflate(0,-self.rect_full_image)
        self.hitbox = self.rect.inflate(0,-8)
        