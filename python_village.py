"""
brief
    This file has soultions of problems in python village/ rosalind.com

date
    Sep 2023

author
    Mohamed Ahmed

useage
    python_village.py
"""

import collections

def even_lines(file_name)-> None:
    """Iterate through file and write even line numbers to new_file.txt.

    Args:
        file_name: file name to read from.
    
        Returns:
            None.
    """

    line_number = 0
    with open(file_name, 'r') as file:
        for line in file:
            if line_number%2 == 1:
                new_file = open("new_file.txt", "a")
                new_file.write(line)
                new_file.close()
            line_number +=1

even_lines("rosalind_ini5.txt")

SIMPLE_STR = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

def counting(file_name: str)-> None:
    """Count words which are case-sensitive and save it in dict_str dictionary.

    Args:
        simple_str: A string to be count.

    Returns:
        None.
    """
    with open(file_name, "r") as file:
        words = file.read().split(" ")
    file.close()
    # use collection.counter to count every word in words list
    dict_str = dict(collections.Counter(words))
    for item in dict_str.items():
        print(f"{item[0].strip()} {item[1]}")
counting("rosalind_ini6.txt")
