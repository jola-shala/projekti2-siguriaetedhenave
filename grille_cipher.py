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









