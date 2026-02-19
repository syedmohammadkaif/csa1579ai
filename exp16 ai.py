from collections import deque
def bfs(adj_list, start, end):
"""
Perform a breadth-first search in the given graph to find the shortest path
between the start and end nodes.
"""
queue = deque([(start, [start])])
visited = set()
while queue:
node, path = queue.popleft()
if node == end:
return path
if node in visited:
continue

SAVEETHA SCHOOL OF ENGINEERING

SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES

35

visited.add(node)
for neighbor in adj_list[node]:
if neighbor not in visited:
queue.append((neighbor, path + [neighbor]))
return None
if __name__ == '__main__':
graph = {0: [1, 2],
1: [0, 2, 3],
2: [0, 1, 3],
3: [1, 2, 4],
4: [3]}
start_node = 0
end_node = 4
shortest_path = bfs(graph, start_node, end_node)
if shortest_path is not None:
print(f"The shortest path between {start_node} and {end_node} is {shortest_path}")
else:
print(f"There is no path between {start_node} and {end_node}")
