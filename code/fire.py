import os
import time
import random

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def generate_fire_frame(width, height):
    frame = [[' ' for _ in range(width)] for _ in range(height)]

    # Set the bottom row to represent the fire base
    for i in range(width):
        frame[height - 1][i] = '*'

    # Generate the fire effect
    for row in range(height - 2, 0, -1):
        for col in range(1, width - 1):
            rand_offset = random.randint(0, 2)
            avg_intensity = (frame[row + 1][col - 1] + frame[row + 1][col] + frame[row + 1][col + 1]) // 3
            frame[row][col] = max(0, avg_intensity - rand_offset)

    return frame

def display_fire_animation(width, height, duration_sec):
    frames = []
    for _ in range(int(duration_sec // 0.1)):
        clear_screen()
        frame = generate_fire_frame(width, height)
        frames.append(frame)
        for row in frame:
            print(''.join(map(lambda intensity: ' .:ioVM@'[min(intensity, 4)], row)))
        time.sleep(0.1)

    return frames

def main():
    try:
        width, height = os.get_terminal_size()
    except:
        width, height = 80, 24  # Default size if terminal size cannot be determined

    clear_screen()
    print("Generating a mesmerizing fire animation. Press Ctrl+C to exit.")
    
    try:
        frames = display_fire_animation(width, height, duration_sec=60)
    except KeyboardInterrupt:
        clear_screen()
        print("Animation interrupted. Bye!")

if __name__ == "__main__":
    main()
