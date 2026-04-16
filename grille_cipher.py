import random

def rotate(grille):
    size = len(grille)
    return [[grille[size - j - 1][i] for j in range(size)] for i in range(size)]

def generate_grille(size):
    grille = [[0]*size for _ in range(size)]
    positions = []
    total_holes = (size * size) 

    







