def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(book_text):    
    word_list = book_text.split()
    num_words = len(word_list)
    return(f"Found {num_words} total words")

def get_letters_count(book_text):
    letter_count = {}
    for char in book_text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def sort_on(items):
    return items["num"]

def sorted_letter_count(letter_count):
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

