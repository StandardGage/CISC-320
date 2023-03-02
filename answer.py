
from typing import List

students: dict = {}


def openFile(filename: str) -> str:
    with open(filename, 'r') as file:
        text = file.read()
        return text


def parseText(text: str):
    text = text.split('\n')
    for i in range(1, len(text)):
        text[i] = text[i].split(' ')
    return text[1:]


def fillStudents(data: str):
    for log in data:
        studentID: int = int(log[0])
        actionCode = log[1]
        if not studentID in students:
            students[studentID] = {'lowestPageID': None,
                                   'latestPageID': None, 'totalScore': 0, 'scoresSubmitted': None}
        match actionCode:
            case 'P':
                actionCode == 'P'
                pageID: int = int(log[2])
                setLowestPageID(studentID, pageID)
                setLatestPageID(studentID, pageID)
            case 'S':
                actionCode == 'S'
                score: int = int(log[2])
                students[studentID]['totalScore'] += score
                if not students[studentID]['scoresSubmitted']:
                    students[studentID]['scoresSubmitted'] = 0
                students[studentID]['scoresSubmitted'] += 1


def setLowestPageID(studentID: int, pageID: str):
    if students[studentID]['lowestPageID']:
        if pageID < students[studentID]['lowestPageID']:
            students[studentID['lowestPageID']] = pageID
        return
    students[studentID]['lowestPageID'] = pageID


def setLatestPageID(studentID: int, pageID: str):
    if students[studentID]['latestPageID']:
        if pageID > students[studentID]['latestPageID']:
            students[studentID]['latestPageID'] = pageID
        return
    students[studentID]['latestPageID'] = pageID


def printStudents():
    for student in students.keys():
        lowestPageID = students[student]['lowestPageID']
        latestPageID = students[student]['latestPageID']
        totalScore = students[student]['totalScore']
        scoresSumbitted = students[student]['scoresSubmitted']
        if not (scoresSumbitted and lowestPageID):
            continue
        averageScore = int(totalScore / scoresSumbitted)

        print(f"{student} {lowestPageID} {latestPageID} {averageScore}")


def main():
    file: str = 'test.txt'
    text: str = openFile(file)
    if not text:
        return
    text = parseText(text)
    fillStudents(text)
    printStudents()


if __name__ == "__main__":
    main()
