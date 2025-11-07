import pygame

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.set_volume(0.7)

def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()
