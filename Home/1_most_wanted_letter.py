def checkio(text: str) -> list:
    text = text.lower()
    result = {}
    for char in text:
        keys = result.keys()
        if char.isalpha():
           if char in keys:
               result[char] += 1
           else:
                result[char] = 1
        else:
            pass
    result = result.items()
    result = min(sorted(max(result, key=lambda x: x[1])[0], reverse=True))
    print(result)
    return result

#max(sorted(max(result, key=lambda x: x[1])[0], reverse=True))

if __name__ == '__main__':
    #print("Example:")
    #print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")