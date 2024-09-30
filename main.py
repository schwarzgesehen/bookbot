def get_book_content(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

def count_words(content):
    count = 0
    words = content.split()
    for word in words:
        count += 1
    return count

def main():
    content = get_book_content("books/frankenstein.txt")
    count = count_words(content)
    print(content)
    print(count)

main()