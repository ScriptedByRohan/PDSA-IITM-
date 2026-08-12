def findConnectionLevel(n,gmat,px,py): #gmat is adjacent matrix
    if px == py:
        return 0
    
    visited = [False] * n
    queue = [(px,0)]

    visited[px] = True

    while queue:
        person, level = queue.pop(0)

        for friend in range(n):
            if gmat[person][friend] == 1 and not visited[friend]:
                if friend == py:
                    return level+1
                
                visited[friend] = True
                queue.append((friend,level+1))
    return 0 