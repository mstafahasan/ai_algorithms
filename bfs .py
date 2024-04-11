class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node)

    def get_neighbors(self, node):
        return self.edges[node]

def BFS(graph, startNode, finalNode):
    queue = [startNode]
    visited = set()

    while queue:
        currentNode = queue.pop(0)

        if currentNode not in visited:
            visited.add(currentNode)
            # Process the node (e.g., print, store, etc.)
            print(currentNode)  # For simplicity, we're printing it

            if currentNode == finalNode:
                return visited

            neighbors = graph.get_neighbors(currentNode)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

# Test case
if __name__ == "__main__":
    graph = Graph()

    nodes = list(range(1, 16))  # Nodes from 1 to 15

    for node in nodes:
        graph.add_node(node)

    edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 8), (8, 9), (9, 10), (9, 11), (10, 12), (11, 13), (11, 14), (12, 15)]

    for edge in edges:
        graph.add_edge(*edge)


    start_node = 1
    final_node = 11  
    print(f"Test Case {1}: Start from {start_node} and looking for {final_node}")
    print(BFS(graph, start_node, final_node))
    print("=" * 40)  
