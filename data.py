def get_words():
    with open("words.txt", 'r', encoding='utf-8') as file:
        words = [row.strip() for row in file]
        return words

get_words()