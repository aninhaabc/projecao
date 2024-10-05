import pygame
import numpy as np
from transformations import rotation_matrix_x, rotation_matrix_y, rotation_matrix_z, project

WIDTH, HEIGHT = 800, 600
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
FOV = 400 
pyramid_size = 100  

# Inicializar o Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube Projection")
clock = pygame.time.Clock()

# Vértices de uma pirâmide
vertices = np.array([[-1, -1, -1], [-1, -1, 1], [1, -1, 1], [1, -1, -1], [0, 1, 0]]) * pyramid_size

# Arestas que conectam os vértices
edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # Base quadrada
        (0, 4), (1, 4), (2, 4), (3, 4)]  # Faces conectando à ponta da pirâmide

def main():
    theta_x = 0
    theta_y = 0
    theta_z = 0
    translation = np.array([0, 0, 0])  # Vetor de translação
    running = True

    while running:
        screen.fill(BLACK)

        # Controle de rotação pelo teclado
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            theta_y -= 0.05  # Rotacionar no eixo Y
        if keys[pygame.K_RIGHT]:
            theta_y += 0.05  # Rotacionar no eixo Y
        if keys[pygame.K_UP]:
            theta_x -= 0.05  # Rotacionar no eixo X
        if keys[pygame.K_DOWN]:
            theta_x += 0.05  # Rotacionar no eixo X
        if keys[pygame.K_z]:
            theta_z -= 0.05  # Rotacionar no eixo Z
        if keys[pygame.K_x]:
            theta_z += 0.05  # Rotacionar no eixo Z

        # Controle de translação pelo teclado
        if keys[pygame.K_w]:
            translation[1] -= 5  # Mover para cima no espaço 3D
        if keys[pygame.K_s]:
            translation[1] += 5  # Mover para baixo no espaço 3D
        if keys[pygame.K_a]:
            translation[0] -= 5  # Mover para a esquerda
        if keys[pygame.K_d]:
            translation[0] += 5  # Mover para a direita

        # Calcular as matrizes de rotação
        rotation_x = rotation_matrix_x(theta_x)
        rotation_y = rotation_matrix_y(theta_y)
        rotation_z = rotation_matrix_z(theta_z)

        # Aplicar rotação, translação e projetar vértices
        transformed_vertices = []
        for vertex in vertices:
            rotated = np.dot(rotation_x, vertex)
            rotated = np.dot(rotation_y, rotated)
            rotated = np.dot(rotation_z, rotated)
            # Aplicar translação
            translated = rotated + translation
            projected = project(translated, FOV, WIDTH, HEIGHT)
            transformed_vertices.append(projected)

        # Desenhar as arestas
        for edge in edges:
            start, end = edge
            pygame.draw.line(screen, WHITE, transformed_vertices[start], transformed_vertices[end], 2)

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
