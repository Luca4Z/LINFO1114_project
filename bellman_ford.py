import numpy as np

def bellman_ford(matrice):
    """
    Calcule la matrice des plus courts chemins entre toutes les paires de nœuds.

    Args:
        matrice: Matrice de coût représentant les poids des arêtes.

    Returns:
        Matrice des plus courts chemins.
    """

    n = len(matrice)  # Nombre de nœuds

    # Initialisation de la matrice des distances à l'infini
    matriceR = create_empty_matrice(n, n)

    # Pour chaque nœud en tant que source, calculer les distances minimales
    for i in range(n):
        # Calcul des distances minimales à partir du nœud i
        distances = bellman_ford_single_source(matrice, i)
        # Copie des distances dans la matrice résultat
        for j in range(n):
            matriceR[i][j] = distances[j]

    # Rendre la matrice symétrique (les distances sont les mêmes dans les deux sens)
    matriceR = add_symetrie(matriceR)

    # Convertir en tableau NumPy d'entiers
    matriceR = np.array(matriceR, dtype=int)

    return matriceR

def bellman_ford_single_source(matrice, startNode):
    """
    Calcule les distances minimales à partir d'un nœud source donné.

    Args:
        matrice: Matrice de coût.
        startNode: Index du nœud de départ.

    Returns:
        Tableau des distances minimales.
    """

    num_vertices = len(matrice)
    distance = [float('inf')] * num_vertices
    distance[startNode] = 0

    # Relaxation des arêtes |V|-1 fois pour garantir la convergence
    for _ in range(num_vertices - 1):
        # Pour chaque arête, vérifier si on peut améliorer la distance
        for u in range(num_vertices):
            for v in range(num_vertices):
                if matrice[u][v] != 99999999 and distance[u] != float('inf') and distance[u] + matrice[u][v] < distance[v]:
                    distance[v] = distance[u] + matrice[u][v]

    # Vérification de cycles négatifs
    for u in range(num_vertices):
        for v in range(num_vertices):
            if distance[u] != float('inf') and distance[u] + matrice[u][v] < distance[v]:
                print("Graph contains negative cycle")
                return None

    return distance


def create_empty_matrice(row, columns):
    """
    @pre: Un INT, le nombre de rangées
          Un INT, le nombre de colonnes
    @post: une matrice[][] vide de longueur et hauteur spécifiée par les arguments
    """

    matrice = []

    for _ in range(row):
        tempMatrice = []
        for _ in range(columns):
            tempMatrice.append(99999999)  # Valeur initiale pour les non-connectés (ou infinie)
        matrice.append(tempMatrice)
    return matrice


def add_symetrie(matrice):
    """
    @pre: une matrice[][] remplie à moitié, la partie bas-gauche
    @post: une matrice[][] symétrique
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice[j][i] = matrice[i][j]  # Ajouter la symétrie
    return matrice