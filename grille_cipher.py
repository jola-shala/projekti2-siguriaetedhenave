# pjesa enkriptimit

def decrypt_grille(cipher, grille, size):
    matrix = [list(cipher[i*size:(i+1)*size]) for i in range(size)]

    result = []
    for i in range(size):
        for j in range(size):
            if grille[i][j] == 1:
                result.append(matrix[i][j])

    return ''. join(result)

def input_grille(size):
    print("Shkruaj grille (0 dhe 1): ")
    grille = []

    for i in range(size):
        row_input = input(f"Rreshti {i+1}: ")

        if " " in row_input:
            row = [int(x) for x in row_input.split()]
        else:
            row = [int(x) for x in row_input.strip()]

        if len(row) != size:
            print("Gabim: Rreshti nuk ka gjatesi te sakte!")
            exit()

        grille.append(row)
    
    return grille








