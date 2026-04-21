def tsp_greedy(dist):
    n = len(dist)
    visited = [False]*n

    curr = 0
    visited[curr] = True
    path = [curr]
    cost = 0

    for _ in range(n-1):
        mn = float('inf')
        next_city = -1

        for i in range(n):
            if not visited[i] and dist[curr][i] < mn:
                mn = dist[curr][i]
                next_city = i

        cost += mn
        curr = next_city
        visited[curr] = True
        path.append(curr)

    cost += dist[curr][0]
    path.append(0)

    return path, cost

dist = [
 [0,5,9,10],
 [5,0,6,4],
 [9,6,0,8],
 [10,4,8,0]
]

print(tsp_greedy(dist))