def main():
    book_path = "books/frankenstein.txt"
    print_book(read_book(book_path))

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def print_book(contents):
    print(contents)

main()