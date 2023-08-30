import string

def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    print_book(contents)
    count_words(contents)
    count_letters(contents)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def print_book(contents):
    print(contents)
    print("=========" + "\n")

def count_words(contents):
    words = contents.split()
    print(f"The book has {len(words)} words")
    print("\n" + "=========" + "\n")

def count_letters(contents):
    cont_lowercase = contents.lower()
    alphabet = list(string.ascii_lowercase)
    count_dict = {}
    for letter in alphabet:
        count_dict[letter] = 0
    for letter in cont_lowercase:
        if letter in count_dict:
            count_dict[letter] += 1
    print("The letter counts are:" + "\n")
    print(count_dict)
    print("\n" + "=========" + "\n")   

main()