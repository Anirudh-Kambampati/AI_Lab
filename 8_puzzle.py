import heapq
#goal state
GOAL_STATE=[
    [1,2,3],
    [4,5,6],
    [7,8,0]
]
MOVES=[(-1,0), (1,0), (0,-1), (0,1)]
def heuristic(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=GOAL_STATE[i][j]:
                count+=1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def generate_states(state):
    x,y=find_blank(state)
    children=[]
    for dx,dy in MOVES:
        nx,ny=x+dx, y+dy
        
        if 0<=nx<3 and 0<=ny<3:
            new_state=[row[:] for row in state]
            new_state[x][y], new_state[nx][ny]=new_state[nx][ny],new_state[x][y]
            children.append(new_state)
    return children

def best_first_search(start_state):
    visited=set()
    pq=[]
    heapq.heappush(pq,(heuristic(start_state),start_state))
    while pq:
        h, current=heapq.heappop(pq)
        state_tuple=tuple(map(tuple,current))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)


        if current == GOAL_STATE:
            print("Goal state reached")
            return
        
        print("\n Current State (h= ",h,"):")
        for row in current:
            print(row)
        for child in generate_states(current):
            child_tuple = tuple(map(tuple,child))
            if child_tuple not in visited:
                heapq.heappush(pq, (heuristic(child),child))
    print("\n Goal state not found")

if __name__ == "__main__":
    start_state = [
        [1,3,0],
        [4,2,6],
        [7,5,8]
    ]
    best_first_search(start_state)