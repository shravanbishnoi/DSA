"""
Here is the implementation of Dijkstra's Algorithm.

Author: Shravan
Date: 25-04-2024
"""
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from start node to all other nodes in the graph.

    Parameters:
    graph (dict): The graph represented as a dictionary where keys are node names and values are lists of tuples.
    Each tuple contains a neighbor node and the weight of the edge between the node and its neighbor.
    start: The starting node.

    Returns:
    dict: A dictionary where keys are node names and values are the shortest distances from the start node.
    """
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    PQ = [(0, start)]
    visited = set()

    while PQ:
        currentDist, currentNode = heapq.heappop(PQ)
        if currentNode in visited:
            continue
        visited.add(currentNode)
        for neighbor, weight in graph[currentNode]:
            if neighbor in visited:
                continue

            new_distance = currentDist + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                heapq.heappush(PQ, (new_distance, neighbor))
    return dist

graph = {
    's': [('a', 2), ('b', 1)],
    'a': [('b', -2)],
    'b': [],
}
start = 's'
dist = dijkstra(graph, start)
for i, j in dist.items():
    print(f"Distance from {start} to {i} is: ", j)
