import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
    Perform a breadth-first traversal and pathfinding on the graph.

    * If there's no end node input, return a list of nodes in the order of BFS traversal.
    * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path.
    * If there is an end node input and a path does not exist, return None.

    Args:
        start (str): The starting node for BFS.
        end (str, optional): The end node for shortest path search.

    Returns:
        list or None: BFS traversal order or the shortest path, depending on the input.
    """
    # Initialize the queue with the starting node
        queue = [start]
        visited_nodes = set()  # Set to track visited nodes
        parent_node = {start: None}  # Dictionary to store parent nodes
        traversal_order = []  # List to store traversal order

    # Handle edge cases
        if len(self.graph.nodes) == 0:
            raise ValueError('Graph contains no nodes.')

        if start not in self.graph.nodes:
            raise ValueError('Start node not in Graph.')

        if end is not None and end not in self.graph.nodes:
            raise ValueError('End node not in Graph.')

    # Perform BFS
        while queue:
            current_node = queue.pop(0)  # Dequeue the first node
            visited_nodes.add(current_node)  # Mark as visited
            traversal_order.append(current_node)  # Add to traversal order

        # Check if the current node is the end node
            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent_node[current_node]
                return path[::-1]  # Return the shortest path (reversed)

        # Explore neighbors of the current node
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited_nodes and neighbor not in queue:
                    parent_node[neighbor] = current_node  # Record the parent
                    queue.append(neighbor)  # Enqueue the neighbor

    # If no end node is specified, return the BFS traversal order
        if end is None:
            return traversal_order

    # If an end node is specified but no path exists, return None
        return None
            




