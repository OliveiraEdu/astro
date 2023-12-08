def draw_sierpinski_triangle(order, size, x, y):
    if order == 0:
        # Draw a filled triangle
        for i in range(int(size)):
            for j in range(int(i) + 1):
                print("*", end=" ")
            print()
    else:
        # Recursively draw three smaller triangles
        draw_sierpinski_triangle(order - 1, size / 2, x, y)
        draw_sierpinski_triangle(order - 1, size / 2, x + size / 2, y)
        draw_sierpinski_triangle(order - 1, size / 2, x + size / 4, y - size * 0.866 / 2)

def main():
    order = 10  # Adjust the order of the Sierpinski Triangle
    size = 10 # Adjust the size of the triangle
    draw_sierpinski_triangle(order, size, 0, 0)

if __name__ == "__main__":
    main()
