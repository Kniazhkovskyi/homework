import sys


def get_triangle(n):

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle


def print_triangle(triangle):

    width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        line = " ".join(map(str, row))
        print(line.center(width))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python triangle.py <число строк>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError

        triangle = get_triangle(n)
        print_triangle(triangle)

    except ValueError:
        print("Ошибка: Введите положительное целое число строк.")
