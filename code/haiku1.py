import requests
import random
import os
import time
from termcolor import colored

def clear_screen():
    os.system('clear')  # For Linux

def get_random_haiku():
    api_url = "https://haiku.kimonolabs.com/"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        random_haiku = random.choice(data['haikus'])
        return random_haiku
    else:
        print(f"Failed to fetch haiku. Status code: {response.status_code}")
        return None

def display_stylized_text(text):
    # Randomly choose a color for the text
    color = random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])
    
    # Randomly choose a font style
    font_style = random.choice(['block', 'colossal', 'banner', 'graffiti'])

    # Print colored and stylized text
    print(colored(text, color))

def main():
    while True:
        clear_screen()
        random_haiku = get_random_haiku()

        if random_haiku:
            display_stylized_text(random_haiku)

        time.sleep(5)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()
