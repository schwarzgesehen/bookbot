def get_book_content(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

def count_words(content):
    words = content.split()
    return len(words)

def main():
    content = get_book_content("books/frankenstein.txt")
    count = count_words(content)
    print(content)
    print(count)

main()