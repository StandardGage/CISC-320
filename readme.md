## Overview

This Python program is a solution for finding an approximate solution to the Traveling Salesman Problem (TSP), a classic computer science problem. Given a list of cities and the distances between each pair of cities, the TSP seeks the shortest possible route that visits each city exactly once and returns to the origin city.

The program takes a text file as input, which contains a square matrix representing the distances between cities. Each line in the file represents a city, and each number on the line represents the distance to another city. 

The program implements two strategies for solving the problem: the "cheap" method and the "cheap and far" method. The program then finds the optimal path from these two strategies

- The "cheap" method always moves to the nearest unvisited city.
- The "cheap and far" method alternates between moving to the nearest unvisited city and the unvisited city that is farthest from all other cities.

The main function opens the input file, parses the data, applies both methods to find an approximate solution, and prints the path with the lower cost.

## Function Descriptions

- `open_file()`: This function prompts the user to input a filename. It then tries to open the file and read its contents. If the file does not exist, it prints an error message and returns None.

- `parse_items(data)`: This function takes the data from the file and parses it into a 2D list (matrix) of integers, which is used to represent the distances between cities.

- `approx_tsp_cheap(matrix)` and `approx_tsp_cheap_and_far(matrix)`: These functions implement the two strategies for solving the TSP. They start from a vertex, then find the next vertex to visit and add its distance to the total cost. The process is repeated until all vertices have been visited. The functions return the path and its total cost.

- `find_cheapest_vert(vertex, ignore)` and `find_farthest_vert(matrix, ignore)`: These helper functions are used to find the next vertex to visit. They ignore vertices that have already been visited.

- `main()`: This is the main function of the program. It opens the file, parses the data, applies the two methods to find an approximate solution, compares the costs, and prints the cheaper path.

To run the program, call the `main()` function. It will prompt you to enter the name of the file containing the matrix of distances. The program will then print the solution to the console.

Please note that this program provides an approximate solution to the TSP, not the optimal solution. The methods used here are heuristic and aim to find a good solution quickly, rather than the best possible solution.