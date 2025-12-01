def is_safe(node, graph, color, c):
    """Check if assigning color c to node is valid."""
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True


def solve_coloring(node, graph, color, K, N):
    """Backtracking function to color the vertices."""
    if node == N:
        return True

    for c in range(1, K + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if solve_coloring(node + 1, graph, color, K, N):
                return True
            color[node] = 0

    return False

N = int(input("Enter number of vertices: "))
M = int(input("Enter number of edges: "))
K = int(input("Enter number of colors: "))

graph = [[] for _ in range(N)]

print("\nEnter edges (u v):")
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

color = [0] * N

if solve_coloring(0, graph, color, K, N):
    print(f"\nColoring Possible with {K} Colors")
    print("Color Assignment:", color)
else:
    print(f"\nColoring Not Possible with {K} Colors")
