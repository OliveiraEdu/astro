def generate_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        triangles = '*' * (2 * i - 1)
        print(f"{spaces}{triangles}")

def main():
    pyramid_height = 5  # You can adjust the height of the pyramid

    generate_pyramid(pyramid_height)

if __name__ == "__main__":
    main()
