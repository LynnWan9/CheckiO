def popular_words(text: str, words: list) -> dict:
    text = text.lower() # convert all uppercase letters to lowercase letters
    splitted_words = text.split() # break the text into single words
    counter = {} # create an empty dictionary to store words and # times each word occurs
    for word in words:
        counter[word] = splitted_words.count(word) # count # times each word occurs 
    return counter


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
