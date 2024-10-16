def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lc = get_text_lc(text)
    word_count = get_word_count(text)
    chr_l = get_chr(text_lc)
    chr_s = set(chr_l)
    chr_count = get_chr_count(chr_l, chr_s)
    chr_count.sort(reverse=True, key=sort_on)
    ltr_count = get_alphabet_count(chr_l, chr_s)
    ltr_count.sort(reverse=True, key=sort_on)

    print(f"- Report of {book_path} -")
    print(f"{word_count} words counted in the document")
    print("")
    for l in range(0, len(ltr_count)):
        print(f"There are {ltr_count[l]['count']} instances of the letter '{ltr_count[l]['letter']}'")
    print("- Close Report -")


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_text_lc(text):
    return text.lower()


def get_chr(text_lc):
    return [*text_lc]


def get_chr_count(chr_l, chr_s):
    return [{"character": x , "count": chr_l.count(x)} for x in chr_s]


def conv_to_list(chr_count):
    return list(dict.items(chr_count))


def sort_on(dict):
    return dict["count"]


def get_alphabet_count(chr_l, chr_s):
    return [{"letter": x , "count": chr_l.count(x)} for x in chr_s if x.isalpha() == True]


main()
