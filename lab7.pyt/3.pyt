import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("NazarSal")
kajeke = pygame.image.load(r'C:/Users/User/Downloads/photo_2024-03-24_21-44-13.jpg')

music_files = [r"C:\Users\User\Downloads\Telegram Desktop\AlZaBi - 1503.mp3", r"C:\Users\User\Downloads\Telegram Desktop\Jah Khalib - 911.mp3", r"C:\Users\User\Downloads\Telegram Desktop\МОТ - Капкан.mp3"]
current_track = 0

pygame.mixer.music.load(music_files[current_track])

playing = False

running = True
while running:
    screen.blit(kajeke, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause() #probel pauza
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_s:  #s-toktaidy
                pygame.mixer.music.stop()
                playing = False
            elif event.key == pygame.K_n:  #n - kelesi an
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_p:  #p - aldyngy an
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
                playing = True

    pygame.display.update()

pygame.quit()