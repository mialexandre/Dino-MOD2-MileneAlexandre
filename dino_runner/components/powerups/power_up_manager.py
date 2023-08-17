import random
import pygame

from dino_runner.components.powerups.shield import Shield
from dino_runner.utils.constants import SHIELD_SOUND


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score: # len para aleatoriedade
            self.when_appears += random.randint(200, 300) # a cada 200 e 300 pontos 
            self.power_ups.append(Shield()) # escudo aparece

    def update(self, score, game_speed, player): # atualiza pontuação e poderes
        self.generate_power_up(score) # atualiza o poder
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                SHIELD_SOUND.play() 
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000) # contagem de pontuação
                self.power_ups.remove(power_up) # remove o poder quando acabar o tempo do poder
    
    def draw(self, screen): # redesenha p dar continuidade
        for power_up in self.power_ups:
            power_up.draw(screen)                  

    def reset_power_ups(self): # resetando o poder, desaparece da tela quando sair da tela
        self.power_ups = []
        self.when_appears = random.randint(200, 300)