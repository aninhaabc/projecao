import math
import numpy as np

# Função para aplicar rotação em um eixo
def rotation_matrix_x(theta):
    return np.array([[1, 0, 0], [0, math.cos(theta), -math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])

def rotation_matrix_y(theta):
    return np.array([[math.cos(theta), 0, math.sin(theta)], [0, 1, 0], [-math.sin(theta), 0, math.cos(theta)]])

def rotation_matrix_z(theta):
    return np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])

# Função de projeção 3D em 2D
def project(point, fov, width, height):
    x, y, z = point
    factor = fov / (fov + z)
    x_proj = x * factor + width // 2
    y_proj = y * factor + height // 2
    return (int(x_proj), int(y_proj))