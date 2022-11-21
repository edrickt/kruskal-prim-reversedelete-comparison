from helperfunctions import *
from graph import Graph

if __name__ == '__main__':
    # While we haven't exited the program, continue getting input from user
    while 1:
        user_input = print_menu()
        print()

        # If user_input is 1, then test Kruskal and Prim's algorithms
        if user_input == "1":
            # From graph with 15 vertices to 300, increments of 15
            for i in range(15, 315, 15):
                kruskal = Graph.test_algorithm(0, i)
                prim = Graph.test_algorithm(1, i)
                print("Vertices        : ", i)
                print_runtimes("Kruskal", kruskal)
                print_runtimes("Prim", prim)
                print()

        # If user_input is 2, then test Kruskal's, Prim's, and reverse delete algorithm
        elif user_input == "2":
            # From graph with 15 vertices to 120 vertices
            for i in range(15, 135, 15):
                kruskal = Graph.test_algorithm(0, i)
                prim = Graph.test_algorithm(1, i)
                reversedelete = Graph.test_algorithm(2, i)

                print("Vertices        : ", i)
                print_runtimes("Kruskal", kruskal)
                print_runtimes("Prim", prim)
                print_runtimes("Reverse Delete", reversedelete)
                print()

        # If user_input is 3, then print how each algorithm's create MST
        elif user_input == "3":
            # All use the GRAPH_EXAMPLE graph from the presentation
            kruskal = Graph(GRAPH_EXAMPLE)
            kruskal.kruskal_mst()

            prim = Graph(GRAPH_EXAMPLE)
            prim.prim_mst()

            reversedelete = Graph(GRAPH_EXAMPLE)
            reversedelete.reversedelete_mst()

            print("Kruskal's Algorithm: ")
            kruskal.print_mst()
            print()
            print("Prim's Algorithm: ")
            prim.print_mst()
            print()
            print("Reverse Delete Algorithm: ")
            reversedelete.print_mst()
            print()

        # If user_input is 4, it allows us to input a graph of size n to get the MST for that
        # random graph and compelete graph
        elif user_input == "4":
            try:
                size = int(input("Graph size: "))
                if size >= 20:
                    kruskal = Graph(create_complete_graph(size, 1))
                    kruskal.kruskal_mst()
                    prim = Graph(create_complete_graph(size, 1))
                    prim.prim_mst()
                    reversedelete = Graph(create_complete_graph(size, 1))
                    reversedelete.reversedelete_mst()

                    print("Kruskal's Algorithm: ")
                    kruskal.print_mst()
                    print("\nPrims's Algorithm: ")
                    prim.print_mst()
                    print("\nReverse Delete Algorithm: ")
                    reversedelete.print_mst()
                    print()
                else:
                    print("Provide input for graph size greater than or")
                    print("equals to 20 to ensure graph full connectivity")
            except:
                print("INVALID INPUT")

        # If user_input is 5, we test graph connectivity
        elif user_input == "5":
            for i in range(10, 315, 5):
                result = Graph.test_graph_connectivity(i)
                print("Vertices count " + str(i).ljust(3) + ": " + str(result))

        # Else if 6, then exit
        elif user_input == "6":
            exit()

        # Elese wrong input
        else:
            print("INVALID INPUT")
