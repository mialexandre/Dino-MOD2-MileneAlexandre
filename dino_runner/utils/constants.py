import pygame
import os

# Global Constants
TITLE = "Ninja Girl Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Idle__000.png"))

pygame.mixer.init()

SOUNDTRACK = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/Otaku - Blue Bird (Naruto lofi)_36j1CVw8pfU.mp3"))

JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/smw_coin.wav"))

SHIELD_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/smw_1-up.wav"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__000.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__002.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__004.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__005.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__006.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__007.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__008.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__009.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__000.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__002.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__004.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__005.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__006.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__007.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__008.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Run__009.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Jump__005.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Jump__005.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__000.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__002.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__004.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__005.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__006.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__007.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__008.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__009.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__000.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__002.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__004.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__005.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__006.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__007.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__008.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NinjaGirl/Slide__009.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Kunai/Kunai.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Kunai/Kunai.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
