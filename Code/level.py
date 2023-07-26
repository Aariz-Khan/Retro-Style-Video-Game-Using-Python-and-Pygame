import pygame
from csv_layout import import_layout

from settings import *
from player import Player
from map_objects import tile
from debug import debug
from csv_layout import *

class Level:
    def __init__(self):
        #fetching the display surface
        self.display_surface = pygame.display.get_surface()
        #sprite groups
        self.visible_sprites = horizontally_sorted_camera_group()
        self.collider_sprites = pygame.sprite.Group()

        
        #individual sprite setup
        self.create_map()

    def create_map(self):
        layouts = {
            "invisible wall": import_layout("C:/Users/Aariz Khan/CG_Project/Sprites/Tiles for TILED/Tile CSV/CG Floor_Ruin_Group 2_Invisible Wall.csv")
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != "-1":
                        x_pos = 2132-(column_index * TILESIZE)
                        y_pos = 1232-(row_index * TILESIZE)
                        if style == "invisible wall":
                            tile((x_pos,y_pos),[self.collider_sprites],"invisible")
        '''
                if column == 'x':
                    tile((x_pos,y_pos),[self.visible_sprites,self.collider_sprites])
                if column == 'p':
                    self.player = Player((x_pos,y_pos),[self.visible_sprites],self.collider_sprites)
        '''
        self.player = Player((2700,1500),[self.visible_sprites],self.collider_sprites)

    def run(self):
        #all the code to update and draw objects goes here
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        #debug(self.player.direction)

class horizontally_sorted_camera_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.width_half = self.display_surface.get_size()[0]//2
        self.height_half = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        #Creating the floor
        self.floor_surface = pygame.image.load("C:/Users/Aariz Khan/CG_Project/Sprites/Tiles for TILED/Floor Surface.png").convert()
        self.floor_rect = self.floor_surface.get_rect()
    def custom_draw(self, player):
        #fetching the offset for the floor
        self.offset.x = player.rect.centerx - self.width_half
        self.offset.y = player.rect.centery - self.height_half
        #drawing the floor 
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)
        

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_position)