
from typing import List


def openFile(filename: str) -> str:
    """Opens a file and returns its contents as a string of text"""
    with open(filename, 'r') as file:
        text = file.read()
        return text


def parseLogs(text: str) -> str:
    """Parse the logs from a given string of text"""
    if not text:
        # return an empty string if text is empty
        return ''
    text = text.split('\n')
    for i in range(1, len(text)):
        text[i] = text[i].split(' ')
    if len(text) < 2:
        # return an empty string if text holds no valid content
        return ''
    # only return the number of logs specified by the first line of text
    return text[1:int(text[0])+1]


def fillStudents(data: str) -> dict[int, dict]:
    """Fills a dictionary with the given data
    Creates a data structure:\n 
    students = {studentsID: {lowestPageID: None, latestPageID: None, totalScore: 0, scoresSubmitted: 0, averageScore: 0}}.
    \nThen uses the log data to fill in info for each student
    """
    students: dict[int, dict] = {}
    for log in data:
        studentID: int = int(log[0])
        actionCode: str = log[1]
        # setup new student
        if not studentID in students:
            students[studentID] = {'lowestPageID': None,
                                   'latestPageID': None, 'totalScore': 0, 'scoresSubmitted': 0, 'averageScore': 0}
        match actionCode:
            case 'P':
                actionCode == 'P'
                pageID: int = int(log[2])
                setLowestPageID(students, studentID, pageID)
                setLatestPageID(students, studentID, pageID)
            case 'S':
                actionCode == 'S'
                score: int = int(log[2])
                setScore(students, studentID, score)
    return students


def setLowestPageID(students: dict[int, dict], studentID: int, pageID: int):
    """
    Sets the lowest pageID for a given student.
    If the student is missing a lowest pageID it is filled with the parameter
    """
    if students[studentID]['lowestPageID']:
        if pageID < students[studentID]['lowestPageID']:
            students[studentID]['lowestPageID'] = pageID
        return
    students[studentID]['lowestPageID'] = pageID


def setLatestPageID(students: dict[int, dict], studentID: int, pageID: int):
    """Sets the latest pageID to the parameter"""
    students[studentID]['latestPageID'] = pageID


def setScore(students: dict[int, dict], studentID: int, score: int):
    """Sets the totalScore and increases the amount of scores submitted"""
    students[studentID]['totalScore'] += score
    if not students[studentID]['scoresSubmitted']:
        students[studentID]['scoresSubmitted'] = 0
    students[studentID]['scoresSubmitted'] += 1


def sortStudents(students: dict[int, dict]) -> list[int]:
    """Sorts the students in ascending order by their lowestPageID, latestPageID, and then by their averageScore.
    \n Excluding any students missing pages and/or scores."""
    for student in list(students):
        lowestPageID = students[student]['lowestPageID']
        totalScore = students[student]['totalScore']
        scoresSumbitted = students[student]['scoresSubmitted']
        if not (scoresSumbitted and lowestPageID):
            students.pop(student)
            continue
        students[student]['averageScore'] = int(totalScore / scoresSumbitted)
    sortedStudents = sorted(students, key=lambda student: (students[student]['lowestPageID'], students[student]['latestPageID'],
                                                           students[student]['averageScore']))
    return sortedStudents


def printStudents(students, sortedStudents: List[int]):
    """Prints the students by using the id's from the sortedStudents list"""
    for student in sortedStudents:
        lowestPageID = students[student]['lowestPageID']
        latestPageID = students[student]['latestPageID']
        averageScore = students[student]['averageScore']
        print(f'{student} {lowestPageID} {latestPageID} {averageScore}')


def main():
    file: str = input()
    text: str = openFile(file)
    logs: str = parseLogs(text)
    students = fillStudents(logs)
    sortedStudents = sortStudents(students)
    printStudents(students, sortedStudents)


if __name__ == "__main__":
    main()
