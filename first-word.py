import string

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    #new_text = ''
    text2 = text.split()
    if ',' in text2[0]: return text2[0].replace(',' , '')
    if '.' in text2[0]: return text2[]
    if text2[0].isspace(): return text2[1]
    #elif ',' in text2[0]:
     #   return text2[0].replace(',' , '')
    #elif '.' in text2[0]:
        #text2[0].replace('.' , '')
     #   return text2[1]
    else:
        return text2[0]
        #for char in text2[0]:
         #   if char.isspace():
        #       return new_text
         #   else:
          #      new_text += char


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
