# Algorithm Floyda
# search for the shortest path from all knots of the graph to all other


def floyd(matrix):
    n = len(matrix)
    # dd = [None] * n
    # D = [dd[:]] * n
    # S = [dd[:]] * n
    D = matrix[:]
    t = tuple(range(n))
    S = [list(t) for i in range(n)]

    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or j == i:
                    continue
                if D[i][k] == 0 or D[k][j] == 0:
                    continue
                new_dist = D[i][k] + D[k][j]
                if new_dist < D[i][j] or D[i][j] == 0:
                    D[i][j] = new_dist
                    S[i][j] = k

    return D, S


def path(path_matrix, start, end):
    path = [start, end]
    current = end
    while path_matrix[start][current] != current:
        current = path_matrix[start][current]
        path.insert(1, current)
    return path


Matrix = [
            [0, 1, 3, 5, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 4, 2, 0, 0],
            [1, 0, 1, 3, 0]
]

Distance, Route = floyd(Matrix)
print('Distance')
print(Distance)
print('Route')
print(Route)
print('')

dist_0_4 = Distance[0][4]
path_0_4 = path(Route, 0, 4)
print('From 0 to 4 distance={}, path={}'.format(dist_0_4, path_0_4))

dist_0_2 = Distance[0][2]
path_0_2 = path(Route, 0, 2)
print('From 0 to 2 distance={}, path={}'.format(dist_0_2, path_0_2))

dist_3_0 = Distance[3][0]
path_3_0 = path(Route, 3, 0)
print('From 3 to 0 distance={}, path={}'.format(dist_3_0, path_3_0))
