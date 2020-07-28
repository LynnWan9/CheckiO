def checkio(words: str) -> bool:
    count = 0 # initialize a counter
    for i in words.split(): # split the words
        if i.isalpha(): # if the element is a word
            count += 1  # then count up
        else: # if the element is not a word
            count = 0  # then reset the counter
        if count == 3: # once the counter reaches our target (3)
            return True  # returns True
    return False # otherwise returns False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
