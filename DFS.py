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
visited=[]
stack=[]
def dfs(visited,graph,node):
    stack.append(node)
    m = stack.pop()
    if m not in visited:
        print (m,end="")
        visited.append(m)
        for neighbor in reversed(graph[m]):
            if neighbor not in visited:
                stack.append(neighbor)
print("Following is the DFS: \n")
dfs(visited,graph,1)
