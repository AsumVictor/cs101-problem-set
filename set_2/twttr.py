def main():
    omiited_rsult = ommitVowel(input('Enter a sentence:  '))
    print(omiited_rsult)

def ommitVowel(str):
    vowels = ['a', 'i', 'e', 'o', 'u']
    result = ''
    for char in str:
        if char.lower() in vowels:
            result += ''
        else:
            result += char
    return result


main()
