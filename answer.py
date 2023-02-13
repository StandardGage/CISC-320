
from typing import List


def openFile(filename: str) -> str:
    with open(filename, 'r') as file:
        text = file.read()
        return text


def convertToList(s: str) -> List[int]:
    if(len(s) == 0):
        return []
    s = s.split("\n")
    return [int(x) for x in s]


def getValidSum(nums: List[int]) -> int:
    if len(nums) == 0:
        return 'EMPTY'
    length = nums[0]
    sum: int = 'EMPTY'
    for i in range(1, length+1):
        if sum == 'EMPTY' and nums[i] >= 0:
            sum = 0
        if nums[i] == -999:
            break
        if nums[i] < 0:
            continue
        sum += nums[i]
    return sum


def main():
    file: str = input()
    text: str = openFile(file)
    nums: List[int] = convertToList(text)
    ret = getValidSum(nums)
    print(ret)


if __name__ == "__main__":
    main()
