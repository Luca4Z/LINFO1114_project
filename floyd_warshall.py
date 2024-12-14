import numpy as np

def floyd_warshall(matrice):
    """
    @pre: une matrice[][] de coût, où matrice[i][j] représente le coût entre le nœud i et j.
          matrice[i][j] = float('inf') si aucun chemin direct n'existe.
    @post: une matrice[][] contenant les distances les plus courtes entre toutes les paires de nœuds.
    """
    dist = np.array(matrice, dtype=float)

    n = len(matrice)  # Nombre de nœuds dans le graphe

    # Initialisation : les distances des nœuds à eux-mêmes sont 0
    for i in range(n):
        dist[i][i] = 0

    # Algorithme de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Mise à jour de la distance avec un chemin passant par k si c'est plus court
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Convertir les distances en entiers avant de les renvoyer
    dist = dist.astype(int)

    return dist