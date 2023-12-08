import pygame
import sys

def draw_sierpinski_triangle(surface, order, size, x, y):
    if order == 0:
        # Draw a filled triangle
        pygame.draw.polygon(surface, (255, 255, 255), [(x, y), (x + size, y), (x + size / 2, y - size * 0.866)])
    else:
        # Recursively draw three smaller triangles
        draw_sierpinski_triangle(surface, order - 1, size / 2, x, y)
        draw_sierpinski_triangle(surface, order - 1, size / 2, x + size / 2, y)
        draw_sierpinski_triangle(surface, order - 1, size / 2, x + size / 4, y - size * 0.866 / 2)

def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sierpinski Triangle")

    order = 3  # Adjust the order of the Sierpinski Triangle

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        draw_sierpinski_triangle(screen, order, 400, 200, 600)

        pygame.display.flip()
        pygame.time.delay(1000)  # Delay to observe the result

if __name__ == "__main__":
    main()
