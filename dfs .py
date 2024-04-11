def DFS(graph, startNode, finalNode):
    stack = []
    visited = set()
    stack.append(startNode)

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)

            # Process the node (e.g., print, store, etc.)
            process_node(current_node)

        if current_node == finalNode:
            return visited

        neighbors = graph.get_neighbors(current_node)
        for neighbor in neighbors:
            stack.append(neighbor)