from typing import List
from itertools import permutations

from crack_tools.password_hash import simple_hash

# AdaIsGoodDog


def parse_dictionary(file: str) -> List[str]:
    """Parse the dictionary file and fill an array with each word"""
    with open(file, 'r') as dictionary:
        dictionary = dictionary.read().splitlines()
    return dictionary


def hash_words(words: str, hash_code: int, depth: int = 1):
    """Go through all the permutations for words at a length/depth specified
    to check if the hashed word is the password."""
    for depth_iteration in range(1, depth+1):
        for permutation in permutations(words, depth_iteration):
            hash_word = ''.join(permutation)
            hash = simple_hash(hash_word, hash_code)
            if(hash == 0):
                return hash_word

def hash_words_without_tools(words: str, hash_code: int, answer:str = "", depth: int = 1):
    if depth == 0:
        return answer
    for word in words:
        if simple_hash(word, hash_code) == 0:
            answer = word
            return answer


def main():
    HASH_CODE = 81445731
    words = parse_dictionary('crack_tools\dictionary.txt')
    answer = hash_words_without_tools(words, HASH_CODE, 4)
    print(answer)


if __name__ == "__main__":
    main()
