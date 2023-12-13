import pygame
import sys
import math
import random

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
NUM_BOIDS = 50
BOID_SPEED = 2
NEIGHBOR_DISTANCE = 50
LEADER_COLOR = (255, 0, 0)  # Red

# Boid class
class Boid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self, flock):
        alignment_vector = self.alignment(flock)

        self.angle += alignment_vector

        # Normalize angle to stay within [0, 2*pi)
        self.angle %= 2 * math.pi

        # Move boid based on angle
        self.x += BOID_SPEED * math.cos(self.angle)
        self.y += BOID_SPEED * math.sin(self.angle)

        # Wrap around screen
        self.x %= WIDTH
        self.y %= HEIGHT

    def alignment(self, flock):
        alignment_vector = 0

        for other in flock:
            distance = math.hypot(self.x - other.x, self.y - other.y)

            if 0 < distance < NEIGHBOR_DISTANCE:
                alignment_vector += other.angle

        return alignment_vector / max(1, len(flock))  # Ensure not dividing by zero

# Create a flock of boids
flock = [Boid() for _ in range(NUM_BOIDS)]

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boids Simulation')
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update boids
    for boid in flock:
        boid.update(flock)

    # Find the leader boid (highest y-coordinate)
    leader = max(flock, key=lambda b: b.y)

    # Draw boids on the screen
    screen.fill((0, 0, 0))  # Black background

    for boid in flock:
        color = LEADER_COLOR if boid is leader else (255, 255, 255)  # White color for followers
        pygame.draw.circle(screen, color, (int(boid.x), int(boid.y)), 5)

    pygame.display.flip()
    clock.tick(60)  # Adjust the frame rate as needed
