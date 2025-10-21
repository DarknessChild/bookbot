def get_num_words(book_text):    
    word_list = book_text.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")
def get_letters_count(book_text):
    letter_count = {}
    for char in book_text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    print(letter_count)
    return letter_count
def sort_on(letter_count):
    return letter_count.isalpha()["num"]
def sorted_letter_count(letter_count):
        list_of_dicts = []
        for letter in letter_count:
            count = letter_count[letter]
            split_dict ={
                 "char" : letter,
                 "num" : count
                 }
            list_of_dicts.append(split_dict)
        print(list_of_dicts)

