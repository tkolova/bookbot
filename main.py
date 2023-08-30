def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    print(contents)
    

def read_book(book_path):
    #file_contents = None
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()