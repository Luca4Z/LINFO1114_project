# 1) main lit le fichier CSV, qui contient la matrice de coût
# 2) Exécute le calcul des matrices de distance des plus courts chemins(via les trois fonctions)
# 3) Imprime les résultats à l’écran (la matrice de coûts et les trois matrices de distances)

import numpy
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall


with open('matrice.csv', 'r') as f:

    # Lire la première ligne
    f.readline()

    matrice_c = []
    index_loop = 0
    for i in f:
        # ajouter une liste sans le premier élément (le premier élément c'est la première colonne qui nous intéresse pas, voir matrice.csv)
        matrice_c.append(i.strip().split(',')[1:])

        # convertir en int
        for j in range(len(matrice_c[index_loop])):
            matrice_c[index_loop][j] = int(matrice_c[index_loop][j])

        index_loop += 1


    matrice_dijkstra = dijkstra(matrice_c)
    matrice_bellman_ford = bellman_ford(matrice_c)
    matrice_floyd_warshall = floyd_warshall(matrice_c)
    
    print("La matrice de coût:\n", numpy.matrix(matrice_c)) # "Avec numpy, c'est censé mieux afficher la matrice"
    print("\nLa matrice des distances des plus courts chemins entre toutes paires de noeuds en utilisant l'algorithme de Dijkstra:\n", numpy.matrix(matrice_dijkstra))
    print("\nLa matrice des distances des plus courts chemins entre toutes paires de noeuds en utilisant l'algorithme de Bellman-Ford:\n", matrice_bellman_ford)
    print("\nLa matrice des distances des plus courts chemins entre toutes paires de noeuds en utilisant l'algorithme de Floyd-Warshall:\n", matrice_floyd_warshall)

# Solution normalment:
"""
(matrice symétrique)
/ A B C D E F G H I J
A 0 . . . . . . . . .
B 3 0 . . . . . . . .
C 1 2 0 . . . . . . .
D 3 6 4 0 . . . . . .
E 3 3 2 5 0 . . . . .
F 2 3 1 4 1 0 . . . .
G 5 4 4 7 2 3 0 . . .
H 5 5 4 7 2 3 2 0 . .
I 5 7 5 2 5 4 7 5 0 .
J 7 7 5 7 4 5 4 2 5 0
"""

# Matrice de coût mise dans une variable
"""
(matrice de coût)
mC = [
        [0, 5, 1, 3, 99999999, 99999999, 99999999, 99999999, 99999999, 99999999], 
        [5, 0, 2, 99999999, 3, 99999999, 4, 99999999, 99999999, 99999999], 
        [1, 2, 0, 5, 3, 1, 99999999, 99999999, 99999999, 99999999], 
        [3, 99999999, 5, 0, 99999999, 4, 99999999, 99999999, 2, 99999999], 
        [99999999, 3, 3, 99999999, 0, 1, 2, 2, 99999999, 99999999],
        [99999999, 99999999, 1, 4, 1, 0, 99999999, 3, 4, 99999999], 
        [99999999, 4, 99999999, 99999999, 2, 99999999, 0, 2, 99999999, 5], 
        [99999999, 99999999, 99999999, 99999999, 2, 3, 2, 0, 5, 2], 
        [99999999, 99999999, 99999999, 2, 99999999, 4, 99999999, 5, 0, 5], 
        [99999999, 99999999, 99999999, 99999999, 99999999, 99999999, 5, 2, 5, 0]
    ]

"""