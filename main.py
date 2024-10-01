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

def sort_on(dict):
    return dict["count"]

def analyze_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({'char': char, 'count' : count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def main():
    book_path = "books/frankenstein.txt"
    
    content = get_book_content(book_path)
    word_count = count_words(content)
    char_count = count_chars(content)
    
    report = analyze_chars(char_count)

    print(f"--- Report of {book_path} ---")
    print(f"{word_count} words found in document")
    
    for entry in report:
        print(f"The '{entry['char']}' character was found {entry['count']} times") 

    print("--- End report ---")

main()