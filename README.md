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

#### Passo a passo:

Para obter a matriz de projeção que realiza essa transformação, foi necessário realizar uma dedução similar à apresentada pelo professor na atividade de sala. No entanto, devido à natureza tridimensional da transformação, foi preciso fixar um dos eixos em cada uma das duas deduções realizadas para obter as funções correspondentes.

$$
\begin{bmatrix}
X_{pWp} \\
Z_p \\
W_p \\
\end{bmatrix}= 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & -d \\
0 & -\frac{1}{d} & 0 \\
\end{bmatrix}
\begin{bmatrix}
X_o \\
Z_o \\
1 \\
\end{bmatrix}
\hspace{1.5in}
\begin{bmatrix}
Y_{pWp} \\
Z_p \\
W_p \\
\end{bmatrix}= 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & -d \\
0 & -\frac{1}{d} & 0 \\
\end{bmatrix}
\begin{bmatrix}
Y_o \\
Z_o \\
1 \\
\end{bmatrix}
$$

As duas equações unidas resultam na equação abaixo:

#### Resultado:

$$
\begin{bmatrix}
X_{pWp} \\
Y_{pWp} \\
Z_p \\
W_p \\
\end{bmatrix}= 
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & -d \\
0 & 0 & -\frac{1}{d} & 0 \\
\end{bmatrix}
\begin{bmatrix}
X_o \\
Y_o \\
Z_o \\
1 \\
\end{bmatrix}
$$

Essa matriz devolve as cordenadas x, y e z da projeção, alem de uma cordenada auxilixar w que multiplica x e y. Por isso, há necessidade dividir os pontos x e y obtidos por esse quarto número, assim, conseguimos projetar os pontos 3D para um mundo 2D.

# Etapas do programa :

## Multiplicações matriciais :

No código, utilizamos das matrizes de multiplicação matrical apresentadas anteriormente para fazer as operações de rotação nos eixos e também de translação através das funções a seguir :

```
def rotation_x (tetha):

    tetha = np.radians(tetha)
    cos = np.cos(tetha)
    sin = np.sin(tetha)
    rotation_matrix = np.array([[1,0,0,0],[0,cos,sin,0], [0,-sin,cos,0],[0,0,0,1]])

    return rotation_matrix

def rotation_y (tetha):

    tetha = np.radians(tetha)
    cos = np.cos(tetha)
    sin = np.sin(tetha)
    rotation_matrix = np.array([[cos,0,-sin,0],[0,1,0,0], [sin,0,cos,0],[0,0,0,1]])
    return rotation_matrix

def rotation_z (tetha):

    tetha = np.radians(tetha)
    cos = np.cos(tetha)
    sin = np.sin(tetha)
    rotation_matrix = np.array([[cos,sin,0,0],[-sin,cos,0,0], [0,-0,1,0],[0,0,0,1]])

    return rotation_matrix

def move(x,y,z):
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

```

com elas podemos fazer a rotação em todos os eixos do cubo a uma angulação θ e posteriormente transladamos o cubo por meio da função move para longe da origem a fim de  possibilitar a vizualização dos vertices.


## Projeções :

Para realizar a projeção, utilizamos a matriz de projeção apresentada anteriormente e no código a implementação foi feita da seguinte forma :

```
def vertices_2d(vertices_rotacionados,d):
    vertices = []
    matriz_projeção = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,(-d)],[0,0,(-1/d),0]])
    projetado = matriz_projeção @ vertices_rotacionados
    for ponto in projetado.T:
        vertices.append([ponto[0]/ponto[3],ponto[1]/ponto[3]])
    return vertices
x = move(0+player[0,0],0+player[0,1],200+player[0,2]) @  rotation_x(tetha) @ rotation_z(tetha) @ rotation_y(tetha) @ vertices 

transformed_vertices = vertices_2d(x,fov)

```
* Realizamos todas as operações de rotação e translação ainda no mundo 3D (Reparem que na função move deixamos setado para somar 200 a posição z do cubo e além disso a posição do player que nos será útil futuramente para a movimentação no game).

* Utilizamos a função de projeção ``` vertices_2d ``` para fazer a projeção de todos vértices do cubo passando os vertices e o fov (distância focal) par a função.

## Desenhando pontos na tela : 

Após a projeção dos pontos para o munto 2D podemos desenhar os pontos na tela, e nesse momento utilizaremos aquela lista de arestas que criamos no ínicio do progrma :

### Trecho de código :

```
for aresta in arestas:
        start = transformed_vertices[aresta[0]]
        end = transformed_vertices[aresta[1]]
        pygame.draw.line(screen, (255, 255, 255), (start[0] + position[0], start[1] + position[1]), (end[0] + position[0], end[1] + position[1]), 1)

```

- Nessse trecho de código usamos as posições dos pontos juntamente das arestas para fazer a ligação entre cada um dos pontos com uma linha que quando completos formam o desenho do cubo.



## Movimentação :


Para realizar a movimentação, utilizamos o vetor do player definido previamente e somamos sua posição à matriz de translação do cubo, assim como foi citado anteriormente, para isso escolhemos o eixo que vamos somar ao capturar eventos de clique nas teclas WASD no pygame.


````

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

            if  player[0,2] > 0:
                player[0,2] -= speed

        elif move_status.get('back'):
            
            player[0,2] += speed
    
            
        if move_status.get('left'):
            
            player[0,0] -= speed

        elif move_status.get('rigth'):
            
            player[0,0] += speed

````

## Distância focal (Fov) :

Para realizar a mudança de distância focal, utilizamos a mesma matriz de projeção citada anteriormente, mas alterando o 'fov' passado. Dessa forma, modamos a distância focal do cubo capturando o evento de scroll no mouse. 

````
elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 4:  # scroll up

                if fov < 1000:
                    fov += 4
                    
            elif event.button == 5:  # scroll down

                if fov > 4:
                    fov -= 4

````
