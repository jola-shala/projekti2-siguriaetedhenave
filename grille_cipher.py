# pjesa enkriptimit

def decrypt_grille(cipher, grille, size):
    matrix = [list(cipher[i*size:(i+1)*size]) for i in range(size)]

    result = []
    for i in range(size):
        for j in range(size):
            if grille[i][j] == 1:
                result.append(matrix[i][j])

    return ''. join(result)







