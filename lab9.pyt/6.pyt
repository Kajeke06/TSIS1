import pygame
import time
from random import randrange, choice

pygame.init()

WIDTH = 500
HEIGHT = 500
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Menus Tutorial')
main_menu = True  # Изменено на True
font = pygame.font.Font('freesansbold.ttf', 24)
bg = pygame.transform.scale(pygame.image.load(r'C:/Users/User/Downloads/og_og_1661264244291838533.jpg'), (300, 300))
ball = pygame.transform.scale(pygame.image.load(r'C:/Users/User/Downloads/og_og_1661264244291838533.jpg'), (150, 150))
menu_command = 0
game_started = False  # Добавлено

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


def draw_menu():
    global game_started
    command = -1
    pygame.draw.rect(screen, 'black', [100, 100, 300, 300])
    screen.blit(bg, (100, 100))
    pygame.draw.rect(screen, 'green', [100, 100, 300, 300], 5)
    pygame.draw.rect(screen, 'white', [120, 120, 260, 40], 0, 5)
    pygame.draw.rect(screen, 'gray', [120, 120, 260, 40], 5, 5)
    txt = font.render('NazarSal', True, 'black')
    screen.blit(txt, (135, 127))

    if game_started:
        button1 = Button('Continue', (120, 180))
    else:
        button1 = Button('Ойнау', (120, 180))
    button1.draw()

    button2 = Button('Әуен', (120, 240))
    button2.draw()
    button3 = Button('Параметрлер', (120, 300))
    button3.draw()
    menu = Button('Шығу', (120, 350))
    menu.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command


def draw_game():
    global game_started
    menu_btn = Button('Бастау', (230, 450))
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    screen.blit(ball, (175, 175))
    return menu


def start_new_game():
    RES = 500
    SIZE = 50

    x, y = randrange(0, RES - SIZE, SIZE), randrange(0, RES - SIZE, SIZE)  # Получаем случайные координаты для змейки
    apple = randrange(0, RES - SIZE, SIZE), randrange(0, RES - SIZE, SIZE)  # Получаем случайные координаты для яблока
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    score = 0
    fps = 5

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
            apple = randrange(0, RES - SIZE, SIZE), randrange(0, RES - SIZE, SIZE)  # Обновляем позицию яблока
            length += 1
            score += 1
            fps += 1

        if time.time() - start_time > product_lifetime:
            start_time = time.time()
            product_weight = choice(['light', 'medium', 'heavy'])
            apple = randrange(0, RES - SIZE, SIZE), randrange(0, RES - SIZE, SIZE)  # Обновляем позицию яблока

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


run = True
while run:
    screen.fill('light blue')
    timer.tick(fps)
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
            if menu_command == 1:  # Если выбрана кнопка "Ойнау"
                game_started = True
    else:
        if not game_started:
            main_menu = draw_game()
        else:
            start_new_game()  # Запуск новой игры
            game_started = False  # Сброс переменной после завершения игры
        if menu_command > 0:
            text = font.render(f'Button {menu_command} pressed!', True, 'black')
            screen.blit(text, (150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
