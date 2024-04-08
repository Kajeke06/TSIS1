import sys, pygame
from pygame.locals import *
import random

pygame.init()

FPS = 60
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

zhol = pygame.image.load(r"C:\Users\User\Downloads\Telegram Desktop\photo_2024-04-01_22-35-50.jpg")
screen = pygame.display.set_mode((400, 600))
screen.fill('WHITE')
pygame.display.set_caption("NazarSal")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\User\Downloads\Telegram Desktop\photo_2024-04-01_22-36-18.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\User\Downloads\Telegram Desktop\photo_2024-04-01_22-33-18.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


P1 = Player()
C1 = Coin()

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(zhol, (0, 0))

    P1.move()

    scores = font_small.render(str(score), True, BLACK)
    screen.blit(scores, (380, 10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    collisions = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collisions:
        score += 1
        C1 = Coin()
        coins.add(C1)
        all_sprites.add(C1)

    pygame.display.update()
    clock.tick(FPS)