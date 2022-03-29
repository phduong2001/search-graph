import numpy as np


def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:

    visited = {start: -1}
    path = []

    stack = [start]

    while stack:
        current = stack.pop()

        if current == end:
            break

        for i in range(matrix.shape[1] - 1, -1, -1):
            if matrix[current, i] != 0:
                if i not in visited:
                    stack.append(i)
                    visited[i] = current

    temp = end
    while temp != -1:
        path.append(temp)
        temp = visited[temp]
    path.reverse()

    print(visited, path)

    return visited, path


def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 

    path = []
    visited = {start: -1}

    queue = [start]

    while queue:
        current = queue.pop(0)

        if current == end:
            break

        for i in range(0, matrix.shape[1]):
            if matrix[current, i] != 0:
                if i not in visited:
                    queue.append(i)
                    visited[i] = current

    temp = end
    while temp != -1:
        path.append(temp)
        temp = visited[temp]
    path.reverse()

    print(visited, path)

    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:

    path = []
    visited = {start: -1}

    cost = 10 ** 8
    queue = [[0, start]]

    while queue:
        queue = sorted(queue)
        p = queue.pop()

        p[0] *= -1

        if p[1] == end:
            cost = min(cost, p[0])
            queue = sorted(queue)

        for i in range(0, matrix.shape[1]):
            if matrix[p[1], i] != 0:
                distance = p[0] + matrix[p[1], i]
                if i not in visited:
                    queue.append([distance * -1, i])
                    visited[i] = p[1]
                if i == end and cost > p[0] + matrix[p[1], i]:
                    cost = distance
                    visited[i] = p[1]

    temp = end
    while temp != -1:
        path.append(temp)
        temp = visited[temp]
    path.reverse()

    print(visited, path)

    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:

    path = []
    visited = {start: -1}

    queue = [(0, start)]

    while queue:
        queue = sorted(queue)
        p = queue.pop()

        if p[1] == end:
            break

        for i in range(0, matrix.shape[1]):
            if matrix[p[1], i] != 0:
                if i not in visited:
                    queue.append((matrix[p[1], i], i))
                    visited[i] = p[1]

    temp = end
    while temp != -1:
        path.append(temp)
        temp = visited[temp]
    path.reverse()

    print(visited, path)

    return visited, path


def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path = []
    visited = {}
    return visited, path
