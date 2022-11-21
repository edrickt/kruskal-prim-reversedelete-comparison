import random
# Max edge value
MAX_VALUE = 1000
# Graph from powerpoint presentation
GRAPH_EXAMPLE = [["x", 3, "x", 7, "x"],
                [  3, "x", 4,  9,  5],
                [ "x", 4, "x", 1,  8],
                [  7,  9,  1, "x", 10],
                [ "x", 5,  8,  10,"x"]]

# Edge object that has i->j with weight attributes
class Edge:
    def __init__(self, i, j, weight):
        self.i = i
        self.j = j
        self.weight = weight

# Disjoint set object that allows us to find parent and union sets
class DisjointSet:
    def __init__(self, n):
        self.set = [-1 for i in range(n)]
        self.n = n

    def find(self, n):
        while self.set[n] >= 0:
            n = self.set[n]
        return n

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        self.set[i] = j

# Get the edge weights of graphs in sorted order
def get_edge_weights(graph):
    n = len(graph)
    edges = []
    # For all vertices
    for i in range(n):
        # For j in range i+1 to get upper triangle
        for j in range(i+1):
            # If i and j are connected, append to edge_arr
            if graph[i][j] != "x":
                edges.append(Edge(i, j, graph[i][j]))
    # Sort and return
    edges.sort(key=lambda x: x.weight)
    return edges

# Function to create a complete graph
def create_complete_graph(n, seed):
    # Set seed
    random.seed(seed)
    graph = []
    # For how many vertices, create a subarray to create an adjacency matrix
    for i in range(n):
        # Temp array to append to the original adjacency matrix
        temp = []
        for j in range(n):
            # If we are on the lower triangle, then just append what is in the upper triangle
            if j < i:
                temp.append(graph[j][i])
            # Else append a new random value
            else:
                temp.append(random.randrange(1, MAX_VALUE))
        # Set diagonal as "x", no edge to same vertices
        temp[i] = "x"
        # Append to graph to create matrix
        graph.append(temp)
    # Return
    return graph

# Same as above function but will have a change to not add an edge between two vertices
def create_random_graph(n, seed):
    random.seed(seed)
    graph = []
    for i in range(n):
        temp = []
        for j in range(n):
            val = random.randrange(1, MAX_VALUE)
            # If the value below half of the MAX_VALUE then don't add an edge
            # This simulates a probability of having an edge existing at 0.5
            if val < MAX_VALUE/2:
                val = "x"
            if j < i:
                temp.append(graph[j][i])
            else:
                temp.append(val)
        temp[i] = "x"
        graph.append(temp)
    return graph

# Print the graph used for testing
def print_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            val = str(graph[i][j])
            print(val.ljust(3), end=" ")
        print()
    print()

# Print menu and get user input, return user input
def print_menu():
    print("------------------------MENU------------------------")
    print("1: Compare Kruskal's algorithm and Prim's algorithm")
    print("2: Small graph test with Reverse Delete algorithm")
    print("3: Demonstrate algorithm with sample graph")
    print("4: Test algorithms with size n complete graph")
    print("5: Test random graph connectivity")
    print("6: Exit")
    user_input = input(">> ")
    return user_input

# Print runtimes. We pass string for algorithm, as well as runtime list
def print_runtimes(algorithm, runtime):
    print(" ", algorithm.ljust(14), "-----------------------------")
    print("    Random      : ", runtime[0], " Nanoseconds")
    print("    Complete    : ", runtime[1], " Nanoseconds")
