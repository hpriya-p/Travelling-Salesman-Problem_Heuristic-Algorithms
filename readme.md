Nearest Neighbour and Adjacent Pairwise Exchange Algorithms for the Travelling Salesman Problem
====================================
Description
-----------
The travelling salesman problem (TSP) is an optimization problem in which the least cost circuit that passes through each city exactly once is determined. There are several heuristic and branch-and-bound algorithms that can be used to determine a solution to the travelling salesman problem. Two commonly used heuristic algorithms are the Repeated Nearest Neighbour Algorithm and the Adjacent Pairwise Exchange. 

This python program combines the nearest neighbour algorithm and adjacent pairwise exchange algorithm to determine a heuristic solution to a given TSP. 

Using the Program
-------------------
The file -RNNA_adjacentPairwiseExchange.py- can be run from command prompt/terminal, or from a python editor like Enthought Canopy. The sample TSPs from 'sample TSP data.py' are automatically imported into the program. In order to run the program, call the function 'TSP(matrix, starting_city)'. 'starting_city' is an optional parameter - it is the city that you wish to start in (which may or may not be required, depending on the nature of the problem). Matrix is a tuple, where each element is a list representing a row. 

Input Specifications
--------------------
The input is a tuple whose elements are lists. Each list represents a row in the matrix. The first element of each listis a string, which is the name of the city/node. The rest of the elements in the row are numbers. If there are 'n' lists (or "rows"), there should be exactly 'n+1' elements in each row/list. For example:
'(["a", inf, 200, 1000, 700], ["b",500, inf, 400, 3000], ["c",300, 500, inf, 950], ["d", 900, 400, 700, inf])'
would be a valid input. More examples of valid inputs are provided in 'sample TSP data.py'

More Information
-----------------
The program is also able to handle situations where there is not an edge connecting a particular vertex to every other vertex in the graph. In this case, the program displays how many routes were searched, and returns a heuristic solution. It should be noted, however, that in this case it is possible that the heuristic solution is much larger than the optimal solution as the nearest neighbour algorithm is designed for complete graphs. 
