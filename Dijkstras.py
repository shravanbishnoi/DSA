import heapq


def dijkstra(graph, start):
    dist = {}
    for vertex in graph:
        dist[vertex] = float('infinity')
    dist[start] = 0
    PQ = [(0, start)]
    
    while PQ:
        # Pop the vertex with the smallest distance from the priority queue
        currentDist, currentVert = heapq.heappop(PQ)
        if currentDist > dist[currentVert]:
            continue
        
        for neighbor, weight in graph[currentVert].items():
            distance = currentDist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(PQ, (distance, neighbor))
    return dist

graph = {
    'A': {'B': 10, 'C': 5},
    'B': {'C': 3},
    'C': {'B': 4, 'D': 1},
    'D': {'B': 2}
}

vertex = 'A'
print(dijkstra(graph, vertex))
