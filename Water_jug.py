from collections import deque

def water_jug_bfs(jug1, jug2, goal):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (a, b), path = queue.popleft()

        if a == goal or b == goal:
            print("\nSolution Found:\n")
            for state in path:
                print(state)
            print(f"\nFinal State: (Jug1 = {a}, Jug2 = {b})")
            return

        next_states = [
            (jug1, b),                    
            (a, jug2),                      
            (0, b),                         
            (a, 0),                        
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  
            (a + min(b, jug1 - a), b - min(b, jug1 - a))   
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution found")


jug1 = int(input("Enter capacity of jug1: "))
jug2 = int(input("Enter capacity of jug2: "))
goal = int(input("Enter goal amount: "))

water_jug_bfs(jug1, jug2, goal)