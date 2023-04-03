import pygame 
import numpy as np
from functions import * 

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

)  * 60

vertices = vertices.T
vertices = np.vstack((vertices, np.ones((1, vertices.shape[1]))))
vertices = vertices.T

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
player = np.array([[0], [0], [1], [1]])
move_status = {"left" : False, "rigth" : False, "front" : False, "back" : False}
speed = 10

zoom_in = np.array([
    [1.05, 0, 0, 0],
    [0, 1.05, 0, 0],
    [0, 0, 1.05, 0],
    [0, 0, 0, 1]
])


zoom_out = np.array([
    [0.95, 0, 0, 0],
    [0, 0.95, 0, 0],
    [0, 0, 0.95, 0],
    [0, 0, 0, 1]
])


# Crie uma janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cubo 3D')

tetha = 0
running = True
while running:

    # Desenhe um fundo preto
    screen.fill((0, 0, 0))

    # Transforme cada vértice do cubo usando a matriz de rotação
    transformed_vertices = []

    for vertex in vertices:



        x = rotation_x(tetha) @ rotation_z(tetha) @ rotation_x(tetha) @ vertex 
        # Normaliza as coordenadas do vértice dividindo pela coordenada W
        x /= x[3]

        x[:3] = np.add(x[:3], player[:3, 0])
        # Adiciona o vértice transformado na lista
        transformed_vertices.append(x[:3])
        
    # Desenhe as arestas do cubo na tela
    for edge in edges:

        start = transformed_vertices[edge[0]]
        end = transformed_vertices[edge[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0] + position[0], start[1] + position[1]), (end[0] + position[0], end[1] + position[1]), 2)

    # Atualize a tela
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

        if move_status.get('front'):
            vertices = vertices @ zoom_in
        elif move_status.get('back'):
            vertices = vertices @ zoom_out
        if move_status.get('left'):
            player = move(-speed,0,0) @ player
        elif move_status.get('rigth'):
            player = move(speed,0,0) @ player


    # Atualize a rotação do cubo
    tetha += 0.05

# Encerre o Pygame
pygame.quit()




