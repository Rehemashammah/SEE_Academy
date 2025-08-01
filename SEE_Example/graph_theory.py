graph =   {
      "A": ["B", "C"],
      "B": ["A", "D"],
      "C": ["A", "E"],
      "D": ["B"],
      "E": ["C"]
}

#Depth First Search(DFS)
def dfs(graph, start, visited=None) :
    if visited is None:
        visited = set()
    visited.add(start)
    
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
dfs(graph, "E")