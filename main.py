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
    print(f"The file has {len(words)} words." + "\n")

def count_letters(contents):
    cont_lowercase = contents.lower()
    alphabet = list(string.ascii_lowercase)
    count_dict = {}
    for letter in alphabet:
        count_dict[letter] = 0
    for letter in cont_lowercase:
        if letter in count_dict:
            count_dict[letter] += 1
    sorted_counts = dict(sorted(count_dict.items(), key=lambda x:x[1], reverse=True))
    print("The letter counts are:" + "\n")
    #print(sorted_counts)
    for letter in sorted_counts:
        print(f"{letter} : {sorted_counts[letter]}")
    print("\n" + "=========" + "\n")   

main()