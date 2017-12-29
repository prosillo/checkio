def correct_sentence(text: str) -> str:
    text2 = text.capitalize()
    if text2[-1] is not ".":
       return text2 + "."
    return text2
