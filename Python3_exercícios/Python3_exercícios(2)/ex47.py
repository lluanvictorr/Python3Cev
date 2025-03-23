import pygame
pygame.init()
from time import sleep
print('**************** CONTAGEM REGRESSIVA PARA 2025 ****************')
for contagem in range(10 , -1, -1,):
    print(contagem)
    sleep(1)
print('FELIZ ANO NOVO!!!')
pygame.mixer.music.load('ex47.mp3')
pygame.mixer.music.play(loops=3)
input()
pygame.event.wait()

