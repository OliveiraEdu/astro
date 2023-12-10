import colorama
import math
import random
import os
import time

colorama.init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return 0
    return n

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    pixels = [[' ' for _ in range(width)] for _ in range(height)]
    for row in range(height):
        for col in range(width):
            x = x_min + (x_max - x_min) * col / (width - 1)
            y = y_min + (y_max - y_min) * row / (height - 1)
            c = complex(x, y)
            val = mandelbrot(c, max_iter)
            pixels[row][col] = val
    return pixels

def display_mandelbrot(pixels):
    for row in pixels:
        for val in row:
            if val == 0:
                print(colorama.Back.BLACK + ' ', end='')
            else:
                color = random.choice([colorama.Back.RED, colorama.Back.GREEN, colorama.Back.YELLOW, colorama.Back.BLUE])
                print(color + ' ', end='')
        print()

def main():
    try:
        width, height = os.get_terminal_size()
    except:
        width, height = 80, 24  # Default size if terminal size cannot be determined

    while True:
        clear_screen()

        # Adjust parameters dynamically
        x_min = random.uniform(-2, -1)
        x_max = random.uniform(0, 1)
        y_min = random.uniform(-1, 0)
        y_max = random.uniform(1, 2)
        max_iter = random.randint(30, 70)

        pixels = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
        display_mandelbrot(pixels)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
