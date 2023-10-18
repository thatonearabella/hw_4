while True:
    string = input("Please enter a string: ")

    if string.lower() == 'done':
        print("Bye!")
        break

    chars = ',.:!?'  
    for char in chars:
        string = string.replace(char, '')

    string = string.upper()

    print(string)
