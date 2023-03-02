# What does this program do?

This program is meant to calculate, sort, and report maximum, most recent, and average of a sequence of logs. More specifically it performs these actions on students data. The data is made up of logs containing information on student's page openings, submission scores, as well as body temperature scores.

The program takes the name of a file as its input. This file is meant to be the data or logs that the program will work with.

# How does the program work?

## Parsing logs and Filling students

The program works by opening the inputted file and converting the text within the file to objects which can be handled. Once the file is opened the logs are then parsed and separated so that it is clear what information each log holds. Then each log is taken and used to fill a dictionary where the key is a student's ID. For each student, their ID holds another nested dictionary which contains their lowest page ID, latest page ID, total score, number of score submissions, and finally their average score. Besides the everage score attribute, each field is filled with the log data as it is gone through.

## Sorting

Once all of the log data has been transferred to fill the students dictionary, the process of sorting the students starts.
The students are sorted in ascending order by their lowest page ID, latest page ID, and then average score. Before the actual sorting happens though, each student is checked to make sure that it has at least one page ID and at least one score submission. Any students missing these are deleted from the dictionary. Once only valid students remain, each student is given their average score by dividing their total score by their amount of scores submitted. Finally once each valid student has been given their average score, the students are actually sorted.

## Printing

The next process is rather simple as now that we have a list of ID's sorted by the above requirements, each student is simply printed in order to show its ID, lowest page ID, highest page ID, and average score.

# What is the algorithmic runtime?

To find the algorithmic runtime of this problem we must look at the complexity of each function and how they are called.

1. **openFile** function has a time complexity of O(n), where n is the size of the file, because it reads the entire file and returns it as a string.
2. **parseLogs** function has a time complexity of O(n), where n is the number of lines in the text, because it splits the text into lines and then splits each line into words. The number of iterations in the for loop is n-1.
3. **fillStudents** function has a time complexity of O(L), where L is the number of logs, because it iterates over the log data and fills a dictionary with the given data. The **setLowestPageID**, **setLatestPageID**, and **setScore** functions are called once for each log, and each of those functions has a time complexity of O(1) since they perform constant-time operations.
4. **sortStudents** function has a time complexity of O(s log s), where s is the number of students, because it sorts the students using Python's built-in _sorted_ function, which has a worst-case time complexity of O(n log n). The key function passed to the sorted function is called three times for each student, so its time complexity is O(3n) = O(n).
5. **printStudents** function has a time complexity of O(n), where n is the number of sorted students, because it iterates over the sorted students and prints the data for each student.

## Conclusion

Overall, the time complexity of the main function is dominated by the **sortStudents** function, which has a time complexity of O(s log s) where s is the number of students. It is also important that each log is gone through at a complexity of O(L) where L is the number of logs. Therefore, the overall time complexity of the code is O(s*log*s + L), where s is the number of students and L is the number of logs.
