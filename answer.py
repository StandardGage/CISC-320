
from typing import List

students = {}
max_int = 9999999

# students = {studentID: [pageIDs, scores, temps]}


def openFile(filename: str) -> str:
    with open(filename, 'r') as file:
        text = file.read()
        return text


def parseText(text: str):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split(' ')
        id = text[i][0]
        code = text[i][1]
        action = int(text[i][2])
        time = int(text[i][3])
        if code == 'P':
            pageID = action
            students[id] = {'pID': pageID}


def main():
    file: str = "test.txt"
    text: str = openFile(file)
    parseText(text)
    [print(s + s['pid']) for s in students]


if __name__ == "__main__":
    main()
