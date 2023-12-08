import os
import time
import numpy as np

def clear_screen():
    os.system('clear')  # For Linux

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def display_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    for row in range(height):
        for col in range(width):
            x = np.interp(col, [0, width], [x_min, x_max])
            y = np.interp(row, [0, height], [y_min, y_max])
            c = complex(x, y)

            color = mandelbrot(c, max_iter)
            # Adjust the character based on the color intensity
            char = ' ' if color == max_iter else '@'

            print(char, end='')
        print()

def main():
    width = 80
    height = 24
    x_min, x_max = -2, 1
    y_min, y_max = -1, 1
    initial_max_iter = 50

    for i in range(1, 20):  # Update max_iter for 20 iterations
        max_iter = initial_max_iter + i * 10
        clear_screen()
        display_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
        time.sleep(1)

if __name__ == "__main__":
    main()
