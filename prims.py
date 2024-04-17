##  OUTPUTS THE EDGES NOT THE PARENT POINTERS ###
def prim(graph, weights, r):
    # Initialize variables
    vertices = len(graph)
    Q = list(range(vertices))
    key = [float('inf')] * vertices
    p = [None] * vertices

    key[r] = 0

    min_spanning_tree = []

    while Q:
        u = extract_min(Q, key)
        for v in graph[u]:
            if v in Q and weights[(u, v)] < key[v]:
                p[v] = u
                key[v] = weights[(u, v)]
    
    for i in range(1, vertices):
        min_spanning_tree.append((p[i], i))

    return min_spanning_tree

def extract_min(Q, key):
    min_key = float('inf')
    min_vertex = None
    for vertex in Q:
        if key[vertex] < min_key:
            min_key = key[vertex]
            min_vertex = vertex
    Q.remove(min_vertex)
    return min_vertex

# Example graph represented as an adjacency list
# Graph example is from slides
graph = {
    0: [1, 7],
    1: [0, 2, 7],
    2: [1, 4, 3],
    3: [2],
    4: [2, 5, 6, 7],
    5: [4],
    6: [4, 7],
    7: [0, 1, 4, 6]
}

# Example weights represented as a dictionary of tuples (u, v) to weight
weights = {
    (0, 1): 3,
    (1, 2): 8,
    (2, 3): 15,
    (2, 4): 2,
    (4, 5): 9,
    (4, 6): 4,
    (4, 7): 5,
    (6, 7): 6,
    (0, 7): 14,
    (1, 7): 10,
    (7, 1): 10,
    (7, 0): 14,
    (7, 6): 6,
    (7, 4): 5,
    (6, 4): 4,
    (5, 4): 9,
    (4, 2): 2,
    (3, 2): 15,
    (2, 1): 8,
    (1, 0): 3,
}

r = 1  # Starting vertex
result = prim(graph, weights, r)
print("Minimum Spanning Tree (list of vertices):", result)