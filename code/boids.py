import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_BOIDS = 50
BOID_RADIUS = 5
BOID_SPEED = 2
NEIGHBOR_DISTANCE = 50
NUM_ITERATIONS = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Boid class
class Boid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.angle = random.uniform(0, 2 * np.pi)

    def update(self, flock):
        alignment_vector = self.alignment(flock)

        self.angle += alignment_vector

        # Normalize angle to stay within [0, 2*pi)
        self.angle %= 2 * np.pi

        # Move boid based on angle (with wrapping around screen)
        self.x += BOID_SPEED * np.cos(self.angle)
        self.y += BOID_SPEED * np.sin(self.angle)

        # Wrap around screen
        self.x %= WIDTH
        self.y %= HEIGHT

    def alignment(self, flock):
        alignment_vector = 0

        for other in flock:
            distance = np.hypot(self.x - other.x, self.y - other.y)

            if 0 < distance < NEIGHBOR_DISTANCE:
                alignment_vector += other.angle

        return alignment_vector / len(flock)

# Create a flock of boids
flock = [Boid() for _ in range(NUM_BOIDS)]

# Set up the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Boids Simulation")
clock = pygame.time.Clock()

# Main loop
running = True
iteration = 0

while running and iteration < NUM_ITERATIONS:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update boids
    for boid in flock:
        boid.update(flock)

    # Draw boids
    screen.fill(BLACK)
    for boid in flock:
        pygame.draw.circle(screen, WHITE, (int(boid.x), int(boid.y)), BOID_RADIUS)

    # Display status
    status_text = f"Iteration: {iteration}/{NUM_ITERATIONS}"
    font = pygame.font.Font(None, 36)
    status_surface = font.render(status_text, True, WHITE)
    screen.blit(status_surface, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

    iteration += 1

pygame.quit()
