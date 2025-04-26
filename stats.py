def sort_on(dict):
    return dict["num"]


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def get_num_words(filepath):
    book_content = get_book_text(filepath)
    book_words = book_content.split()
    total_words = len(book_words)
    return total_words


def get_chars_in_book(filepath):
    book_content = list(get_book_text(filepath).lower())
    chars_in_book = {}
    for a in book_content:
        if a in chars_in_book:
            chars_in_book[a] += 1
        else:
            chars_in_book[a] = 1
    return chars_in_book


def dict_to_list_of_dicts(a_dict):
    new_list = []
    for a_char in a_dict:
        if a_char.isalpha():
            new_list.append({"char": a_char, "num": a_dict[a_char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
