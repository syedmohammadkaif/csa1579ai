import numpy as npdef tsp(cities):
# Create a distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))
for i in range(n):
for j in range(n):
if i != j:
dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])
# Initialize variables
tour = [0]
unvisited_cities = set(range(1, n))
total_distance = 0
# Find the nearest unvisited city and add it to the tour
while unvisited_cities:

SAVEETHA SCHOOL OF ENGINEERING

SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES

39

current_city = tour[-1]
nearest_city = min(unvisited_cities, key=lambda city: dist_matrix[current_city][city])
tour.append(nearest_city)
unvisited_cities.remove(nearest_city)
total_distance += dist_matrix[current_city][nearest_city]
# Complete the tour by returning to the starting city
tour.append(0)
total_distance += dist_matrix[tour[-2]][0]
return tour, total_distance
