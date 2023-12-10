import colorama
import os
import math
import time

colorama.init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def koch_snowflake(iterations, length):
    if iterations == 0:
        return [(0, 0), (length, 0)]

    angle = math.pi / 3  # 60 degrees
    segment_length = length / 3

    points = []
    points.extend(koch_snowflake(iterations - 1, segment_length))
    
    x, y = points[-1]
    x += segment_length * math.cos(angle)
    y += segment_length * math.sin(angle)
    points.append((x, y))

    points.extend(koch_snowflake(iterations - 1, segment_length))
    
    x, y = points[-1]
    x += segment_length * math.cos(-angle)
    y += segment_length * math.sin(-angle)
    points.append((x, y))

    points.extend(koch_snowflake(iterations - 1, segment_length))

    return points

def display_koch_snowflake(points):
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

        iterations = random.randint(2, 5)
        length = min(width, height) - 1
        points = koch_snowflake(iterations, length)
        display_koch_snowflake(points)

        time.sleep(2)

if __name__ == "__main__":
    main()
