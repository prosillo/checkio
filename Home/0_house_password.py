def checkio(data):
    num = 0
    cap = 0
    low = 0
    if len(data) >= 10:
        for x in data:
            if x.isupper():
                cap += 1
                print(x + " : Caps")
                print(cap)
                continue
            if x.islower():
                low += 1
                print(x + " : Low")
                print(low)
                continue
            if x.isnumeric():
                num += 1
                print(x + " : Num")
                print(num)
                continue
        if (num, cap, low) > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
