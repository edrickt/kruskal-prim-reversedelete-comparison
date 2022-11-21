from helperfunctions import *
from time import perf_counter_ns
# Number of loops we put test the algorithms in
ITERATIONS = 5

# Graph class that allows us to create a MST using 3 different algorithms. Prim's algorithm, Kruskal's algorithm,
# and the Reverse Delete algorithm.
class Graph:
    def __init__(self, graph=None):
        # Where we store MST
        self.mst = []
        # Make passed in graph as object's graph
        self.graph = graph
        # Don't get edge array if we don't pass in graph. Used if we just want to use DFS to test connectivity
        if self.graph is not None:
            self.edge_arr = get_edge_weights(graph)

    # Create an MST using Kruskal's algorithm
    def kruskal_mst(self):
        # Clear MST sine we might put kruskal_mst() in a loop. Creates a new MST everytime within that loop
        # instead of just appending to it
        self.mst = []
        # Copy graph and edge_arr so we don't change values at that memory address
        graph = self.graph.copy()
        edge_arr = self.edge_arr.copy()
        # Start timer
        start = perf_counter_ns()

        # Create disjoint_set to hold nodes
        disjoint_set = DisjointSet(len(graph))
        # Edge counter
        edges = 0

        # While we don't have minimum amount of edges to connect graph, keep going
        while edges < len(graph) - 1:
            # Get lowest edge weight
            cur_edge = edge_arr.pop(0)
            # i -> j with weight
            i = disjoint_set.find(cur_edge.i)
            j = disjoint_set.find(cur_edge.j)
            # If they don't share the same parent node, then union, add to MST, increment edge counter
            if i != j:
                self.mst.append(cur_edge)
                disjoint_set.union(i, j)
                edges += 1

        # Return total time it took to run algorithm
        return perf_counter_ns() - start

    # Create an MST using Prim's algorithm
    def prim_mst(self):
        # Clear MST so we can put function in loop and it doesn't just append after each time we
        # run it
        self.mst = []
        graph = self.graph.copy()
        # Start timer
        start = perf_counter_ns()

        # Create a processed edge array so we know which vertices we have processed
        processed_edges = [False for i in range(len(graph))]
        # Start from the first Node
        processed_edges[0] = True
        # Begin with 0 edges added to MST
        edges = 0

        # While we don't have the minimum number of edges in the MST, keep going
        while edges < len(graph) - 1:
            # Set the minimum weight to something larger than max weight in our graph
            # We do this since we will update the minweight anyways to the first edge weight we find since
            # our edge weight will be less than 99999999
            minweight = 99999999
            # Variables so we can get the vertices from the for loop
            u, v = 0, 0
            # For all edges in graph
            for i in range(len(graph)):
                # For all edges that are processed
                if processed_edges[i] is True:
                    # Find the minimum weight to the next vertices that are not yet added to the MST
                    for j in range(len(graph)):
                        # If it is not yet added, and it is connected
                        if processed_edges[j] is False and graph[i][j] != "x":
                            # If we find a new minweight, then update that and keep iterating to find a new
                            # potential min edge weight
                            if minweight > graph[i][j]:
                                minweight = graph[i][j]
                                u, v = i, j
            # Append new edge to the MST and make the new node that we connected to be added to the MST
            self.mst.append(Edge(u, v, graph[u][v]))
            processed_edges[v] = True
            # Increment edge
            edges += 1

        # Return elapsed time
        return perf_counter_ns() - start

    # Create an MST using reverse delete method
    def reversedelete_mst(self):
        # Clear MST and copy the graph and edge_arr
        self.mst = []
        graph = self.graph.copy()
        edge_arr = self.edge_arr.copy()
        # Start timer
        start = perf_counter_ns()

        # Start with max number of edges in "MST"
        edges = len(edge_arr)

        # While we don't have the minimum number of edges in the MST, then keep removing edges from graph
        while edges > len(graph) - 1:
            # Get highest weight edge
            cur_edge = edge_arr.pop(-1)
            i = cur_edge.i
            j = cur_edge.j

            # Remove edge from graph
            graph[i][j], graph[j][i] = "x", "x"

            # Perform DFS on the graph to see if all nodes are visited. Will return an array with sum
            # 0 if all nodes are visited
            visited = [1 for i in range(len(graph))]
            self.dfs(graph, 0, visited)

            # If the sum of the array is greater than 0, then that means not all nodes are visited, so we
            # add the edge back into the graph
            if sum(visited) > 0:
                graph[i][j], graph[j][i] = cur_edge.weight, cur_edge.weight
            # Else, we remove an edge from the graph, go until we have n-1 edges
            else:
                edges -= 1

        # Get the remaining edges in the graph to create an MST
        self.mst = get_edge_weights(graph)

        # Return elapsed time
        return perf_counter_ns() - start

    # Depth first search on graph with adjacency matrix representation
    def dfs(self, graph, vertex, visited):
        # Set vertex as visited
        visited[vertex] = 0
        # For all edges from node vertex to node j that we haven't visited, then call depth first search
        # on that node to search through that
        for j in range(len(graph)):
            if graph[vertex][j] != "x" and visited[j] == 1:
                self.dfs(graph, j, visited)

    # Print the MST along with the minimum weight
    def print_mst(self):
        minweight = 0
        for i in self.mst:
            print(str(i.i).rjust(3), "->", str(i.j).ljust(3), i.weight)
            minweight += i.weight
        print("Minimum weight:", minweight)

    # Method to test graph connectivity with respect to number of vertices for random graphs
    @staticmethod
    def test_graph_connectivity(n):
        # New Graph object so we can use dfs
        dfs = Graph()
        # For how many iterations we use in our tests, create that number of random and complete graphs
        for i in range(ITERATIONS):
            # Create random graph of size n with seed i+1, same graphs we use for our tests
            graph = create_random_graph(n, i+1)
            # Set visited array
            visited = [1 for vertex in range(len(graph))]
            # Perform dfs on the graph
            dfs.dfs(graph, 0, visited)
            # If we didn't visit all nodes in one of the random graphs, return false
            if sum(visited) > 0:
                return False
        # Else return true
        return True

    # Function that we use to test algorithms
    # Specify which algorithm we want to use, as well as the size of the graphs
    @staticmethod
    def test_algorithm(algorithm, size):
        # Create a random and complete graph array
        random_graph_arr, complete_graph_arr = [], []
        # Create graphs and put into respective array
        for i in range(ITERATIONS):
            random_graph_arr.append(create_random_graph(size, i+1))
            complete_graph_arr.append(create_complete_graph(size, i+1))

        # Elapsed time accumulator for random and complete graphs
        random_time = 0
        complete_time = 0
        for i in range(ITERATIONS):
            # New graph objects, pass in graph i from random and complete graph arrays
            random_mst = Graph(random_graph_arr[i])
            complete_mst = Graph(complete_graph_arr[i])
            # If we set option 0, we use Kruskal's algorithm
            if algorithm == 0:
                # Add elapsed time to respective accumulators
                random_time += random_mst.kruskal_mst()
                complete_time += complete_mst.kruskal_mst()
            # If we set algorithm to 1, we use Prim's algorithm
            elif algorithm == 1:
                random_time += random_mst.prim_mst()
                complete_time += complete_mst.prim_mst()
            # Else we just use reverse delete algorithm
            else:
                random_time += random_mst.reversedelete_mst()
                complete_time += complete_mst.reversedelete_mst()
        # Return the elapsed time divided by number of iterations to get average time
        return [random_time/ITERATIONS, complete_time/ITERATIONS]
        