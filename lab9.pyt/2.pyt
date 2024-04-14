import pygame
from random import randrange, choice
import time

def start_new_game():
    RES = 800
    SIZE = 50

    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    score = 0
    fps = 5

    pygame.init()
    screen = pygame.display.set_mode((RES, RES))
    pygame.display.set_caption("NazarSal")
    clock = pygame.time.Clock()
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    font_end = pygame.font.SysFont('Arial', 66, bold=True)

    product_lifetime = 5
    start_time = time.time()
    apple_color = 'red'  # Initialize apple color

    running = True
    while running:

        screen.fill(pygame.Color('black'))
        [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]

        # Draw apple with current color
        pygame.draw.rect(screen, pygame.Color(apple_color), (*apple, SIZE, SIZE))

        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
        screen.blit(render_score, (5, 5))
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
        if snake[-1] == apple:
            # Change apple color every other time it appears
            apple_color = 'yellow' if apple_color == 'red' else 'red'
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            length += 1
            score += 1
            fps += 1

        if time.time() - start_time > product_lifetime:
            start_time = time.time()
            product_weight = choice(['light', 'medium', 'heavy'])
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(1)
            return

        pygame.display.flip()
        pygame.display.update()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True}
        if key[pygame.K_s] and dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True}
        if key[pygame.K_a] and dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False}
        if key[pygame.K_d] and dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True}

start_new_game()