# 3d-spinner

## Como rodar o programa :

Primeiramente é necessário realizar a clonagem do repositório por meio do comando: git clone https://github.com/C0D8/3d-spinner.git. Assim como também instalar as bibliotecas necessárias e por fim executar o arquivo "main.py".

### Bibliotecas necessárias :
 * Numpy 
 * Pygame
- Obs.: Para realizar a instalação de maneira automatizada basta rodar o comando pip install -r requiriments.txt na raiz do projeto. 

### Execução:

- Para executar, basta rodar o arquivo "main.py" por meio do comando: python main.py

## Considerações iniciais :

### Matriz do cubo :

Para realizar todas as operações criamos os pontos dos vértices do cubo em uma matriz em que cada ponto representa um dos 8 vértices do cubo e para fazer a ligação desses pontos utilizamos uma  lista com vetores que representam a ligação de cada um dos vérties. Essa lista vai nos ajudar posteriormente para fazer o desenho do cubo na tela.


```
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


```





## Operações de rotação :

Para realizar a rotação do cubo ainda no espaço 3d utilizamos algumas matrizes de rotacão que serão apresentadas abaixo.

### Rotações nas direções dos eixos :

Em 3D, é possível rotacionar pontos ao redor de cada um dos eixos usando as matrizes:

- Para rotacionar no eixo x :
$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$


- Para rotacionar no eixo y :
$$

R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- Para rotacionar no eixo z :
$$
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Essas matrizes já contém a nossa (necessária) dimensão adicional que permitirá, depois, controlar as translações e projeções.

## Operação de translação : 

Para realizar a translação do cubo utilizaremos da dimenção adicional citada anteriomente :

### Matriz de translação :


$$
R_z = \begin{bmatrix}
1& 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Dessa forma, é possível definir a translação desejada em cada um dos eixos x, y e z.




## Projeção do cubo 3D em 2D : 

Como foi dito anterimente, após realizarmos todas as transformações ainda no mundo 3D, chega o momento de fazer a projeção dos pontos para o mundo 2D e para isso usamos a seguinte matriz :

### Matriz de projeção 


$$
R_z = \begin{bmatrix}
1& 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & -d \\
0 & 0 & -1/d & 0
\end{bmatrix}
$$



Essa matriz devolve as cordenadas x, y e z da projeção, alem de uma cordenada auxilixar w que multiplica x e y. Por isso, há necessidade dividir os pontos x e y obtidos por esse quarto número, assim, conseguimos projetar os pontos 3D para um mundo 2D.



## Desenhando pontos na tela : 


Após a projeção dos pontos para o munto 2D podemos desenhar os pontos na tela, e nesse momento utilizaremos aquela lista de arestas que criamos no ínicio do progrma :

### Trecho de código :

```
for aresta in arestas:
        start = transformed_vertices[aresta[0]]
        end = transformed_vertices[aresta[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0] + position[0], start[1] + position[1]), (end[0] + position[0], end[1] + position[1]), 1)

```

- Nessse trecho de código usamos as posições dos pontos juntamente das arestas para fazer a ligação entre cada um dos pontos com uma linha.















