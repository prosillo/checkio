def popular_words(text: str, words: list) -> dict:
    text_splitted = text.split()
    text_lower = [x.lower() for x in text_splitted]
    res = {}
    count = 0
    for word in words:
        if word.lower() in text_lower:
            res[word] = text_lower.count(word)
        else:
            res[word] = 0
            print(res)
    return res
    return None


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