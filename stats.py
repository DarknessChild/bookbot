"""Module for analyzing text statistics of a book."""
def get_book_text(filepath):
    """Reads in the book text from the given filepath and returns it as a string."""
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_num_words(book_text):
    """Returns the number of words in the book text."""
    word_list = book_text.split()
    num_words = len(word_list)
    return f"Found {num_words} total words"

def get_letters_count(book_text):
    """Returns a dictionary with the count of each letter in the book text."""
    letter_count = {}
    for char in book_text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def sort_on(items):
    """Sorts the items in the list of dictionaries based on the 'num' key."""
    return items["num"]

def sorted_letter_count(letter_count):
    """Returns a sorted list of dictionaries from the letter count dictionary."""
    list_of_dicts = []
    for letter in letter_count:
        count = letter_count[letter]
        split_dict ={
                "char" : letter,
                "num" : count
                }
        list_of_dicts.append(split_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
