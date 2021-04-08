import pygame
import pyautogui
from PIL import Image

def run(client_socket):

    width, height = pyautogui.size()

    table = Image.open("Table.png")
    width_table, height_table = table.size
    pygame.init()
    screen = pygame.display.set_mode(pyautogui.size())
    pygame.display.set_caption('Billiard')
    background_image = pygame.image.load("Table.png")
    background_image =  pygame.transform.scale(background_image, (width, round(width*height_table/width_table)) )
    ball_1 = pygame.image.load("Ball_1.png")
    ball_1 = pygame.transform.scale(ball_1, (65, 65))
    clock = pygame.time.Clock()
    screen.blit(background_image, [0, height/6])
    screen.blit(ball_1, [400, 400])

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                client_socket.close()
                running = False
        
        pygame.display.flip()
        clock.tick(30)