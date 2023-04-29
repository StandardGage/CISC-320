# What does this program do?

This program is meant to solve the knapsack problem, which aims to find the optimal set of items to include in a knapsack with a limited weight capacity. Each item has a specific weight and value, and the objective is to maximize the total value of the selected items without exceeding the knapsack`s weight capacity.

It consists of the following functions

1. `parse_items(data)`: This function reads the input data, which consists of the total number of items, the knapsack's capacity, and the items' names, weights, and values. The function returns the total_items, capacity, and a list of the items themselves

2. `find_optimal_subset(items, total_items, capacity)`: This function uses dynamic programming to find the optimal set of items that maximize the total value while staying within the weight capacity. It returns the optimal set of items and the total value of the selected items.

3. `main()`: This function reads the input file, calls the parse_items() function to process the input, and then calls the find_optimal_subset() function to find the optimal set of items. It prints the sorted list of items and the optimal set of items with their total value.

# What is the time complexity?

The function which dominates that the overall program's time complexity will be is the `find_optimal_subset` function. Therefore, we will focus on that. The function is O(nW) where n is the total_items and W is the capacity. This is because the function uses dynamic programming to solve the knapsack problem, and it iterates through all the items and all possible capacities from 1 to the given capacity.

The nested loops in the function are what contribute to this time complexity

- The outer loop iterates through each item, resulting in O(total_items) complexity.

- The inner loop iterates through each capacity value from 1 to the given capacity, resulting in O(capacity) complexity.

Since these loops are nested, their complexities are multiplied, giving the overall time complexity of O(total_items \* capacity) or O(nW).

# What is the worst case scenario?

In the worst-case scenario, the program's time complexity is still dominated by the `find_optimal_subset` function, as it has the highest time complexity among all functions in the program.

As previously mentioned, the time complexity of the `find_optimal_subset` function is O(total_items \* capacity) or O(nW) due to the nested loops iterating through all items and all possible capacities from 1 to the given capacity.

# What is the space complexity?

The program's space complexity is also dominated by the `find_optimal_subset` function, as it creates a dynamic programming table of dimensions (total_items + 1) x (capacity + 1). Therefore, the worst-case space complexity of the program is once again O(total_items \* capacity) or O(nW).
