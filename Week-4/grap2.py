def function(tanks, pipes ):
    graph = {tank : [] for tank in tanks}
    for u,v in pipes:
        graph[u].append(v)

    candidate = None
    visited = set()
    
    def dfs(tank):
        visited.add(tank)
        for next_tank in graph[tank]:
            if next_tank not in visited:
                dfs(next_tank)

    for tank in tanks:
        if tank not in visited:
            dfs(tank)
            candidate = True
        
    visited = set()
    dfs(candidate)
    if len(visited) == len(tanks):
        return candidate
    return 0
