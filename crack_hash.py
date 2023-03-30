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
    to check if the hashed word is the password. This method uses python's built-in
    permutations function to find all combinations without repeats and then hashes each combination."""
    for depth_iteration in range(1, depth+1):
        for permutation in permutations(words, depth_iteration):
            hash_word = ''.join(permutation)
            hash = simple_hash(hash_word, hash_code)
            if(hash == 0):
                return hash_word


def hash_words_without_tools(words: str, hash_code: int, depth: int = 1, prev_hash_words=[], level=1):
    """Go through all the permutations for words at a length/depth specified
    to check if the hashed word is the password. This method uses a recursive backtracking algorithm to
    find all combinations with repeats and then hashes each combination. It works by keeping track of the previous
    combinations one level behind, and uses those to build the new level for hashing. If the password is found at any
    moment the recursion is broken out of to value efficiency."""
    if level > depth:
        return None
    if level == 1:
        hash_words = words
        for word in hash_words:
            if simple_hash(word + suffix, hash_code) == 0:
                return word + suffix
    else:
        hash_words = []
        for word in prev_hash_words:
            for suffix in words:
                hash_words.append(word+suffix)
                if simple_hash(word + suffix, hash_code) == 0:
                    return word + suffix
    return hash_words_without_tools(words, hash_code, depth, hash_words, level + 1)


def main():
    HASH_CODE = 81445731
    words = parse_dictionary('crack_tools/dictionary.txt')
    answer = hash_words_without_tools(words, HASH_CODE, depth=4)
    print(answer)


if __name__ == "__main__":
    main()
