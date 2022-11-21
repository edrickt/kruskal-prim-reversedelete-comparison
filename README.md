# Kruskal, Prim's, and Reverse Delete Algorithm Comparison
Simple program to compare the runtimes of different algorithms to create minimum spanning trees

## Overview
Goal: Demonstrate the time complexity between the classic MST algorithms by using graphs with differing numbers of edges and vertices on 3 different MST algorithms.

Simple implementations may be used.

### Kruskal's Algorithm
While there is not (n-1) edges added, we keep adding
edges in increasing order of weight given that it does not
create cycles.

### Prim's Algorithm
While there is not the minimum amount of edges, keep addin glowest edges adjacent to each node 
added to MST given it doesn't create a cycle.

### Reverse Delete Algorithm
With edges sorted in decreasing order, keep
removing edges until there is (n-1) edges, given
that removing an edge does not disconnect the graph.

## Usage
1. Set working directory to where main.py and helperfunctions.py is located

2. Type "python3 main.py" to run program
