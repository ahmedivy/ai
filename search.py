from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graph = {
            "A": [(146, ("A", "O")), (140, ("A", "S")), (494, ("A", "C"))],
            "O": [(146, ("O", "A")), (151, ("O", "S"))],
            "S": [
                (151, ("S", "O")),
                (140, ("S", "A")),
                (80, ("S", "R")),
                (99, ("S", "F")),
            ],
            "C": [(494, ("C", "A")), (146, ("C", "R"))],
            "R": [(80, ("R", "S")), (146, ("R", "C")), (97, ("R", "P"))],
            "F": [(99, ("F", "S")), (211, ("F", "B"))],
            "B": [(211, ("B", "F")), (101, ("B", "P"))],
            "P": [(101, ("P", "B")), (97, ("P", "R")), (138, ("P", "C"))],
        }
        # heuristics for Node B
        self.heristics = {
            "A" : 10,
            "O" : 9,
            "S" : 7,
            "C" : 8,
            "R" : 6,
            "F" : 5,
            "P": 3,
            "B": 0
        }

        self.edges = {}
        self.weights = {}
        self.populate_edges()
        self.populate_weights()

    def populate_edges(self):
        for node, edges in self.graph.items():
            neighbours = [n2 for _, (_, n2) in edges]
            self.edges[node] = neighbours


    def populate_weights(self):
        for node, edges in self.graph.items():
            for cost, edge in edges:
                self.weights[edge] = cost

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]


def ucs(graph: Graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))

    path_track = {start: None}

    while queue.not_empty:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)

            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = path_track[node]
                return path[::-1]


            for n in graph.neighbors(node):
                if n not in visited:
                    total_cost = cost + graph.get_cost(node, n)
                    queue.put((total_cost, n))
                    path_track[n] = node
    return []


def gbfs(graph: Graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    path_track = {start: None}

    while queue.not_empty:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)

            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = path_track[node]
                return path[::-1]

            for n in graph.neighbors(node):
                if n not in visited:
                    total_cost = graph.heristics[n]
                    queue.put((total_cost, n))
                    path_track[n] = node
    return []

def a_star(graph: Graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((graph.heristics[start], (start, 0)))
    path_track = {start: (None, 0)}

    while queue.not_empty:
        _, (node, cost) = queue.get()
        if node not in visited:
            visited.append(node)

            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = path_track[node][0]
                return path[::-1]

            for n in graph.neighbors(node):
                if n not in visited:
                    g_n = cost + graph.get_cost(node, n)
                    prirority = g_n + graph.heristics[n]
                    queue.put((prirority, (n, g_n)))
                    path_track[n] = (node, prirority)
    return []

g = Graph()

print("Edges: ",  g.edges)
print("Weights: ",  g.weights)
print("Heuristics: ", g.heristics)
print("UCS: ", ucs(g, "A", "B"))
print("GBFS: ", gbfs(g, "A", "B"))
print("A*: ", a_star(g, "A", "B"))

