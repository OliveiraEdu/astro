import random
import numpy as np
import os
import time

# Constants
WIDTH, HEIGHT = 80, 20
NUM_BOIDS = 10  # Increase the number of boids
BOID_SPEED = 2
NEIGHBOR_DISTANCE = 5

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

# Main loop
while True:  # Run infinitely
    os.system('clear')  # For Linux

    # Update boids
    for boid in flock:
        boid.update(flock)

    # Display boids in the terminal
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            for boid in flock:
                if int(boid.x) == x and int(boid.y) == y:
                    row += "o"
                    break
            else:
                row += " "
        print(row)

    # Wait for a short time to observe the movement
    time.sleep(0.1)
