from collections import defaultdict

# ---------- The graph ----------
# node -> set of edges leaving that node.
# An edge is a tuple: (relationship, other_node).
# defaultdict(set) means nodes spring into existence on first touch --
# no need to pre-declare Alice, Steve, and Bob.
# The set makes edges unique on the whole (relationship, neighbor) pair:
# adding the same friendship twice is a no-op, but "friend" and
# "coworker" edges to the same person can coexist.

graph = defaultdict(set) 
# { 
#   Alice: [ (friend, Bob) ],
#   Bob: [ (friend, Alice), (friend, Steve) ],
#   Steve: [ (friend, Bob) ]
# }

def add_edge(a, b, relationship):
    graph[a].add((relationship, b))
    graph[b].add((relationship, a))  # friendship goes both ways

add_edge("Alice", "Bob", "friend")
add_edge("Bob", "Alice", "friend")

add_edge("Bob", "Steve", "friend")
add_edge("Steve", "Bob", "friend")


# print("The graph in memory:")
# for node, edges in graph.items():
    # print(f"  {node}: {edges}")

def is_connection(node_1, node_2, edge) -> bool:
    if (edge, node_2) in graph.get(node_1):
        print("direct connection")
        return True
        e
    nodes_searched = []
    for (relationship, name) in graph[node_1]:
        print(relationship, name)
        if (edge, node_2) in graph.get(name):
            print("connection through: ", name)


is_connection("Alice", "Steve", "friend")
    

def find_path(start_node, target_node, edge):
    start_node_links = graph.get(start_node)
    print(start_node_links)
    print(type(start_node_links))
    if (edge, target_node) in start_node_links:
        print("direct connection")
    


# find_path("Bob", "Steve", "friend")


# ---------- The search ----------
# "Are start and goal connected through this relationship?"
# Walk the edges outward from start. Remember how we reached each
# node (breadcrumbs). If we ever land on goal, follow the
# breadcrumbs backwards to produce the path.

# def find_path(start, goal, relationship):
#     to_visit = [start]            # nodes discovered but not explored yet
#     reached_from = {start: None}  # breadcrumbs: node -> the node we came from

#     while to_visit:
#         current = to_visit.pop(0)

#         if current == goal:
#             # Found it. Walk breadcrumbs backwards: Bob -> Steve -> Alice
#             path = []
#             while current is not None:
#                 path.append(current)
#                 current = reached_from[current]
#             path.reverse()
#             return path

#         for rel, neighbor in graph[current]:
#             if rel == relationship and neighbor not in reached_from:
#                 reached_from[neighbor] = current
#                 to_visit.append(neighbor)

#     return None  # explored everything reachable, never hit goal

# # ---------- Run it ----------
# print()
# path = find_path("Alice", "Bob", "friend")
# if path:
#     print(f"Yes, Alice and Bob are connected: {' -> '.join(path)}")
# else:
#     print("No, Alice and Bob are not connected.")
