import pygame 
import numpy as np
from functions import * 

def vertices_2d(vertices_rotacionados):
    vertices = []
    matriz_projeção = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-D],[0,0,-1/D,0]])
    projetado = matriz_projeção @ vertices_rotacionados
    for ponto in projetado.T:
        vertices.append([ponto[1]/ponto[3],ponto[0]/ponto[3]])
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
rodar = True
contador = 0
while rodar == True:
    contador += 1

    matriz_rotacao_x = rotation_x(THETA)
    matriz_rotacao_y = rotation_y(THETA)
    matriz_rotacao_z = rotation_z(THETA)

    matriz_rotacao_final = matriz_rotacao_x @ matriz_rotacao_y @ matriz_rotacao_z

    vertices_rotacionados = matriz_rotacao_final @ vertices

    vertices_duasdimensoes = vertices_2d(vertices_rotacionados)

    if contador ==2:
        rodar = False
    THETA += 0.03
    

    

print(vertices_2d(vertices))   



