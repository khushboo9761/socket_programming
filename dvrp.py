def dvrp(num_nodes, routers):
    for i in range(num_nodes):
        for j in range(num_nodes):
            for k in range(num_nodes):
                if routers[j][i] + routers[i][k] < routers[j][k]:
                    routers[j][k] = routers[j][i] + routers[i][k]
    return routers

def print_routing_table(node, routers):
    print("Routing table for node", node)
    print("Node\tCost")
    for i in range(len(routers[node])):
        print(i, "\t", routers[node][i])

def shortest_path(node, routers):
    distances = routers[node]
    visited = [node]
    while len(visited) < len(routers):
        candidates = []
        for i in range(len(distances)):
            if i not in visited:
                candidates.append((distances[i], i))
        cost, nearest = min(candidates)
        visited.append(nearest)
        for i in range(len(distances)):
            new_cost = routers[nearest][i] + cost
            if i not in visited and new_cost < distances[i]:
                distances[i] = new_cost
    return distances

num_nodes = int(input("Enter the number of nodes: "))
routers = []
for i in range(num_nodes):
    row = list(map(int, input(f"Enter costs from node {i} to all other nodes (separated by spaces): ").split()))
    routers.append(row)

routers = dvrp(num_nodes, routers)

for i in range(num_nodes):
    print_routing_table(i, routers)

source_node = int(input("Enter the source node for shortest path calculation: "))
shortest_distances = shortest_path(source_node, routers)

print("Shortest distances from node", source_node)
for i in range(len(shortest_distances)):
    print(f"Node {i}: {shortest_distances[i]}")
