def bfsShortest(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        currentState, path = queue.pop(0)
        for i in graph[currentState]:
            if i not in path:
                if i == goal:
                    return path + [i]
                else:
                    queue.append((i, path + [i]))

def dijkstraShortestPath(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    shortest_path = {}
    visited = set()

    while len(visited) < len(graph):
        current_node = min(
            (node for node in graph if node not in visited), key=lambda x: distances[x]
        )
        visited.add(current_node)

        for i, j in graph[current_node].items():
            if distances[current_node] + j < distances[i]:
                distances[i] = distances[current_node] + j
                shortest_path[i] = (current_node, j)

    path = [end]
    total_weight = 0
    while end != start:
        parent, weight = shortest_path[end]
        path.insert(0, parent)
        total_weight += weight
        end = parent

    return path, total_weight

graph = {
    'Istanbul': {'Bursa': 157, 'Tekirdag': 146},
    'Bursa': {'Istanbul': 157, 'Denizli':448 },
    'Tekirdag': {'Istanbul': 146, 'Denizli': 491, 'Edirne': 143},
    'Denizli': {'Bursa': 448, 'Tekirdag': 491, 'Edirne': 826},
    'Edirne': {'Tekirdag': 143, 'Denizli': 826}
}

s = bfsShortest(graph, "Istanbul", "Denizli")
d, w = dijkstraShortestPath(graph,"Istanbul", "Tekirdag")
print(s)
print(d, w)