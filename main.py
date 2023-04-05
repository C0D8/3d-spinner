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


# Definindo a posição do player
player = np.array([[0], [0], [1], [1]]).T

#Status de movimentação para o player
move_status = {"left" : False, "rigth" : False, "front" : False, "back" : False}


#Velocidade do jogador
speed = 5

#Definindo fov
fov = 300

# Crie uma janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cubo 3D')

tetha = 0
running = True

# Defina a posição e tamanho do retângulo do gradiente

while running:

    # Desenhe um fundo preto
    screen.fill((0, 0, 0))

    # Transforme cada vértice do cubo usando a matriz de rotação e translação 
    x = move(0+player[0,0],0+player[0,1],200+player[0,2]) @  rotation_x(tetha) @ rotation_z(tetha) @ rotation_y(tetha) @ vertices 

    # Adiciona o vértice transformado na lista
    transformed_vertices = vertices_2d(x,fov)

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

        elif event.type == pygame.KEYUP:
           
            if event.key == pygame.K_w:
                move_status['front'] = False
            if event.key == pygame.K_s:
                move_status['back'] = False
            if event.key == pygame.K_d:
                move_status['rigth'] = False
            if event.key == pygame.K_a:
                move_status['left'] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 4:  # scroll up

                if fov < 1000:
                    fov += 4

            elif event.button == 5:  # scroll down

                if fov > 4:
                    fov -= 4


        if move_status.get('front'):

            if  player[0,2] > 0:
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




