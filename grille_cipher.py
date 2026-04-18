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

<<<<<<< Updated upstream
def print_grille(grille):
    print("\nGrille (1 = vrima):")
    for row in grille:
        print(" ".join(str(x) for x in row))

def encrypt(message, grille):
    size = len(grille)
    grid = [["X" for _ in range(size)] for _ in range(size)]
    index = 0
=======

# DECRYPT NGA STRING
def decrypt(cipher_text, grille):
    size = len(grille)

    # kthe string në grid
    grid = []
    index = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(cipher_text[index])
            index += 1
        grid.append(row)

    message = ""

    for _ in range(4):
        for i in range(size):
            for j in range(size):
                if grille[i][j] == 1:
                    message += grid[i][j] 
                    grille = rotate(grille)

                    return message


# =========================
# ▶️ MENU
# =========================
if __name__ == "__main__":

    size = int(input("Jep madhësinë e matrices (p.sh. 4): "))

    grille = generate_grille(size)
    print_grille(grille)
 
    while True:
        print("\n--- GRILLE CIPHER ---")
        print("1.Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Zgjedh: ")

        if choice == "1":
            msg = input("Mesazhi: ")
            cipher = encrypt(msg, grille)

        elif choice == "2":
            cipher = input("Shkruaj cipher text: ")
            print("Decrypted:", decrypt(cipher,grille))


       elif choice == "3":
        break
    
    else:
        print("Gabim!")
        


