import numpy


def dijkstra(matrice):
    """
    @pre: une matrice[][] de coût
    @post: une matrice[][] R contenant la longeur des chemins le plus court entre le noeud i et j 

    # l'algorithme de Dijkstra calcule les distances de tout noeud au départ d'un noeud de départ prédéfini et devront donc être exécutés dans une boucle permettant le calcul de toutes les distances entre noeuds.
    """
    # TODO
    matriceR = create_empty_matrice(len(matrice), len(matrice[0]))
    matriceInit = create_init_table(3)

    for i in range(len(matrice)):
        for j in range(i+1):
            #if i == 1 & j == 1:
                #matriceR[3][1] = find_shortest_path(matrice, 3, 1)
            matriceR[i][j] = find_shortest_path(matrice, i, j)
        if i == 4:
            break



    print(numpy.matrix(matriceR))
    #print(numpy.matrix(matriceInit))
    return [[]]

def create_empty_matrice(row, columns):
    matrice = []
    for _ in range(row):
        tempMatrice = []
        for _ in range(columns):
            tempMatrice.append("")
        matrice.append(tempMatrice)
    return matrice

def create_init_table(startNode):
    matrice = create_empty_matrice(10, 10)
    #hashMap = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
    for i in range(len(matrice)):
        if startNode == i :
            matrice[i][0] = -1
        else:
            matrice[i][0] = 999
    return matrice

def find_shortest_path(matriceC, startNode, endNode):
    if startNode == endNode :
        return 0
    else:
    
        matriceInit = create_init_table(startNode)
        costs = {0: matriceInit[0][0], 1: matriceInit[1][0], 2: matriceInit[2][0], 3: matriceInit[3][0], 4: matriceInit[4][0], 5: matriceInit[5][0], 6: matriceInit[6][0], 7: matriceInit[7][0], 8: matriceInit[8][0], 9: matriceInit[9][0]}
        print("costs:", costs)
        smallestNode = startNode
        node = startNode
        smallestCostTemp = 99999999999
        smallestCost = 0
        fridge = [startNode]
        print(startNode, endNode)
        for i in range (len(matriceInit)):
            print("node:", node, "fridge:", fridge)
            for j in range(len(matriceInit[0])):
                cost = matriceC[node][j]
                if cost < smallestCostTemp and j not in fridge and cost:
                    smallestCostTemp = cost
                    smallestNode = j
                if costs[j] > cost + smallestCost and costs[j] != -1:
                    cost = matriceC[node][j]
                    #print("smallest cost of node 1!ç! is", costs[1])
                    #if cost + smallestCOst < costs[j]
                    costs[j] = cost+smallestCost
                    print("smallest cost of node 1!ç! is", costs[1])
                print("smallest cost of node", j, "is", costs[j])
            # check previous smallest:
            for k in range(len(matriceInit)):
                if smallestCostTemp > costs[k] and k not in fridge:
                    print("changes")
                    smallestCostTemp = costs[k]
                    smallestNode = k
                    smallestCost = 0 # on ajoute costs[k] après
            print("smallest is", smallestCostTemp)
            fridge.append(smallestNode)
            costs[smallestNode] = -1
            node = smallestNode
            smallestCost += smallestCostTemp
            print(costs)


            
            
            #print("plus petit coût entre", startNode, "et quelconque", "vaut:", smallestCost, "avec le noeud", smallestNode)
            
            
            if smallestNode == endNode:
                print("fin. plus petit coût entre", startNode, "et", endNode, "-->", smallestCost)
                return smallestCost
            smallestCostTemp = 300000
                
            #break
        #print(matriceC[startNode][endNode])

        #print(numpy.matrix(matriceInit))
        return "?"



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

dijkstra(mC)