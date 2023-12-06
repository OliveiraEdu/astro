import requests
import random
import os
import time
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

def display_ascii_art(entity_name):
    figlet = Figlet(width=random.randint(80, 120),  # Random width for font
                   font=random.choice(['standard', 'block', 'colossal', 'slant', 'big', 'script']),
                   justify='center')
    ascii_art = figlet.renderText(entity_name)
    
    # Randomize the location within the terminal
    rows, columns = os.popen('stty size', 'r').read().split()
    rows, columns = int(rows), int(columns)
    
    row_position = random.randint(1, rows-10)  # Ensure some margin at the bottom
    column_position = random.randint(1, columns-len(ascii_art.split('\n')[0]))

    print('\033[{};{}H{}'.format(row_position, column_position, ascii_art))  # Move cursor to specified position

def main():
    while True:
        clear_screen()
        random_entity = get_random_astronomy_data()

        if random_entity:
            display_ascii_art(random_entity)

        time.sleep(2)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()
