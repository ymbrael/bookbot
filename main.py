import sys

from stats import get_word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 
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
    print(f"Found {word_count} total words")
    print("")
    for l in range(0, len(ltr_count)):
        print(f"{ltr_count[l]['letter']}: {ltr_count[l]['count']}")
    print("- Close Report -")


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
