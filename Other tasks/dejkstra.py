# Algorithm Dejkstry
# search for the shortest path from one knot of the graph to all others

# Matrix as a list of lists

from collections import deque


def dejkstra(matrix, start):
    n = len(matrix)
    distance = [None] * n
    path = [0] * n
    distance[start] = 0
    nonvisited = [start]
    visited = []

    while nonvisited:
        current = min(nonvisited, key=lambda x: distance[x])
        current_dist = distance[current]
        for i, weight in enumerate(matrix[current]):
            if i in visited:
                continue
            if weight:
                if distance[i] is None or distance[i] > weight + current_dist:
                    distance[i] = weight + current_dist
                    path[i] = current
                nonvisited.append(i)
        visited.append(current)
        nonvisited.remove(current)

    return distance, path


def recreate_path(path_list, node):
    path = deque()
    current = node
    path.append(node)
    while path_list[current] != current:
        path.appendleft(path_list[current])
        current = path_list[current]

    return list(path)


Matrix = [
            [0, 1, 3, 5, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 4, 2, 0, 0],
            [1, 0, 1, 3, 0]
]


start = 0
dist, path = dejkstra(Matrix, start)
print(dist, path)       # [0, 1, 2, 4, 1] [0, 0, 4, 4, 0]
node = 2
path_list = recreate_path(path, node)
print(f'path from start={start} to node={node}: {path_list}')   # path from start=0 to node=2: [0, 4, 2]
print('')

Matrix2 = [
            [0,	 7,	 9,	  0, 0, 14],
            [7,	 0,	 10, 15, 0, 0],
            [9,	 10, 0,	 11, 0, 2],
            [0,	 15, 11,  0, 6, 0],
            [0,	 0,	 0,	  6, 0, 9],
            [14, 0,	 2,	  0, 9, 0]
]
start2 = 0
dist2, path2 = dejkstra(Matrix2, start)
print(dist2, path2)       # [0, 7, 9, 20, 20, 11] [0, 0, 0, 2, 5, 2]
node2 = 4
path_list2 = recreate_path(path2, node2)
print(f'path from start={start2} to node={node2}: {path_list2}')    # path from start=0 to node=4: [0, 2, 5, 4]


####################################################
# Matrix as a dict


import operator


def dejk(matrix, start):
    dist = dict.fromkeys(matrix.keys(), None)
    dist[start] = 0
    nonvisited = dist.copy()
    path = dist.copy()
    path[start] = start
    visited = []
    elements = len(matrix.keys())
    while nonvisited:
        knot, weight = min(list(filter(lambda item: item[1] is not None, nonvisited.items())), key=operator.itemgetter(1))
        for child in matrix[knot].keys():
            if child not in nonvisited:
                continue

            if dist[child] is None or dist[child] > matrix[knot][child] + weight:
                dist[child] = matrix[knot][child] + weight
                path[child] = knot

            nonvisited[child] = dist[child]

        del nonvisited[knot]

    return dist, path


G = {
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'B': {'A': 5, 'D': 1, 'G': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16},
    'G': {'B': 2, 'D': 1, 'C': 2},
}


dist, path = dejk(G, 'B')
print(dist)
print(path)

# {'A': 4, 'B': 0, 'C': 3, 'D': 1, 'E': 2, 'F': 4, 'G': 2}
# {'A': 'D', 'B': 'B', 'C': 'E', 'D': 'B', 'E': 'D', 'F': 'E', 'G': 'B'}
