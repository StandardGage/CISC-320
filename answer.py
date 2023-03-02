
from typing import List

students: dict[int, dict] = {}


def openFile(filename: str) -> str:
    with open(filename, 'r') as file:
        text = file.read()
        return text


def parseLogs(text: str):
    if not text:
        return ''
    text = text.split('\n')
    for i in range(1, len(text)):
        text[i] = text[i].split(' ')
    if len(text) < 2:
        return ''
    return text[1:int(text[0])+1]


def fillStudents(data: str):
    for log in data:
        studentID: int = int(log[0])
        actionCode = log[1]
        if not studentID in students:
            students[studentID] = {'lowestPageID': None,
                                   'latestPageID': None, 'totalScore': 0, 'scoresSubmitted': 0, 'averageScore': 0}
        match actionCode:
            case 'P':
                actionCode == 'P'
                pageID: int = int(log[2])
                setLowestPageID(studentID, pageID)
                setLatestPageID(studentID, pageID)
            case 'S':
                actionCode == 'S'
                score: int = int(log[2])
                setScore(studentID, score)


def setLowestPageID(studentID: int, pageID: int):
    if students[studentID]['lowestPageID']:
        if pageID < students[studentID]['lowestPageID']:
            students[studentID]['lowestPageID'] = pageID
        return
    students[studentID]['lowestPageID'] = pageID


def setLatestPageID(studentID: int, pageID: int):
    students[studentID]['latestPageID'] = pageID


def setScore(studentID: int, score: int):
    students[studentID]['totalScore'] += score
    if not students[studentID]['scoresSubmitted']:
        students[studentID]['scoresSubmitted'] = 0
    students[studentID]['scoresSubmitted'] += 1


def sortStudents():
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


def printStudents(sortedStudents: List[int]):
    for student in sortedStudents:
        lowestPageID = students[student]['lowestPageID']
        latestPageID = students[student]['latestPageID']
        averageScore = students[student]['averageScore']
        print(f'{student} {lowestPageID} {latestPageID} {averageScore}')


def main():
    file: str = input()
    text: str = openFile(file)
    logs: str = parseLogs(text)
    fillStudents(logs)
    sortedStudents = sortStudents()
    printStudents(sortedStudents)


if __name__ == "__main__":
    main()
