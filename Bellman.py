from Graph import Graph
import math

G = Graph()
with open('/home/shravan/Desktop/ADSA/code/data1.txt', 'r') as file:
    lines = file.readlines()

for line in range(1, len(lines)):
    data = lines[line].split()
    G.add_vertex(int(data[0]))
    G.add_vertex(int(data[1]))
    G.add_edge(int(data[0]), int(data[1]), int(data[2]))


def Bellman(graph, node):
    distances = {}

    for vert, data in G:
        if vert!=node:
            distances[vert] = 10000000000
    distances[node] = 0
    for u in range(1, len(graph)):
        for v, w in graph.get_adjacency(u):
            if (distances[u] + w) < distances[v]:
                distances[v] = distances[u] + w

    for u in range(1, len(graph)):
        for v, w in graph.get_adjacency(u):
            if (distances[u] + w) < distances[v]:
                return "Graph contains a negative cycle"
    return distances

print(Bellman(G, 1))
