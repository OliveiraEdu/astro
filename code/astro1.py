import requests
import random
import os
import time
from termcolor import colored
from pyfiglet import Figlet

def clear_screen():
    os.system('clear')  # For Linux

def get_random_astronomy_data():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        random_entity = random.choice(data['bodies'])
        return random_entity['englishName']
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def display_stylized_text(entity_name):
    # Randomly choose a color for the text
    color = random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])
    
    # Randomly choose a font style
    font_style = random.choice(['block', 'colossal', 'banner', 'graffiti'])

    # Create a Figlet instance with the chosen font style
    figlet = Figlet(font=font_style, justify='center')
    
    # Render the ASCII art
    ascii_art = figlet.renderText(entity_name)

    # Print colored and stylized text
    print(colored(ascii_art, color))

def main():
    while True:
        clear_screen()
        random_entity = get_random_astronomy_data()

        if random_entity:
            display_stylized_text(random_entity)

        time.sleep(2)

if __name__ == "__main__":
    main()
