import pygame
import time
import pyautogui
import pickle
from PIL import Image
from math import sqrt, fabs
from pygame.mouse import get_pos


radius = 15*2
invisible_ball_positions = [[280, 285],[670, 285],[670+radius, 285-(radius/2)-1],
                    [670+radius, 285+(radius/2)+1],[670+(radius*2), 285-radius-1],
                    [670+(radius*2), 285],[670+(radius*2), 285+radius+1],
                    [670+(radius*3), 285-(radius+(radius/2))-2],[670+(radius*3), 285-(radius/2)-1],
                    [670+(radius*3), 285+(radius/2)+1],[670+(radius*3), 285+(radius+(radius/2))+2],
                    [670+(radius*4), 285-(radius*2)-2],[670+(radius*4), 285-radius-1],
                    [670+(radius*4), 285],[670+(radius*4), 285+radius+1],
                    [670+(radius*4), 285+(radius*2)+2]]

visible_ball_positions = [[(s-25) for s in xs] for xs in invisible_ball_positions]

class Visible_ball():
    def __init__(self, path):
        self.ball = pygame.image.load(path)
        self.ball = pygame.transform.scale(self.ball, (50, 50))

    def place(self, screen, x, y):
        screen.blit(self.ball, [x, y])

class Invisible_ball():
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.color = color
        self.ball = pygame.draw.circle(screen, color, (x, y), radius/2)

    def move(self, x, y):
        self.screen.fill("red")
        make_invisible_balls(self.screen)

        
def move_visible_balls(screen, bals):
    bals[0].place(screen, visible_ball_positions[0][0], visible_ball_positions[0][1])
    pygame.draw.line(screen, (255,255,255), (invisible_ball_positions[0][0],invisible_ball_positions[0][1]), get_pos())
    bals[1].place(screen, visible_ball_positions[1][0], visible_ball_positions[1][1])
    bals[11].place(screen, visible_ball_positions[2][0], visible_ball_positions[2][1])
    bals[3].place(screen, visible_ball_positions[3][0], visible_ball_positions[3][1])
    bals[6].place(screen, visible_ball_positions[4][0], visible_ball_positions[4][1])
    bals[8].place(screen, visible_ball_positions[5][0], visible_ball_positions[5][1])
    bals[14].place(screen, visible_ball_positions[6][0], visible_ball_positions[6][1])
    bals[13].place(screen, visible_ball_positions[7][0], visible_ball_positions[7][1])
    bals[15].place(screen, visible_ball_positions[8][0], visible_ball_positions[8][1])
    bals[4].place(screen, visible_ball_positions[9][0], visible_ball_positions[9][1])
    bals[9].place(screen, visible_ball_positions[10][0], visible_ball_positions[10][1])
    bals[7].place(screen, visible_ball_positions[11][0], visible_ball_positions[11][1])
    bals[2].place(screen, visible_ball_positions[12][0], visible_ball_positions[12][1])
    bals[10].place(screen, visible_ball_positions[13][0], visible_ball_positions[13][1])
    bals[5].place(screen, visible_ball_positions[14][0], visible_ball_positions[14][1])
    bals[12].place(screen, visible_ball_positions[15][0], visible_ball_positions[15][1])

