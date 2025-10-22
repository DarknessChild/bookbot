from stats import get_num_words
from stats import get_letters_count
from stats import sorted_letter_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_location = "books/frankenstein.txt"
    book_text = get_book_text(book_location)
    words = get_num_words(book_text)
    letter_count = get_letters_count(book_text)
    sorted_letters = sorted_letter_count(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
            continue
        else:
            continue

main()