import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite): 
    def __init__(self, image, type): # estruturando a imagem, estrutura inicial
        self.image = image 
        self.type = type # tipo do obstáculo
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed 
        if self.rect.x < -self.rect.width:
            obstacles.pop() 

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
        