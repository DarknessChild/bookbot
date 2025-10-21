from stats import get_num_words
from stats import get_letters_count
from stats import sorted_letter_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    get_num_words(book_text)
    letter_count = get_letters_count(book_text)
    sorted_letter_count(letter_count)
main()