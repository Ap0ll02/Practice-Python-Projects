"""
Finding Palindromes.

Author: Jack Ratermann
Date: May 26, 2024
"""
from termcolor import colored as cc
# pylint: disable=no-member
from project1 import load as ld


word_list = ld("wordlist.txt")
pali_list = []
for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(cc("We Found " + str(len(pali_list)) + " Palindromes!\n", "green"))
print(*pali_list, sep=', ')
