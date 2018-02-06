def extractVowel(word):


    vowel=['a','e','i','o','u','A','E','I','O','U']
    newWord=""
    for letter in word:
        if letter not in vowel:
            newWord+=letter
            # print(letter)
    # print(newWord)
    return newWord

# word.replace(vowel,"")

if __name__ == '__main__':
    pass
    word=input("Enter your string")
    print(extractVowel(word))