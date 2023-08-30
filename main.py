def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    print_book(contents)
    count_words(contents)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def print_book(contents):
    print(contents)
    print("=========")
    print()

def count_words(contents):
    words = contents.split()
    print(f"The book has {len(words)} words")
    print()

main()