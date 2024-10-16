def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lc = get_text_lc(text)
    word_count = get_word_count(text)
    print(f"{word_count} words counted in {book_path}")
    letters_l = get_letters(text_lc)
    letters_s = set(letters_l)
    letter_count = get_letter_count(letters_l, letters_s)
    print(letter_count)


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_text_lc(text):
    return text.lower()


def get_letters(text_lc):
    return [*text_lc]


def get_letter_count(letters_l, letters_s):
    return {x:letters_l.count(x) for x in letters_s}


main()
