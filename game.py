import pygame
import pyautogui
from PIL import Image
from pygame.mouse import get_pos

radius = 15*2
ball_positions = [[280, 285],[670, 285],[670+radius, 285-(radius/2)-1],
                    [670+radius, 285+(radius/2)+1],[670+(radius*2), 285-radius-1],
                    [670+(radius*2), 285],[670+(radius*2), 285+radius+1],
                    [670+(radius*3), 285-(radius+(radius/2))-2],[670+(radius*3), 285-(radius/2)-1],
                    [670+(radius*3), 285+(radius/2)+1],[670+(radius*3), 285+(radius+(radius/2))+2],
                    [670+(radius*4), 285-(radius*2)-2],[670+(radius*4), 285-radius-1],
                    [670+(radius*4), 285],[670+(radius*4), 285+radius+1],
                    [670+(radius*4), 285+(radius*2)+2]]

class Visible_ball():
    def __init__(self, path):
        self.ball = pygame.image.load(path)
        self.ball = pygame.transform.scale(self.ball, (40, 40))

    def place(self, screen, x, y):
        screen.blit(self.ball, [x, y])

class Invisible_ball():
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.color = color
        self.ball = pygame.draw.circle(screen, color, (x, y), radius/2)

    def move(self, x, y):
        self.screen.fill("red")
        move_invisible_balls(self.screen)

def make_visible_balls(screen):
    white_ball = Visible_ball("Pictures/White_ball.png")
    white_ball.place(screen, 250, 250)

    ball1 = Visible_ball("Pictures/Ball_1.png")
    ball1.place(screen, 800, 400)

    ball11 = Visible_ball("Pictures/Ball_11.png")
    ball11.place(screen, 840, 430)

    ball3 = Visible_ball("Pictures/Ball_3.png")
    ball3.place(screen, 840, 370)

    ball6 = Visible_ball("Pictures/Ball_6.png")
    ball6.place(screen, 880, 340)

    ball8 = Visible_ball("Pictures/Ball_8.png")
    ball8.place(screen, 880, 400)

    ball14 = Visible_ball("Pictures/Ball_14.png")
    ball14.place(screen, 880, 460)

    ball13 = Visible_ball("Pictures/Ball_13.png")
    ball13.place(screen, 920, 330)

    ball15 = Visible_ball("Pictures/Ball_15.png")
    ball15.place(screen, 920, 370)

    ball4 = Visible_ball("Pictures/Ball_4.png")
    ball4.place(screen, 920, 430)

    ball9 = Visible_ball("Pictures/Ball_9.png")
    ball9.place(screen, 920, 460)

    ball7 = Visible_ball("Pictures/Ball_7.png")
    ball7.place(screen, 960, 340)

    ball2 = Visible_ball("Pictures/Ball_2.png")
    ball2.place(screen, 960, 370)

    ball10 = Visible_ball("Pictures/Ball_10.png")
    ball10.place(screen, 960, 400)

    ball5 = Visible_ball("Pictures/Ball_5.png")
    ball5.place(screen, 960, 430)

    ball12 = Visible_ball("Pictures/Ball_12.png")
    ball12.place(screen, 960, 460)
    
def move_invisible_balls(screen):
    white_ball = Invisible_ball(screen, ball_positions[0][0], ball_positions[0][1], (255,255,255))
    
    ball1 = Invisible_ball(screen, ball_positions[1][0], ball_positions[1][1], (0,0,0))
    ball11 = Invisible_ball(screen, ball_positions[2][0], ball_positions[2][1], (0,0,0))
    ball3 = Invisible_ball(screen, ball_positions[3][0], ball_positions[3][1], (0,0,0))
    ball6 = Invisible_ball(screen, ball_positions[4][0], ball_positions[4][1], (0,0,0))
    ball8 = Invisible_ball(screen, ball_positions[5][0], ball_positions[5][1], (0,0,0))
    ball14 = Invisible_ball(screen, ball_positions[6][0], ball_positions[6][1], (0,0,0))
    ball13 = Invisible_ball(screen, ball_positions[7][0], ball_positions[7][1], (0,0,0))
    ball15 = Invisible_ball(screen, ball_positions[8][0], ball_positions[8][1], (0,0,0))
    ball4 = Invisible_ball(screen, ball_positions[9][0], ball_positions[9][1], (0,0,0))
    ball9 = Invisible_ball(screen, ball_positions[10][0], ball_positions[10][1], (0,0,0))
    ball7 = Invisible_ball(screen, ball_positions[11][0], ball_positions[11][1], (0,0,0))
    ball2 = Invisible_ball(screen, ball_positions[12][0], ball_positions[12][1], (0,0,0))
    ball10 = Invisible_ball(screen, ball_positions[13][0], ball_positions[13][1], (0,0,0))
    ball5 = Invisible_ball(screen, ball_positions[14][0], ball_positions[14][1], (0,0,0))
    ball12 = Invisible_ball(screen, ball_positions[15][0], ball_positions[15][1], (0,0,0))

