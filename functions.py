import numpy as np 

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


def projection(points, distance):

    # points =  np.vstack ( (points, np.ones( points.shape[1]) ) )

    t_matrix = np.array([[0,0,0,1],[0,0,1,0],[0,-1/distance,0,0],[-distance,0,0,0]])
    transformed_points = t_matrix @ points
    transformed_points[0,0] = transformed_points[0,0]/transformed_points[3,0]
    transformed_points[1,0] = transformed_points[1,0]/transformed_points[3,0]
    result = []
    result.append(transformed_points[0,0])
    result.append(transformed_points[1,0])
    result.append(transformed_points[2,0])
    result.append(1)

    return result

def move(x,y,z):
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])





