import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,800))
screen.fill('white')
pygame.display.set_caption('NazarSal')
clock = pygame.time.Clock()
x = 400
y = 400

run = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    ball = pygame.draw.circle(screen, 'red', center =(x, y), radius=25)
    

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x -= 20
            screen.fill('white')
        elif event.key == pygame.K_RIGHT:
            x += 20
            screen.fill('white')
        elif event.key == pygame.K_UP:
            y -= 20
            screen.fill('white')
        elif event.key == pygame.K_DOWN:
            y += 20
            screen.fill('white')
            
    if 0 >= x: x = 0 
    if x >= 800: x = 800
    if 0 >= y: y = 0 
    if y >= 800: y = 800
            
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)