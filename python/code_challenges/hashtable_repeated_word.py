# from data_structures.hashtable import Hashtable

import re


def first_repeated_word(word):
    pattern = re.compile('[^a-zA-Z ]')
    naked_content = pattern.sub('', word)
    words_to_iterate = naked_content.lower().split()
    temp_set = set()

    for word in words_to_iterate:
        if word in temp_set:
            return word
        else:
            temp_set.add(word)
