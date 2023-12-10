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
SEPARATION_DISTANCE = 30
ALIGNMENT_DISTANCE = 50
COHESION_DISTANCE = 50
SEPARATION_WEIGHT = 1.0
ALIGNMENT_WEIGHT = 0.8
COHESION_WEIGHT = 0.6

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
        separation_vector = self.separation(flock)
        alignment_vector = self.alignment(flock)
        cohesion_vector = self.cohesion(flock)

        self.angle += separation_vector + alignment_vector + cohesion_vector

        # Move boid based on angle (with wrapping around screen)
        self.x += BOID_SPEED * np.cos(self.angle)
        self.y += BOID_SPEED * np.sin(self.angle)

        # Wrap around screen
        self.x %= WIDTH
        self.y %= HEIGHT

    def separation(self, flock):
        separation_vector = 0

        for other in flock:
            distance = np.hypot(self.x - other.x, self.y - other.y)

            if 0 < distance < SEPARATION_DISTANCE:
                angle_diff = np.arctan2(self.y - other.y, self.x - other.x)
                separation_vector += np.pi - np.abs(np.abs(self.angle - angle_diff) - np.pi)

        return SEPARATION_WEIGHT * separation_vector

    def alignment(self, flock):
        alignment_vector = 0

        for other in flock:
            distance = np.hypot(self.x - other.x, self.y - other.y)

            if 0 < distance < ALIGNMENT_DISTANCE:
                alignment_vector += other.angle

        return ALIGNMENT_WEIGHT * (alignment_vector / len(flock))

    def cohesion(self, flock):
        cohesion_vector = 0

        for other in flock:
            distance = np.hypot(self.x - other.x, self.y - other.y)

            if 0 < distance < COHESION_DISTANCE:
                cohesion_vector += other.angle

        return COHESION_WEIGHT * (cohesion_vector / len(flock))

# Create a flock of boids
flock = [Boid() for _ in range(NUM_BOIDS)]

# Set up the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update boids
    for i, boid in enumerate(flock):
        boid.update(flock)
        print(f"Updating boid {i + 1}/{NUM_BOIDS}", end='\r')  # Print progress on the same line

    # Draw boids
    screen.fill(BLACK)
    for boid in flock:
        pygame.draw.circle(screen, WHITE, (int(boid.x), int(boid.y)), BOID_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

print("\nSimulation complete!")
pygame.quit()
