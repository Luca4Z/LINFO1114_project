import numpy


def dijkstra(matrice):
    """
    @pre: une matrice[][] de coût
    @post: une matrice[][] R contenant la longeur des chemins le plus court entre le noeud i et j 

    # l'algorithme de Dijkstra calcule les distances de tout noeud au départ d'un noeud de départ prédéfini et devront donc être exécutés dans une boucle permettant le calcul de toutes les distances entre noeuds.
    """
    
    # Créons une matrice vide, de départ
    matriceR = create_empty_matrice(len(matrice), len(matrice[0]))

    # pour chaque noeud calculons la distance du plus court chemin. Comme la matric est symétrique. Dx = [0, len(matrice)] et Dy = [0, x]
    for i in range(len(matrice)):
        for j in range(i+1):
            matriceR[i][j] = find_shortest_path(matrice, i, j)

    # ajouter la symétrie, pour que la matrice soit complète
    return add_symétrie(matriceR)

def create_empty_matrice(row, columns):
    """
    @pre: Un INT, le nombre de rangées
          Un INT, le nombre de colonnes
    @post: une matrice[][] E vide, de longueur et hauteur spécifié par les arguments
    """

    matrice = []

    for _ in range(row):
        tempMatrice = []
        for _ in range(columns):
            tempMatrice.append("")
        matrice.append(tempMatrice)
    return matrice

def create_init_table(startNode):
    """
    @pre: un INT, le noeud de départ (A=0, B=1, ...)
    @post: une matrice[][] contenant l'initialisation du tableau. Le noeud de départ vaut 0, les autres l'infini (représenté par 999).

    """
    matrice = create_empty_matrice(10, 10)
    for i in range(len(matrice)):
        if startNode == i :
            matrice[i][0] = -1
        else:
            matrice[i][0] = 999
    return matrice

def find_shortest_path(matriceC, startNode, endNode):
    """
    @pre: une matrice[][] de coût
          INT le noeud de départ (0=A, 1=B, ...)
          INT le noeud d'arrivée (0=A, 1=B, ...)
    @post: le coût de la distance du plus court chemin entre startNode et endNode 
    """
    if startNode == endNode :
        return 0
    
    
    matriceInit = create_init_table(startNode)

    # Créons un dictionnaire qui mémorisera les coûts minimales de chaque noeud
    costs = {0: matriceInit[0][0], 1: matriceInit[1][0], 2: matriceInit[2][0], 3: matriceInit[3][0], 4: matriceInit[4][0], 5: matriceInit[5][0], 6: matriceInit[6][0], 7: matriceInit[7][0], 8: matriceInit[8][0], 9: matriceInit[9][0]}

    # Définissons des variables utiles, tels que le frigo, le plus petit coût total et temporaire et le noeud de départ
    smallestNode = startNode
    node = startNode
    smallestCostTemp = 99999999999
    smallestCost = 0
    fridge = [startNode]

    for i in range (len(matriceInit)):
        for j in range(len(matriceInit[0])):

            # Obtenir le coût entre le noeud et le noeud j
            cost = matriceC[node][j]

            # Vérifiér si le coût est inférieur au coût minimale jusqu'à présent, et que le noeud n'est pas encore dans le frigo
            if cost < smallestCostTemp and j not in fridge and cost:
                smallestCostTemp = cost
                smallestNode = j
            
            # Ajuster le dictionnaire des coûts du noeud J si le coût actuelle est infiérieur à son coût au temps i-1
            if costs[j] > cost + smallestCost and costs[j] != -1:
                cost = matriceC[node][j]
                costs[j] = cost+smallestCost

        # Trouvons le noeud avec la distance le plus court. Soit il se trouve à partir du noeud sur lequel on vient d'arriver, soit c'est un ancien noeud:
        for k in range(len(matriceInit)):
            if smallestCostTemp+smallestCost > costs[k] and k not in fridge:
                smallestCostTemp = costs[k]
                smallestNode = k
                smallestCost = 0

        # Ajouter dans le frigo le noeud avec la distance la plus coûrte et lui assigner un coût de -1 pour ne plus le considérer
        fridge.append(smallestNode)
        costs[smallestNode] = -1
        node = smallestNode

        # Augmenter le coût
        smallestCost += smallestCostTemp
        
        # Vérifier si nous sommes arrivés au noeud de fin 'endNode'
        if smallestNode == endNode:
            return smallestCost
        
        # Remmetre smallestCostTemp à une valeur élévé pour l'itération suivante
        smallestCostTemp = 300000

    return "/"

def add_symétrie(matrice):
    """
    @pre: une matrice[][] remplit à moitie, la partie bas-gauche
    @post: une matrice[][] R remplit symétrique 

    """
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice[i][j] = matrice[j][i]
    return matrice