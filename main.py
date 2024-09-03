def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    get_words = word_count(text)
    get_letters = letter_count(text)
    dict_list = dict_to_list(get_letters)
    sorted_dict = sort_dict(dict_list)
    print(f"--Begin report of {book_path}--")
    print(f"{get_words} words were found in the text\n")
    for item in sorted_dict:
        for value in item.keys():
            print(f"{value} letter was found {item[value]} times")
    print(f"--End report of {book_path}--")

def get_text(path):
    with open(path, "r", encoding="utf-8") as text:
        return text.read()

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters = {}
    for letter in text:
        lowercase = letter.lower()
        alphabet = lowercase.isalpha()
        if lowercase in letters and alphabet is True:
            letters[lowercase] += 1
        elif alphabet is False:
            pass
        else:
            letters[lowercase] = 1
    return letters

def dict_to_list(dict):
    dict_list = [{i: value} for i, value in dict.items()]
    return dict_list

def sort_dict(dict):
    sorted_dict_list = sorted(dict, key=lambda x: list(x.values()), reverse=True)
    return sorted_dict_list

main()