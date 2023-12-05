def generate_magic_square():
    n = 3
    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2

    for num in range(1, n*n + 1):
        magic_square[i][j] = num
        i -= 1
        j += 1

        if num % n == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j == n:
            j = 0
    
    return magic_square

def print_square(square):
    for row in square:
        print(row)

magic_square = generate_magic_square()
print_square(magic_square)