def make_invisible_balls(screen):
    white_ball = Invisible_ball(screen, invisible_ball_positions[0][0], invisible_ball_positions[0][1], (255,255,255))

    ball1 = Invisible_ball(screen, invisible_ball_positions[1][0], invisible_ball_positions[1][1], (0,255,0))
    ball11 = Invisible_ball(screen, invisible_ball_positions[2][0], invisible_ball_positions[2][1], (0,255,0))
    ball3 = Invisible_ball(screen, invisible_ball_positions[3][0], invisible_ball_positions[3][1], (0,255,0))
    ball6 = Invisible_ball(screen, invisible_ball_positions[4][0], invisible_ball_positions[4][1], (0,255,0))
    ball8 = Invisible_ball(screen, invisible_ball_positions[5][0], invisible_ball_positions[5][1], (0,255,0))
    ball14 = Invisible_ball(screen, invisible_ball_positions[6][0], invisible_ball_positions[6][1], (0,255,0))
    ball13 = Invisible_ball(screen, invisible_ball_positions[7][0], invisible_ball_positions[7][1], (0,255,0))
    ball15 = Invisible_ball(screen, invisible_ball_positions[8][0], invisible_ball_positions[8][1], (0,255,0))
    ball4 = Invisible_ball(screen, invisible_ball_positions[9][0], invisible_ball_positions[9][1], (0,255,0))
    ball9 = Invisible_ball(screen, invisible_ball_positions[10][0], invisible_ball_positions[10][1], (0,255,0))
    ball7 = Invisible_ball(screen, invisible_ball_positions[11][0], invisible_ball_positions[11][1], (0,255,0))
    ball2 = Invisible_ball(screen, invisible_ball_positions[12][0], invisible_ball_positions[12][1], (0,255,0))
    ball10 = Invisible_ball(screen, invisible_ball_positions[13][0], invisible_ball_positions[13][1], (0,255,0))
    ball5 = Invisible_ball(screen, invisible_ball_positions[14][0], invisible_ball_positions[14][1], (0,255,0))
    ball12 = Invisible_ball(screen, invisible_ball_positions[15][0], invisible_ball_positions[15][1], (0,255,0))

def draw_table(screen):
    pygame.draw.line(screen, (0,0,0), (105,63), (470,63))
    pygame.draw.line(screen, (0,0,0), (532,63), (905,63))
    pygame.draw.line(screen, (0,0,0), (936,106), (936,466))
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

def find_distance(x1,y1,x2,y2):
    if (x1 - x2) == 0:
        if (y1 - y2) > 0:
            return (y1 - y2)
        else:
            return y2 - y1
    elif y1 - y2 == 0:
        if x1 - x2 > 0 :
            return x1 - x2
        else:
            return x2 - x1
    else:
        c = x2 - x1
        d = y2 - y1
        return sqrt(((c)*(c)) + ((d)*(d)))

