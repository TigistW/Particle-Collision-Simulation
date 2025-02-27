import pygame
import numpy as np
import random
import math

WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 20
FPS = 60

collision_type = "elastic"
class Particle:
    def __init__(self, x, y, vx, vy, radius, mass, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass
        self.color = color

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def check_collision(p1, p2):
    distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return distance <= p1.radius + p2.radius

def resolve_collision(p1, p2, collision_type):
    dx, dy = p2.x - p1.x, p2.y - p1.y
    distance = math.sqrt(dx**2 + dy**2)
    
    if distance == 0:
        return

    nx, ny = dx / distance, dy / distance
    tx, ty = -ny, nx

    v1n = nx * p1.vx + ny * p1.vy
    v1t = tx * p1.vx + ty * p1.vy
    v2n = nx * p2.vx + ny * p2.vy
    v2t = tx * p2.vx + ty * p2.vy

    if collision_type == "elastic":
        v1n_new = (v1n * (p1.mass - p2.mass) + 2 * p2.mass * v2n) / (p1.mass + p2.mass)
        v2n_new = (v2n * (p2.mass - p1.mass) + 2 * p1.mass * v1n) / (p1.mass + p2.mass)
    else:  # Inelastic
        v1n_new = v2n_new = (v1n * p1.mass + v2n * p2.mass) / (p1.mass + p2.mass)
    p1.vx = v1n_new * nx + v1t * tx
    p1.vy = v1n_new * ny + v1t * ty
    p2.vx = v2n_new * nx + v2t * tx
    p2.vy = v2n_new * ny + v2t * ty


particles = []
for _ in range(NUM_PARTICLES):
    particles.append(Particle(
        random.randint(50, WIDTH - 50),
        random.randint(50, HEIGHT - 50),
        random.uniform(-2, 2),
        random.uniform(-2, 2),
        random.randint(10, 20),
        random.uniform(1, 5),
        (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    ))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Collision Simulation")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

menu_rect = pygame.Rect(10, 10, 200, 60)
option_rects = {
    "elastic": pygame.Rect(10, 10, 200, 30)
}
menu_open = False

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(event.pos):
                menu_open = not menu_open
            elif menu_open:
                for option, rect in option_rects.items():
                    if rect.collidepoint(event.pos):
                        collision_type = option
                        menu_open = False

    pygame.draw.rect(screen, (255, 255, 255), menu_rect)
    menu_text = font.render(f"Collision: {collision_type}", True, (0, 0, 0))
    screen.blit(menu_text, (menu_rect.x + 5, menu_rect.y + 5))

    if menu_open:
        for option, rect in option_rects.items():
            pygame.draw.rect(screen, (200, 200, 200), rect)
            option_text = font.render(option.capitalize(), True, (0, 0, 0))
            screen.blit(option_text, (rect.x + 5, rect.y + 5))

    for particle in particles:
        particle.move()
        particle.draw(screen)

    # Check for collisions
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            if check_collision(particles[i], particles[j]):
                resolve_collision(particles[i], particles[j], collision_type)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
