from locale import normalize
from re import A
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collider_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../1 - level/graphics/player/down/down_0.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-16)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.collider_sprites = collider_sprites


#player movement

    #fetching inputs
    def player_input(self):
        key_pressed = pygame.key.get_pressed()
        #for y direction
        if key_pressed[pygame.K_w]:
            self.direction.y = -1
        elif key_pressed[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        #for x direction
        if key_pressed[pygame.K_a]:
            self.direction.x = -1
        elif key_pressed[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self,speed):
        #normalising speed while moving diagonally
        if self.direction.magnitude() != 0: #checking magnitude of vector is non zero
            self.direction = self.direction.normalize() #setting magnitude to 1
        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    #collider for sprites
    def collision(self,direction):
        if direction == "vertical":
            for sprite in self.collider_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
        if direction == "horizontal":
            for sprite in self.collider_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right
        
                    


        
        

    def update(self):
        self.player_input()
        self.move(self.speed)

        