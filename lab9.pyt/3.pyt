import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # Check if X was clicked or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # Check if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    position = event.pos
                    points.append(position)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]: # left mouse button held down
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
                elif event.buttons[2]: # right mouse button held down
                    radius = min(200, radius + 1)
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        # Drawing additional shapes
        draw_square(screen, (100, 100), 50, mode)
        draw_triangle(screen, (250, 100), 50, mode)
        draw_equilateral_triangle(screen, (400, 100), 50, mode)
        draw_rhombus(screen, (550, 100), 50, mode)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def draw_square(screen, center, side_length, color_mode):
    # Drawing a square with center at given coordinates and side length
    rect = pygame.Rect(center[0] - side_length // 2, center[1] - side_length // 2, side_length, side_length)
    color = get_color(color_mode)
    pygame.draw.rect(screen, color, rect)

def draw_triangle(screen, top_point, side_length, color_mode):
    # Drawing an equilateral triangle with top point at given coordinates and side length
    height = int(side_length * (3 ** 0.5) / 2)
    color = get_color(color_mode)
    pygame.draw.polygon(screen, color, [(top_point[0], top_point[1]), 
                                        (top_point[0] - side_length // 2, top_point[1] + height), 
                                        (top_point[0] + side_length // 2, top_point[1] + height)])

def draw_equilateral_triangle(screen, top_point, side_length, color_mode):
    # Drawing an equilateral triangle with top point at given coordinates and side length
    height = int(side_length * (3 ** 0.5) / 2)
    color = get_color(color_mode)
    pygame.draw.polygon(screen, color, [(top_point[0], top_point[1]), 
                                        (top_point[0] - side_length // 2, top_point[1] + height), 
                                        (top_point[0] + side_length // 2, top_point[1] + height)])

def draw_rhombus(screen, center, side_length, color_mode):
    # Drawing a rhombus with center at given coordinates and side length
    half_diagonal = int(side_length * (2 ** 0.5) / 2)
    color = get_color(color_mode)
    pygame.draw.polygon(screen, color, [(center[0] - side_length // 2, center[1]), 
                                        (center[0], center[1] + half_diagonal), 
                                        (center[0] + side_length // 2, center[1]), 
                                        (center[0], center[1] - half_diagonal)])

def get_color(color_mode):
    # Getting color based on mode
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)

main()