def draw_table(screen):
    pygame.draw.line(screen, (0,0,0), (105,63), (470,63))
    pygame.draw.line(screen, (0,0,0), (532,63), (905,63))
    pygame.draw.line(screen, (0,0,0), (936,106), (937,466))
    pygame.draw.line(screen, (0,0,0), (105,508), (470,508))
    pygame.draw.line(screen, (0,0,0), (532,508), (905,508))
    pygame.draw.line(screen, (0,0,0), (64,106), (64,466))

def draw_holes(screen):
    pygame.draw.circle(screen, (0,0,0), (66, 66), 11)
    pygame.draw.circle(screen, (0,0,0), (501, 41), 11)
    pygame.draw.circle(screen, (0,0,0), (939, 66), 11)
    pygame.draw.circle(screen, (0,0,0), (66, 507), 11)
    pygame.draw.circle(screen, (0,0,0), (501, 533), 11)
    pygame.draw.circle(screen, (0,0,0), (939, 507), 11)

def run():#client_socket):
    width, height = pyautogui.size()
    table = Image.open("Pictures/Table.png")
    icon = pygame.image.load("Pictures/Icon.png")
    icon = pygame.transform.scale(icon, (32, 32))
    width_pic, height_pic = table.size
    pygame.init()
    screen = pygame.display.set_mode((1000, round((1000*height_pic)/width_pic)), pygame.DOUBLEBUF, 32)
    invisible_layer = pygame.Surface((1000, round((1000*height_pic)/width_pic)))
    invisible_layer.set_alpha(128)
    print(round((1000*height_pic)/width_pic))
    visible_layer = pygame.Surface((1000, round((1000*height_pic)/width_pic)))
    visible_layer.set_alpha(255)
    pygame.display.set_caption('Billiard')
    pygame.display.set_icon(icon)
    background_image = pygame.image.load("Pictures/Table.png")
    background_image = pygame.transform.scale(background_image, (1000, round((1000*height_pic)/width_pic )))
    clock = pygame.time.Clock()
    visible_layer.blit(background_image, [0,0])
    screen.blit(invisible_layer, [0,0])
    draw_table(visible_layer)
    draw_holes(visible_layer)

    white_ball = Invisible_ball(visible_layer, ball_positions[0][0], ball_positions[0][1], (255,255,255))
    ball1 = Invisible_ball(visible_layer, ball_positions[1][0], ball_positions[1][1], (0,0,0))
    ball11 = Invisible_ball(visible_layer, ball_positions[2][0], ball_positions[2][1], (0,0,0))
    ball3 = Invisible_ball(visible_layer, ball_positions[3][0], ball_positions[3][1], (0,0,0))
    ball6 = Invisible_ball(visible_layer, ball_positions[4][0], ball_positions[4][1], (0,0,0))
    ball8 = Invisible_ball(visible_layer, ball_positions[5][0], ball_positions[5][1], (0,0,0))
    ball14 = Invisible_ball(visible_layer, ball_positions[6][0], ball_positions[6][1], (0,0,0))
    ball13 = Invisible_ball(visible_layer, ball_positions[7][0], ball_positions[7][1], (0,0,0))
    ball15 = Invisible_ball(visible_layer, ball_positions[8][0], ball_positions[8][1], (0,0,0))
    ball4 = Invisible_ball(visible_layer, ball_positions[9][0], ball_positions[9][1], (0,0,0))
    ball9 = Invisible_ball(visible_layer, ball_positions[10][0], ball_positions[10][1], (0,0,0))
    ball7 = Invisible_ball(visible_layer, ball_positions[11][0], ball_positions[11][1], (0,0,0))
    ball2 = Invisible_ball(visible_layer, ball_positions[12][0], ball_positions[12][1], (0,0,0))
    ball10 = Invisible_ball(visible_layer, ball_positions[13][0], ball_positions[13][1], (0,0,0))
    ball5 = Invisible_ball(visible_layer, ball_positions[14][0], ball_positions[14][1], (0,0,0))
    ball12 = Invisible_ball(visible_layer, ball_positions[15][0], ball_positions[15][1], (0,0,0))

    screen.blit(visible_layer, [0,0])
    

    running = True

    while running:
        for event in pygame.event.get():
            print(get_pos())
            if event.type == pygame.QUIT:
                #client_socket.close()
                running = False
            if event.type == pygame.KEYDOWN:
                ball_positions[0][1] += 1
                white_ball.move(ball_positions[0][0], ball_positions[0][1])

        screen.blit(visible_layer, [0,0])
        pygame.display.flip()
        clock.tick(30)

run()