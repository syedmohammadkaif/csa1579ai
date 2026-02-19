from collections import deque
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True
# Generate next states
def next_states(state):
    m, c, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    states = []
    for mm, cc in moves:
        if boat == 'L':  
            new_m = m - mm
            new_c = c - cc
            new_boat = 'R'
        else:      
            new_m = m + mm
            new_c = c + cc
            new_boat = 'L'
        if is_valid(new_m, new_c):
              states.append((new_m, new_c, new_boat))
    return states
# BFS Search
def solve():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for nxt in next_states(state):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = state
                queue.append(nxt)
    return None
# MAIN
solution = solve()
print("Missionaries and Cannibals Solution:\n")
for step in solution:
    print(step)
