def draw_sierpinski_triangle(order, size, x, y):
    lines = []
    if order == 0:
        # Draw a filled triangle
        for i in range(int(size)):
            spaces = " " * (2 * (int(size) - i) - 2)
            triangles = "*" * (2 * i + 1)
            lines.append(spaces + triangles)
    else:
        # Recursively draw three smaller triangles
        draw_sierpinski_triangle(order - 1, int(size / 2), x, y)
        draw_sierpinski_triangle(order - 1, int(size / 2), x + size / 2, y)
        draw_sierpinski_triangle(order - 1, int(size / 2), x + size / 4, y - size * 0.866 / 2)

    for line in lines:
        print(line)

def main():
    order = 20  # Adjust the order of the Sierpinski Triangle
    size = 8  # Adjust the size of the triangle
    draw_sierpinski_triangle(order, size, 0, 0)

if __name__ == "__main__":
    main()
