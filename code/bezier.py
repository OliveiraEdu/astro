import colorama
import os
import random
import time

colorama.init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def bezier_curve(t, control_points):
    n = len(control_points) - 1
    x = sum(binomial_coefficient(n, i) * (1 - t) ** (n - i) * t ** i * control_points[i][0] for i in range(n + 1))
    y = sum(binomial_coefficient(n, i) * (1 - t) ** (n - i) * t ** i * control_points[i][1] for i in range(n + 1))
    return int(x), int(y)

def generate_bezier_curve(width, height, control_points):
    points = []
    for t in range(0, 101):
        t /= 100.0
        x, y = bezier_curve(t, control_points)
        if 0 <= x < width and 0 <= y < height:
            points.append((x, y))
    return points

def display_bezier_curve(points):
    for row in range(height):
        for col in range(width):
            if (col, row) in points:
                print(colorama.Back.RED + ' ', end='')
            else:
                print(colorama.Back.BLACK + ' ', end='')
        print()

def main():
    try:
        width, height = os.get_terminal_size()
    except:
        width, height = 80, 24  # Default size if terminal size cannot be determined

    while True:
        clear_screen()

        # Generate random control points for the Bezier curve
        control_points = [(random.randint(0, width), random.randint(0, height)) for _ in range(4)]

        # Generate and display the Bezier curve
        points = generate_bezier_curve(width, height, control_points)
        display_bezier_curve(points)

        time.sleep(0.5)

if __name__ == "__main__":
    main()