def move_ball(x1,y1,x2,y2, distans, visible_screen, screen, background, bals):
    end = 0
    ax = 64
    ay = 508
    bx = 936
    by = 508
    cx = 936
    cy = 64
    dy = 64
    urav_a = -(y1 - y2)/(x1 - x2)
    urav_b = y1 - urav_a*x1
    print(distans)
    dist = distans
    distance = 0
    if dist > 100:
        distance = 12*100
    else:
        distance = 12*dist
    cur_distance = 0
    print(distance)
    curx = 0
    cury = 0
    udar1 = 0 
    udar2 = 0
    if x1 > x2 and y1 > y2: # down and left
        print("down and left")
        for i in range(x1, -1000):
            curx = i
            visible_ball_positions[0][0] = curx
            cury = round(urav_a*curx + urav_b)
            visible_ball_positions[0][1] = cury
            cur_distance = find_distance(x1,y1,curx,cury)
    
            if curx == ax + radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar1 = 1
            if cury - radius/2 == ay and udar2 == 0 and end == 0:
                curx = -(urav_b - cury)/urav_a
                udar2 = 1
            if round(distance) - round(cur_distance) < 5:
                break
            move_visible_balls(visible_screen, bals)
        
    elif x1 > x2 and y1 < y2: # up and left
        print("up and left")
        for i in range(x1, -1000):
            curx = i
            cury = round(urav_a*curx + urav_b)
            cur_distance = find_distance(x1,x2,curx,cury)
            
            if curx == ax + radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar1 = 1
            if cury == dy - radius/2 and udar2 == 0 and end == 0:
                curx = -(urav_b - cury)/urav_a
                udar2 = 1
            if round(distance) == round(cur_distance):
                break
    
    elif x1 < x2 and y1 > y2: # down and right
        print("down and right")
        for i in range(x1, 1000 + 1, 3):
            curx = i
            cury = round(urav_a*curx + urav_b)
            invisible_ball_positions[0][0] = curx 
            invisible_ball_positions[0][1] = cury
            visible_ball_positions[0][0] = curx - 25
            visible_ball_positions[0][1] = cury - 25
            cur_distance = find_distance(x1,y1,curx,cury)
            if curx == bx - radius/2 and udar1 == 0  and end == 0:
                cury = urav_a*curx + urav_b
                udar1 = 1
            if cury - radius/2 == by and udar2 == 0  and end == 0:
                curx = -(urav_b - cury)/urav_a
                udar2 = 1
            if round(distance) - round(cur_distance) < 5:
                break
            move_visible_balls(visible_screen, bals)
            update_picure(screen, visible_screen, background, bals)
            pygame.display.flip()

    
    elif x1 < x2 and y1 < y2:#up and right
        print("up and right")
        for i in range(x1, 1000 + x1, 3):
            curx = i
            cury = round(urav_a*curx + urav_b)
            cur_distance = find_distance(x1,x2,curx,cury)
            invisible_ball_positions[0][0] = curx 
            invisible_ball_positions[0][1] = cury
            visible_ball_positions[0][0] = curx - 25
            visible_ball_positions[0][1] = cury - 25
            if curx == cx - radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar1 = 1
            if cury == cy - radius/2 and udar2 == 0 and end == 0:
                curx = -(urav_b - cury)/urav_a
                udar2 = 1
            if round(distance) - round(cur_distance) < 5:
                break
            move_visible_balls(visible_screen, bals)
            update_picure(screen, visible_screen, background, bals)
            pygame.display.flip()
    
    elif x1 == x2 and y1 > y2:#down
        curx = x2
        for i in range(y1, -1000):
            cury = i
            cur_distance = find_distance(x1,x2,curx,cury)
            if cury - radius/2 == ay and udar1 == 0 and end == 0:
                udar1 = 1
            if cury == cy - radius/2 and udar2 == 0 and end == 0:
                udar2 = 1
            if round(distance) == round(cur_distance):
                break
    
    elif x1 == x2 and y1 < y2: #up
        curx = x2
        for i in range(y1, 1000):
            cury = i
            cur_distance = find_distance(x1,x2,curx,cury)
            if cury - radius/2 == ay and udar1 == 0 and end == 0:
                udar1 = 1
            if cury == cy - radius/2 and udar2 == 0 and end == 0:
                udar2 = 1
            if round(distance) == round(cur_distance):
                break
    
    elif x1 > x2 and y1 == y2:#left
        cury = y2
        for i in range(x1, -1000):
            curx = i
            cur_distance = find_distance(x1,x2,curx,cury)

            if curx == ax + radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar1 = 1
            if curx == cx - radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar2 = 1
            if round(distance) == round(cur_distance):
                break
            
    elif x1 < x2 and y1 == y2:#right
        cury = y2
        for i in range(x1, 1000):
            curx = i
            cur_distance = find_distance(x1,x2,curx,cury)
            
            if curx == ax + radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar1 = 1
            if curx == cx - radius/2 and udar1 == 0 and end == 0:
                cury = urav_a*curx + urav_b
                udar2 = 1
            if round(distance) == round(cur_distance):
                break

def update_picure(screen, visible, background_image, bals):
    screen.fill([0,0,0])
    visible.blit(background_image, [0,0])
    move_visible_balls(visible, bals)
    screen.blit(visible, [0,0])

def send_pickle(msg, client_socket):
    try:
        msg = pickle.dumps(msg)
        client_socket.send(msg)
        recv_msg = client_socket.recv(1024)
        recv_msg = pickle.loads(recv_msg)
        print(recv_msg)
        if recv_msg:
            return recv_msg
    except Exception as e:
        print("Server is down or something..")
        print(e)
        client_socket.close()
        exit(0)

def receive_pickle(client_socket):
    try:
        msg = client_socket.recv(1024)
        msg = pickle.loads(msg)

        client_socket.send(pickle.dumps("!CONFIRMED"))
        if msg == "!DISCONNECT":
            """napishi che nqma vryzka i izlezni ot programata"""
            return False
            
        return msg
    except Exception as e:
        print("Client is down or something..")
        print(e)
        return False

def height_pygame(y, height):
    new_height = height - y
    return new_height

