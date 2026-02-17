# 🧠 AI Lab Programs — Search & Game Algorithms

This repository contains implementations of classic AI search and problem-solving programs, including graph traversal, game playing, and state-space search problems.

Each program includes:

* Algorithm overview
* Core idea
* Line-by-line code explanation

---

# 📌 Problem 1 — Breadth First Search (BFS)

## ✅ Algorithm — Breadth First Search

Breadth First Search traverses a graph **level by level** starting from a source node. It uses a **queue (FIFO)** so that nearer nodes are visited before deeper nodes.

**Steps**

1. Start from source node
2. Mark visited
3. Add to queue
4. Remove from front of queue
5. Add all unvisited neighbors
6. Repeat until queue is empty

---

## 💻 Code with Explanation

```python
"""
This code implements a Breadth-First Search (BFS) algorithm on a graph.
"""

# Graph stored as adjacency list (node -> neighbors)
graph = {
    1: [2,3,4],      # neighbors of node 1
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

visited = []      # list to track visited nodes
queue = []        # queue for BFS traversal

visited = []      # reinitialize visited list
queue = []        # reinitialize queue

def bfs (visited,graph,node):
    visited.append(node)        # mark start node visited
    queue.append(node)          # enqueue start node

    while queue:                # loop while queue not empty
        m = queue.pop(0)        # remove front element (FIFO)
        print (m,end =" ")      # visit node

        for neighbour in graph[m]:           # check neighbors
            if neighbour not in visited:     # if not visited
                visited.append(neighbour)    # mark visited
                queue.append(neighbour)      # enqueue neighbor

print ("Following is the bfs")
bfs(visited,graph,1)            # first traversal
bfs(visited,graph,1)            # second call prints nothing new (already visited)
```

---

# 📌 Problem 2 — Depth First Search (DFS using Stack)

## ✅ Algorithm — DFS (Iterative)

Depth First Search explores nodes by going **deep first** before backtracking. Uses a **stack (LIFO)**.

**Steps**

1. Push start node
2. Pop top node
3. Visit if not visited
4. Push neighbors
5. Repeat until stack empty

---

## 💻 Code with Explanation

```python
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

visited = []      # visited nodes list
stack = []        # stack for DFS

def dfs_stack(visited, graph, node):
    stack.append(node)          # push start node

    while stack:                # while stack not empty
        m= stack.pop()          # pop top node (LIFO)

        if m not in visited:    # process only if new
            print (m, end = " ")
            visited.append(m)   # mark visited

            # reverse keeps traversal order consistent
            for neighbour in reversed(graph[m]):
                if neighbour not in visited:
                    stack.append(neighbour)

print ("Following is the DFS (using Stack)")
dfs_stack(visited,graph,1)
```

---

# 📌 Problem 3 — Tic Tac Toe with Minimax

## ✅ Algorithm — Minimax

Minimax evaluates all possible moves in a game tree and selects the optimal move assuming both players play optimally.

**Scoring**

* Win → positive score
* Loss → negative score
* Draw → zero

---

## 💻 Code with Explanation

```python
import math   # used for infinity values

def print_board(board):
    print("\n")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))  # row 1
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))  # row 2
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))  # row 3
    print("\n")

def check_winner(board):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),   # rows
        (0,3,6),(1,4,7),(2,5,8),   # columns
        (0,4,8),(2,4,6)            # diagonals
    ]

    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]        # return winner symbol

    return None

def is_draw(board):
    return " " not in board        # draw if no empty space

# Minimax recursive evaluator
def minimax(board, depth, isMaximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1                   # maximizing player win
    if winner == "X":
        return -1                  # minimizing player win
    if is_draw(board):
        return 0                   # draw score

    # remaining code recursively explores moves and returns best score
```

---

# 📌 Problem 4 — Water Jug Problem (BFS State Search)

## ✅ Algorithm — State Space BFS

Each state = `(jug1_amount, jug2_amount)`
Use BFS to reach a state where one jug equals the goal.

**Operations**

* Fill jug
* Empty jug
* Pour between jugs

---

## 💻 Code with Explanation

```python
from collections import deque   # fast queue

def water_jug_bfs(jug1, jug2, goal):
    start = (0, 0)                          # both jugs empty
    queue = deque([(start, [])])            # queue holds state + path
    visited = set([start])                  # visited states

    while queue:
        (a, b), path = queue.popleft()      # get next state

        if a == goal or b == goal:          # goal check
            print("\nSolution Found:\n")
            for state in path:
                print(state)
            print(f"\nFinal State: (Jug1 = {a}, Jug2 = {b})")
            return

        next_states = [
            (jug1, b),                      # fill jug1
            (a, jug2),                      # fill jug2
            (0, b),                         # empty jug1
            (a, 0),                         # empty jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  # pour 1→2
            (a + min(b, jug1 - a), b - min(b, jug1 - a))   # pour 2→1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
```

---

