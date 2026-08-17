import math

def dijkstra(graph, source):
    n = len(graph)
    dist = [math.inf] * n
    visited = [False] * n
    dist[source] = 0
    for k in range(n):
        u = -1
        min_dist = math.inf
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != math.inf and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
    return dist
graph = [
    [0, 4, math.inf, math.inf, 8],
    [4, 0, 2, 5, math.inf],
    [math.inf, 2, 0, 1, 6],
    [math.inf, 5, 1, 0, 3],
    [8, math.inf, 6, 3, 0]
]
cities = ["A", "B", "C", "D", "E"]
source = 0
distances = dijkstra(graph, source)
print("Shortest distances from", cities[source])
for i in range(len(cities)):
    print(f"{cities[source]} -> {cities[i]} = {distances[i]}")
