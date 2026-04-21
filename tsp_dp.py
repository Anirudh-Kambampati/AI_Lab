def tsp_dp(dist):
    n = len(dist)
    VISITED = (1 << n) - 1

    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            dp[mask][u] + dist[u][v]
                        )

    ans = float('inf')
    for i in range(1, n):
        ans = min(ans, dp[VISITED][i] + dist[i][0])

    return ans

dist = [
 [0,10,15,20],
 [10,0,35,25],
 [15,35,0,30],
 [20,25,30,0]
]

print("Cost:", tsp_dp(dist))