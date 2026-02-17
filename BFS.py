graph = {
    1: [2,3,4],
    2: [5,6],
    3: [],
    4: [7,8],
    5: [9,10],
    6: [],
    7: [11,12],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}

visited = [] #List for visited nodes
queue = [] # for need to be visited
def bfs (visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end=" ")
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Breadth First Search: \n")
bfs(visited,graph,1)