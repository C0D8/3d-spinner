import pygame 
import numpy as np
from functions import * 


TAMANHO_CUBO = 60

vertices = np.array([
     [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
]

)  * TAMANHO_CUBO


vertices = vertices.T
vertices = np.vstack((vertices, np.ones((1, vertices.shape[1]))))

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

pygame.init()

# Defina as dimensões da janela
width = 800
height = 800

position = [width // 2, height // 2]

player = np.array([[0], [0], [1], [1]]).T

player_cam = np.array([[0], [0], [1], [1]])

move_status = {"left" : False, "rigth" : False, "front" : False, "back" : False}
move_direction = {"left" : False, "rigth" : False, "front" : False, "back" : False}
speed = 10

# zoom_in = np.array([
#     [1.05, 0, 0, 0],
#     [0, 1.05, 0, 0],
#     [0, 0, 1.05, 0],
#     [0, 0, 0, 1]
# ])


# zoom_out = np.array([
#     [0.95, 0, 0, 0],
#     [0, 0.95, 0, 0],
#     [0, 0, 0.95, 0],
#     [0, 0, 0, 1]
# ])


# Crie uma janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cubo 3D')

tetha = 0
running = True


color1 = (0, 255, 0)
color2 = (0, 128, 0)

# Defina a posição e tamanho do retângulo do gradiente

while running:

    # Desenhe um fundo preto
    screen.fill((135, 206, 235))

    # Transforme cada vértice do cubo usando a matriz de rotação




    x = move(0+player[0,0],0+player[0,1],200+player[0,2]) @  rotation_x(tetha) @ rotation_z(tetha) @ rotation_y(tetha) @ vertices 
    # Normaliza as coordenadas do vértice dividindo pela coordenada W
    # x /= x[3]


    # x = x * player[2]

    # Adiciona o vértice transformado na lista
    transformed_vertices = vertices_2d(x,100)


        
    
    
    # Atualize a tela

    rect = pygame.Rect(0, height/2, width, height/2)

    # Desenhe o gradiente na tela
    for y in range(rect.top, rect.bottom):
        # Calcule o fator de interpolação entre as cores
        t = (y - rect.top) / rect.height
        # Misture as duas cores usando o fator de interpolação
        color = tuple(int(c1 * (1-t) + c2 * t) for c1, c2 in zip(color1, color2))
        # Desenhe a linha horizontal com a cor interpolada
        pygame.draw.line(screen, color, (rect.left, y), (rect.right, y))

    # Desenhe as arestas do cubo na tela
    for edge in edges:

        start = transformed_vertices[edge[0]]
        end = transformed_vertices[edge[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0] + position[0], start[1] + position[1]), (end[0] + position[0], end[1] + position[1]), 2)

    

    pygame.display.update()

    # Trate eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_w:
                move_status['front'] = True
            if event.key == pygame.K_s:
                move_status['back'] = True
            if event.key == pygame.K_d:
                move_status['rigth'] = True
            if event.key == pygame.K_a:
                move_status['left'] = True

            if event.key == pygame.K_UP:
                move_direction['front'] = True
            if event.key == pygame.K_DOWN:
                move_direction['back'] = True
            if event.key == pygame.K_RIGHT:
                move_direction['rigth'] = True
            if event.key == pygame.K_LEFT:
                move_direction['left'] = True


        elif event.type == pygame.KEYUP:
           
            if event.key == pygame.K_w:
                move_status['front'] = False
            if event.key == pygame.K_s:
                move_status['back'] = False
            if event.key == pygame.K_d:
                move_status['rigth'] = False
            if event.key == pygame.K_a:
                move_status['left'] = False

            if event.key == pygame.K_UP:
                move_direction['front'] = False
            if event.key == pygame.K_DOWN:
                move_direction['back'] = False
            if event.key == pygame.K_RIGHT:
                move_direction['rigth'] = False
            if event.key == pygame.K_LEFT:
                move_direction['left'] = False



        if move_status.get('front'):
            
            player[0,2] -= speed

        elif move_status.get('back'):

            
            player[0,2] += speed
    
            
        if move_status.get('left'):
            
            player[0,0] -= speed


        elif move_status.get('rigth'):
            
            player[0,0] += speed




    # Atualize a rotação do cubo
    tetha += 0.05

# Encerre o Pygame
pygame.quit()




