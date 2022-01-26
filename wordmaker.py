#!/usr/bin/python3
# This program aims to make novel words out of a list of characters
# Note the output of this program can be piped to grep to find regular expressions in scrambled sentences
# for example: $ ./wordmaker.py -w "russia" -c 15 | grep -i "sar"


import argparse
import os
import random
from colorama import Fore


RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RESET = Fore.RESET


def mix_letters(letters_list) -> str:
    for _ in range(0, len(letters_list)):
        switch_partner_one_index = random.randint(0, (len(letters_list)-1))
        switch_partner_two_index = random.randint(0, (len(letters_list)-1))
        switch_letter_temporary_variable = letters_list[switch_partner_one_index]
        letters_list[switch_partner_one_index] = letters_list[switch_partner_two_index]
        letters_list[switch_partner_two_index] = switch_letter_temporary_variable    
    return letters_list


def main() -> None:    
    # supply the characters to use in an argument to the program
    parser = argparse.ArgumentParser(description="Aims to make novel words out of supplied letters")

    args = parser.add_argument("-w", "--word", help="subject word", type=str, default="example")
    args = parser.add_argument("-c", "--count", help="number of words to be returned", type=int, default=15)

    args = parser.parse_args()

    subject_word = args.word

    subject_letter_list = []

    for letter in subject_word:
        subject_letter_list.append(letter)
    print(f"{YELLOW}Letters{RESET}: {subject_letter_list}")

    print(f"\n{GREEN}Scrambled results list{RESET}:")
    for _ in range(args.count):
        for letter in mix_letters(subject_letter_list):
            print(f"{letter}", end="")
        print("")



if __name__=='__main__':
    main()