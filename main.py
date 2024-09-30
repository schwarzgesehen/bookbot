def get_book_content(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

def count_words(content):
    words = content.split()
    return len(words)

def count_chars(content):
    char_count = {}

    for char in content.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1 
    
    return char_count

def main():
    content = get_book_content("books/frankenstein.txt")
    word_count = count_words(content)
    char_count = count_chars(content)

    #print(content)
    #print(word_count)
    print(char_count)

main()