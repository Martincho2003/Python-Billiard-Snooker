import pygame
import pyautogui

width, height = pyautogui.size()

pygame.init()
screen = pygame.display.set_mode(pyautogui.size())
pygame.display.set_caption('Billiard')
background_image = pygame.image.load("Table.png")
background_image =  pygame.transform.scale(background_image, pyautogui.size())
ball_1 = pygame.image.load("Ball_1.png")
ball_1 = pygame.transform.scale(ball_1, (65, 65))
screen.blit(ball_1, [400, 400])
clock = pygame.time.Clock()
screen.blit(background_image, [0,0])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(30)