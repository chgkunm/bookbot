import sys

from stats import dict_to_list_of_dicts, get_chars_in_book, get_num_words


def main():
    filepath = sys.argv[1]
    number_of_words = get_num_words(filepath)
    book_chars_dict = get_chars_in_book(filepath)
    list_of_dicts = dict_to_list_of_dicts(book_chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for a_dict in list_of_dicts:
        print(f"{a_dict["char"]}: {a_dict["num"]}")
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()
