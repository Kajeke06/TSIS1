import pygame
from datetime import datetime as dt

pygame.init()
screen = pygame.display.set_mode((590, 620))
pygame.display.set_caption("NazarSal")
icon = pygame.image.load(r'C:\Users\User\Downloads\Telegram Desktop\mainclock.png')
pygame.display.set_icon(icon)
kajeke = pygame.image.load(r'C:/Users/User/Downloads/photo_2024-03-23_20-22-00.jpg')
kajeke2 = pygame.image.load(r'C:/Users/User/Downloads/rightarm (3).png')
kajeke3 = pygame.image.load(r'C:/Users/User/Downloads/leftarm.png')

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((247, 219, 72))
    screen.blit(kajeke, (10, 10))

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pygame.transform.rotate(kajeke3, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(kajeke2, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center=(293, 305))
    rightarm_rect = rotated_rightarm.get_rect(center=(293, 305))

    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()