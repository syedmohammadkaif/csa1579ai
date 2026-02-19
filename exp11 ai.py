# Map Coloring CSP using Backtracking

def is_valid(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def csp_backtracking(regions, colors, neighbors, assignment={}):
    # If all regions assigned → return solution
    if len(assignment) == len(regions):
        return assignment

    # Select unassigned region
    unassigned = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment, neighbors):
            assignment[unassigned] = color

            result = csp_backtracking(regions, colors, neighbors, assignment)
            if result:
                return result

            # Backtrack
            del assignment[unassigned]

    return None


# MAIN PROGRAM
regions = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['Red', 'Green', 'Blue']

# Adjacency constraints (example map)
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

solution = csp_backtracking(regions, colors, neighbors)

print("Map Coloring Solution:\n")
for region, color in solution.items():
    print(region, "→", color)