# 📌 Problem 5 — 8 Puzzle (Best First Search)

## ✅ Algorithm — Heuristic Best-First Search

* Use heuristic = number of misplaced tiles
* Expand most promising state first
* Use priority queue

---

## 💻 Code with Explanation

```python
import heapq   # priority queue

GOAL_STATE=[
    [1,2,3],
    [4,5,6],
    [7,8,0]
]                          # target board

MOVES=[(-1,0),(1,0),(0,-1),(0,1)]   # blank moves

def heuristic(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=GOAL_STATE[i][j]:
                count+=1            # count misplaced tiles
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j          # blank position

def generate_states(state):
    x,y=find_blank(state)
    children=[]

    for dx,dy in MOVES:
        nx,ny=x+dx, y+dy            # new position

        if 0<=nx<3 and 0<=ny<3:     # bounds check
            new_state=[row[:] for row in state]   # copy board
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            children.append(new_state)

    return children
```

---

---

# 🎓 Viva Voce Q&A — AI Lab Programs

---

# ✅ BFS — Breadth First Search

**Q1. What is BFS?**
BFS is a graph traversal algorithm that visits nodes level by level starting from a source node using a queue.

**Q2. Which data structure is used in BFS?**
Queue (FIFO).

**Q3. Why queue is used in BFS?**
Because it processes nodes in the order they are discovered, ensuring level-wise traversal.

**Q4. What is the time complexity of BFS?**
O(V + E).

**Q5. What is the space complexity?**
O(V), due to visited list and queue.

**Q6. What happens if we don’t use a visited list?**
The algorithm may revisit nodes and can go into infinite loops in cyclic graphs.

**Q7. What does `pop(0)` do in your code?**
Removes the first element from the queue — FIFO behavior.

**Q8. Where is BFS used?**
Shortest path in unweighted graphs, network routing, web crawling.

---

# ✅ DFS — Depth First Search (Stack)

**Q1. What is DFS?**
DFS is a graph traversal algorithm that explores as deep as possible before backtracking.

**Q2. Which data structure is used here?**
Stack.

**Q3. Difference between BFS and DFS?**
BFS is level-wise using queue; DFS is depth-wise using stack or recursion.

**Q4. Why are neighbors reversed in the DFS code?**
To maintain correct left-to-right traversal order when using a stack.

**Q5. Can DFS be implemented without stack?**
Yes, using recursion (implicit stack).

**Q6. Time complexity of DFS?**
O(V + E).

**Q7. One advantage of DFS?**
Uses less memory than BFS in wide graphs.

---

# ✅ Tic Tac Toe — Minimax

**Q1. What is Minimax?**
Minimax is a decision algorithm used in two-player games to choose the optimal move by exploring all possible outcomes.

**Q2. What are maximizing and minimizing players?**
Maximizing tries to get highest score; minimizing tries to get lowest score.

**Q3. What are terminal states?**
Game over states — win, loss, or draw.

**Q4. What scores are used in your program?**
AI win = +1, human win = −1, draw = 0.

**Q5. Why is recursion used in minimax?**
To simulate future moves and evaluate outcomes.

**Q6. What is a drawback of minimax?**
High computation for large game trees.

**Q7. How can minimax be optimized?**
Using alpha-beta pruning.

---

# ✅ Water Jug Problem — BFS

**Q1. What type of problem is Water Jug?**
State space search problem.

**Q2. What represents a state?**
Amount of water in jug1 and jug2 → (a, b).

**Q3. Which algorithm is used here?**
BFS.

**Q4. Why BFS is suitable?**
It finds the shortest sequence of steps to reach the goal.

**Q5. Why is a visited set required?**
To avoid revisiting the same states and looping.

**Q6. Name two allowed operations.**
Fill a jug, empty a jug, pour between jugs.

**Q7. Why deque is used?**
Efficient queue operations from the front.

---

# ✅ 8 Puzzle — Best First Search

**Q1. What type of search is used?**
Heuristic Best-First Search.

**Q2. What is the heuristic in your code?**
Number of misplaced tiles.

**Q3. Why heuristic is used?**
To guide search toward the goal faster.

**Q4. What is the blank tile represented by?**
0.

**Q5. Why deep copy of state is created?**
To avoid modifying the original board.

**Q6. Which data structure manages priority?**
Priority queue using heapq.

**Q7. Difference between BFS and Best First Search?**
BFS expands level-wise; Best First expands lowest heuristic first.

---

# 🎯 Cross-Program Viva Killers (Very Common)

**Q. What is state space?**
All possible configurations of a problem.

**Q. What is a heuristic function?**
A function that estimates how close a state is to the goal.

**Q. What is informed vs uninformed search?**
Uninformed uses no heuristic (BFS, DFS); informed uses heuristic (Best First, A*).

**Q. What is completeness?**
Algorithm guarantees finding a solution if one exists.

**Q. Which is complete — BFS or DFS?**
BFS is complete; DFS is not always.

---