import requests
import os
import time

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

def main():
    while True:
        clear_screen()
        random_entity = get_random_astronomy_data()

        if random_entity:
            print("Random Space Entity: {}".format(random_entity))

        time.sleep(2)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()
