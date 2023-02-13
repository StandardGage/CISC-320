The program starts by taking input from the user.
This input is the name of the file from which to read.
This process is handled in the openFile function.

The string of text taken from this file is then converted
into a list of integers in the convertToList function.
The function simply splits all newline characters out and uses list comprehension to return the new list of integers.

I then take that list and send it to the getValidSum function. This function first checks if the list is empty and returns 'EMPTY' if it is. Otherwise it takes the first element of the list and runs a for loop for the number in that position. If no valid numbers appear, the list returns 'EMPTY', otherwise it adds up all positive values until the for loop ends, or the loop reads the number -999. The sum is then returned and printed.