def run(client_socket):
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
    draw_table(invisible_layer)
    draw_holes(invisible_layer)
    make_invisible_balls(invisible_layer)
    screen.blit(invisible_layer, [0,0])
    
    white_ball = Visible_ball("Pictures/White_ball.png")
    white_ball.place(screen, visible_ball_positions[0][0], visible_ball_positions[0][1])
    pygame.draw.line(screen, (255,255,255), (invisible_ball_positions[0][0],invisible_ball_positions[0][1]), get_pos())

    ball1 = Visible_ball("Pictures/Ball_1.png")
    ball1.place(screen, visible_ball_positions[1][0], visible_ball_positions[1][1])

    ball11 = Visible_ball("Pictures/Ball_11.png")
    ball11.place(screen, visible_ball_positions[2][0], visible_ball_positions[2][1])

    ball3 = Visible_ball("Pictures/Ball_3.png")
    ball3.place(screen, visible_ball_positions[3][0], visible_ball_positions[3][1])

    ball6 = Visible_ball("Pictures/Ball_6.png")
    ball6.place(screen, visible_ball_positions[4][0], visible_ball_positions[4][1])

    ball8 = Visible_ball("Pictures/Ball_8.png")
    ball8.place(screen, visible_ball_positions[5][0], visible_ball_positions[5][1])

    ball14 = Visible_ball("Pictures/Ball_14.png")
    ball14.place(screen, visible_ball_positions[6][0], visible_ball_positions[6][1])

    ball13 = Visible_ball("Pictures/Ball_13.png")
    ball13.place(screen, visible_ball_positions[7][0], visible_ball_positions[7][1])

    ball15 = Visible_ball("Pictures/Ball_15.png")
    ball15.place(screen, visible_ball_positions[8][0], visible_ball_positions[8][1])

    ball4 = Visible_ball("Pictures/Ball_4.png")
    ball4.place(screen, visible_ball_positions[9][0], visible_ball_positions[9][1])

    ball9 = Visible_ball("Pictures/Ball_9.png")
    ball9.place(screen, visible_ball_positions[10][0], visible_ball_positions[10][1])

    ball7 = Visible_ball("Pictures/Ball_7.png")
    ball7.place(screen, visible_ball_positions[11][0], visible_ball_positions[11][1])

    ball2 = Visible_ball("Pictures/Ball_2.png")
    ball2.place(screen, visible_ball_positions[12][0], visible_ball_positions[12][1])

    ball10 = Visible_ball("Pictures/Ball_10.png")
    ball10.place(screen, visible_ball_positions[13][0], visible_ball_positions[13][1])

    ball5 = Visible_ball("Pictures/Ball_5.png")
    ball5.place(screen, visible_ball_positions[14][0], visible_ball_positions[14][1])

    ball12 = Visible_ball("Pictures/Ball_12.png")
    ball12.place(screen, visible_ball_positions[15][0], visible_ball_positions[15][1])

    screen.blit(visible_layer, [0,0])
    bals = [white_ball,ball1,ball2,ball3,ball4,ball5,ball6,ball7,ball8,ball9,ball10,ball11,ball12,ball13,ball14,ball15]

    running = True
    is_mouse_clicked = 0
    while running:
        for event in pygame.event.get():
            x1,y1 = get_pos()
            #print(get_pos())
            if event.type == pygame.QUIT:
                client_socket.close()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x2,y2 = get_pos()
                is_mouse_clicked = 1
            if event.type == pygame.MOUSEBUTTONUP:
                if is_mouse_clicked == 1:
                    distans = find_distance(x1,y1,x2,y2)
                    y2 = height_pygame(y2, round((1000*height_pic)/width_pic ))
                    move_ball(invisible_ball_positions[0][0],invisible_ball_positions[0][1],x2,y2, distans, visible_layer, screen, background_image, bals)
                is_mouse_clicked = 0
        
        if is_mouse_clicked == 0:
            update_picure(screen, visible_layer, background_image, bals)
            pygame.draw.line(screen, (255,255,255), (invisible_ball_positions[0][0],invisible_ball_positions[0][1]), get_pos())
        pygame.display.flip()
        clock.tick(60)






