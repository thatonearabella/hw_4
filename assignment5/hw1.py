while True:
    two_words = input("Please enter two words: ")
    
    if two_words.lower() == 'done':
        print("-- bye !!")
        break

    word = two_words.split()
    
    if len(word) == 2:
        word1, word2 = word
        if word1 < word2:
            print(word1, "comes first")
        else:
            print(word2, "comes first")
    elif len(word) == 1:
        pass
