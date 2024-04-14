import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

width = 800
height = 600
active_size = 0
active_color = 'white'

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("NazarSal")
painting = []

def draw_menu(size, color):
    pygame.draw.rect(screen, 'gray', [0, 0, width, 90])
    pygame.draw.line(screen, 'black', [0, 90], [ width, 90], 3)
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 70, 70])
    pygame.draw.circle(screen, 'white', (45, 45), 34)
    l_brush = pygame.draw.rect(screen, 'black', [90, 10, 70, 70])
    pygame.draw.circle(screen, 'white', (125, 45), 25)
    s_brush = pygame.draw.rect(screen, 'black', [170, 10, 70, 70])
    pygame.draw.circle(screen, 'white', (205, 45), 15)
    m_brush = pygame.draw.rect(screen, 'black', [250, 10, 70, 70])
    pygame.draw.circle(screen, 'white', (285, 45), 5)
    brush_list = [xl_brush, l_brush, s_brush, m_brush]
    if size == 20:
        pygame.draw.rect(screen, 'green', [10, 10, 70, 70], 3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', [90, 10, 70, 70], 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', [170, 10, 70, 70], 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', [250, 10, 70, 70], 3)
    
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    
    blue = pygame.draw.rect(screen, (0, 0, 255), [width - 40, 10, 30, 30])
    orange = pygame.draw.rect(screen, (255, 166, 0), [width - 90, 10, 30, 30])
    green = pygame.draw.rect(screen, (0, 255, 51), [width - 140, 10, 30, 30])
    red = pygame.draw.rect(screen, (255, 0, 0), [width - 190, 10, 30, 30])
    brown = pygame.draw.rect(screen, (153, 85, 50), [width - 40, 50, 30, 30])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [width - 90, 50, 30, 30])
    purple = pygame.draw.rect(screen, (95, 50, 153), [width - 140, 50, 30, 30])
    black = pygame.draw.rect(screen, (0, 0, 0), [width - 190, 50, 30, 30])
    white = pygame.draw.rect(screen, (255, 255, 255), [width - 260, 20, 50, 50])
    color_rect = [blue, orange, green, red, brown, yellow, purple, black, white]
    rgb_list = [(0, 0, 255), (255, 166, 0), (0, 255, 51), (255, 0, 0), (153, 85, 50), (255, 255, 0), (95, 50, 153), (0, 0, 0), (255, 255, 255)]
    
    return brush_list, color_rect, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])


running = True
while running:
    clock.tick(FPS)
    screen.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))
    
    draw_painting(painting)
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, rgbs= draw_menu(active_size, active_color)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
                    
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            
    pygame.display.flip()
pygame.quit()