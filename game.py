import pygame 
import numpy as np
from functions import * 

def vertices_2d(vertices_rotacionados):
    vertices = []
    matriz_projeção = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-D],[0,0,-1/D,0]])
    projetado = matriz_projeção @ vertices_rotacionados
    for ponto in projetado.T:
        vertices.append([ponto[0]/ponto[3],ponto[1]/ponto[3]])
    return vertices


TAMANHO_CUBO = 60
D = 100
THETA = 0

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

print(vertices_2d(vertices))

arestas = [
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

# Crie uma janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cubo 3D')

running = True


while running:

    # Desenhe um fundo preto
    screen.fill((0,0,0))

    matriz_rotacao_x = rotation_x(THETA)
    matriz_rotacao_y = rotation_y(THETA)
    matriz_rotacao_z = rotation_z(THETA)
    matriz_translacao = np.array([[1,0,0,400],[0,1,0,400],[0,0,1,0],[0,0,0,1]])
    matriz_rotacao_final = matriz_rotacao_x @ matriz_rotacao_y @ matriz_rotacao_z
    
    vertices_rotacionados = matriz_translacao @ vertices
    vertices_rotacionados = matriz_rotacao_final @ vertices_rotacionados
    vertices_rotacionados = np.linalg.inv(matriz_translacao) @ vertices_rotacionados
    #vertices = vertices_rotacionados

    transformed_vertices = vertices_2d(vertices_rotacionados)
        # Desenhe as arestas do cubo na tela
    for aresta in arestas:
        start = transformed_vertices[aresta[0]]
        end = transformed_vertices[aresta[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0] + position[0], start[1] + position[1]), (end[0] + position[0], end[1] + position[1]), 1)
    # Trate eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    THETA += 0.03
    pygame.display.update()

# Encerre o Pygame
pygame.quit()