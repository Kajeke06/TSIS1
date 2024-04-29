import pygame
from random import randrange, choice
import time
import psycopg2

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
    apple_color = 'red' 

    running = True
    while running:
        screen.fill(pygame.Color('black'))
        [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
        pygame.draw.rect(screen, pygame.Color(apple_color), (*apple, SIZE, SIZE))
        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
        screen.blit(render_score, (5, 5))
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
        if snake[-1] == apple:
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

def save_game_result(user_name, score):
    # Подключение к базе данных
    conn = psycopg2.connect(
        database="suppliers",
        user="User",
        password="Kajeke006",
        host="WIN-BL0JDSBR2NE",
        port="5432"
    )
    cur = conn.cursor()
    
    # Проверка, существует ли пользователь в базе данных
    cur.execute("SELECT user_id FROM users WHERE username = %s", (user_name,))
    existing_user = cur.fetchone()
    if existing_user:
        user_id = existing_user[0]
        cur.execute("UPDATE user_score SET score = %s WHERE user_id = %s", (score, user_id))

    else:
        # Если пользователя нет, добавляем его в таблицу
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (user_name,))
        user_id = cur.fetchone()[0]

    # Сохранение результатов игры с привязкой к пользователю
    cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
    conn.commit()
    cur.close()
    conn.close()

# Запрос имени игрока перед началом игры
user_name = input("Введите ваше имя: ")
start_new_game()