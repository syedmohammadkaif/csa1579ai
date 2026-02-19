import itertools

# Travelling Salesman Problem - Brute Force Approach
def tsp(distance):
    n = len(distance)
    cities = list(range(n))
    start = 0  # starting city

    min_cost = float('inf')
    best_path = None

    # Generate all possible paths (permutations) except the start city
    for perm in itertools.permutations(cities[1:]):
        path = (start,) + perm + (start,)
        cost = 0

        # Calculate the total distance of this path
        for i in range(len(path) - 1):
            cost += distance[path[i]][path[i+1]]

        # Check for minimum cost
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost


# MAIN PROGRAM
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp(distance_matrix)

print("Shortest Path:", path)
print("Minimum Cost:", cost)
