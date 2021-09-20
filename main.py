"""
Palingram Generator -- Written by Alex Farr

Based on Impractical Python Projects by companyNameHere.
Searches dictionary file in order to first
determine palindromes, and then build them into
palingram sentences after finding them.
"""

import sys


def load(file):
    """Open a text file & return a list of lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.", file=sys.stderr)
        sys.exit(1)


def palindromes():
    word_list = load('res/dict.txt')
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)

    print(f'Number of palindromes found = {len(pali_list)}\n')
    print(*pali_list, sep='\n')


def palingrams():
    """Find all word-pair palingrams in a dictionary file"""
    word_list = load('res/dict_new.txt')
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list


def main():
    pali_out = []
    pali_out = palingrams()
    palingrams_sorted = sorted(pali_out)

    print(f'Number of palingrams = {len(palingrams_sorted)}\n')
    for first, second in palingrams_sorted:
        print(f'{first} {second}')
    sys.exit(0)


if __name__ == '__main__':
    main()
