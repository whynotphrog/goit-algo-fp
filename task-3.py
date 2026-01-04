import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

print(dijkstra(graph, 'A'))