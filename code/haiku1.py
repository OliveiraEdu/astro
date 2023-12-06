import random
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import os
import time
from termcolor import colored
from pyfiglet import Figlet

def clear_screen():
    os.system('clear')  # For Linux

def get_random_haiku():
    haiku_ids = [5732, 2049, 768, 53688, 2189]  # Example IDs; add more as needed
    random_haiku_id = random.choice(haiku_ids)
    haiku_text = strip_headers(load_etext(random_haiku_id)).strip()
    return haiku_text

def display_stylized_text(text):
    color = random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])
    font_style = random.choice(['block', 'colossal', 'banner', 'graffiti'])
    figlet = Figlet(font=font_style, justify='center')
    ascii_art = figlet.renderText(text)
    print(colored(ascii_art, color))

def main():
    while True:
        clear_screen()
        random_haiku = get_random_haiku()

        if random_haiku:
            display_stylized_text(random_haiku)

        time.sleep(5)

if __name__ == "__main__":
