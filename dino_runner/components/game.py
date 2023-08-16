import pygame


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.text_utils import draw_message_component

from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #largura e altura da janela
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 300
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu() # mostra o menu de restart
        pygame.display.quit() # voltar pro jogo
        pygame.quit() # sai do jogo

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()  # reseta os obstaculos para a velocidade inicial
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #cor do céu
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()   # flip traz movimento do jogo para parecer real

    def draw_background(self):
        image_width = BG.get_width() # bg é uma constante de background
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg + 85))    # blit junta as imagens para aparecer em conjunto, vai enfileirando as imgs tmb
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg + 85))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg + 85))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        draw_message_component(
            f"PONTUAÇÃO: {self.score}",
            self.screen,
            pos_x_center= 1000,
            pos_y_center= 50
        )

    def draw_power_up_time(self):   # quando pegar o escudo/martelo, vai definir os segundos restantes com ele
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} FALTAM {time_to_show} SEGUNDOS",
                    self.screen,
                    font_size= 18,
                    pos_x_center= 500,
                    pos_y_center= 40
                )
            else: 
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):    # definiu os dois menus (de iniciar e reiniciar)
        self.screen.fill((255, 255, 255))
        half_screen_heigth = SCREEN_HEIGHT // 2 # faz a divisão e não retorna numeros quebrados
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message_component("APERTE QUALQUER TECLA PARA INICIAR", self.screen)
        else:
            draw_message_component("PRESSIONE QUALQUER TECLA PARA REINICIAR", self.screen, pos_x_center= half_screen_heigth + 250, pos_y_center= half_screen_width - 350)
            draw_message_component(
                f"SUA PONTUAÇÃO: {self.score}",
                self.screen,
                pos_y_center= half_screen_width - 100
            )
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_heigth - 30)) # mexe com as dimensões do icone na janela
            
        pygame.display.flip() 
        self.handle_events_on_menu()
        
