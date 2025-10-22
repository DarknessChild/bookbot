"""Main module for BookBot application."""
import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_letters_count
from stats import sorted_letter_count

def main():
    """Main function to run the BookBot analysis."""
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_location = sys.argv[1]
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

main()
