import random

def rotate(grille):
    size = len(grille)
    return [[grille[size - j - 1][i] for j in range(size)] for i in range(size)]

def generate_grille(size):
    grille = [[0]*size for _ in range(size)]
    positions = []
    total_holes = (size * size) 

    while len(positions) < total_holes:
        i = random.randint(0, size-1)
        j = random.randint(0, size-1)

        g = [[0]*size for _ in range(size)]
        g[i][j] = 1

        ok = True
        temp = g

        for _ in range(4):
            for x in range(size):
                for y in range(size):
                    if temp[x][y] == 1 and (x, y) in positions:
                        ok = False
            temp = rotate(temp)

        if ok:
            positions.append((i, j))

    for (i, j) in positions:
        grille[i][j] = 1

    return grille

def print_grille(grille):
    print("\nGrille (1 = vrima):")
    for row in grille:
        print(" ".join(str(x) for x in row))

def encrypt(message, grille):
    size = len(grille)
    grid = [["X" for _ in range(size)] for _ in range(size)]
    index = 0

    for _ in range(4):
        for i in range(size):
            for j in range(size):
                if grille[i][j] == 1 and index < len(message):
                    grid[i][j] = message[index]
                    index += 1
        grille = rotate(grille)

        cipher_text = ""
        for row in grid:
            cipher_text += "".join(row)

        print("\nEncrypted (string):", cipher_text)
        return cipher_text







