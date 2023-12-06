import random
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

def get_random_haiku():
    # IDs for haikus or poems in the Project Gutenberg collection
    haiku_ids = [5732, 2049, 768, 53688, 2189]  # Example IDs; add more as needed

    # Choose a random haiku ID
    random_haiku_id = random.choice(haiku_ids)

    # Fetch and clean the text
    haiku_text = strip_headers(load_etext(random_haiku_id)).strip()

    return haiku_text

# Rest of the code remains unchanged

def main():
    while True:
        clear_screen()
        random_haiku = get_random_haiku()

        if random_haiku:
            display_stylized_text(random_haiku)

        time.sleep(5)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()
