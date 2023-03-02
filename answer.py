
from typing import List

students: dict[int, dict] = {}


def openFile(filename: str) -> str:
    with open(filename, 'r') as file:
        text = file.read()
        return text


def parseText(text: str):
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
                setScore(studentID, score)


def setLowestPageID(studentID: int, pageID: int):
    if students[studentID]['lowestPageID']:
        if pageID < students[studentID]['lowestPageID']:
            students[studentID]['lowestPageID'] = pageID
        return
    students[studentID]['lowestPageID'] = pageID


def setLatestPageID(studentID: int, pageID: int):
    if students[studentID]['latestPageID']:
        if pageID > students[studentID]['latestPageID']:
            students[studentID]['latestPageID'] = pageID
        return
    students[studentID]['latestPageID'] = pageID


def setScore(studentID: int, score: int):
    students[studentID]['totalScore'] += score
    if not students[studentID]['scoresSubmitted']:
        students[studentID]['scoresSubmitted'] = 0
    students[studentID]['scoresSubmitted'] += 1


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
    file: str = input()
    text: str = openFile(file)
    text = parseText(text)
    fillStudents(text)
    printStudents()


if __name__ == "__main__":
    main()
