from collections import deque

def get_states(a, b, maxA, maxB):
    states = []

    # Fill A
    states.append((maxA, b))

    # Fill B
    states.append((a, maxB))

    # Empty A
    states.append((0, b))

    # Empty B
    states.append((a, 0))

    # Pour A -> B
    transfer = min(a, maxB - b)
    states.append((a - transfer, b + transfer))

    # Pour B -> A
    transfer = min(b, maxA - a)
    states.append((a + transfer, b - transfer))

    return states


def water_jug_bfs(maxA, maxB, goals):
    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        a, b = queue.popleft()

        # If current state is any goal
        if (a, b) in goals:
            path = []
            state = (a, b)
            while state:
                path.append(state)
                state = parent[state]
            return path[::-1]

        # Explore neighbors
        for s in get_states(a, b, maxA, maxB):
            if s not in visited:
                visited.add(s)
                parent[s] = (a, b)
                queue.append(s)

    return None


# MAIN
maxA = 4
maxB = 3
goals = {(2, 0)}  # ONLY goal = (2,0)

solution = water_jug_bfs(maxA, maxB, goals)

print("Solution Steps:\n")
for step in solution:
    print(step)
