def print_book(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    print(book_contents)
 

def main():
    print_book("books/frankenstein.txt")

if __name__ == '__main__':
    main()
