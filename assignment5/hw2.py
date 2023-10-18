words = input("Enter string: ")

print("Input string =", words)

length = len(words)
index = length - 1

while index >= 0:
    print(words[index])
    index -= 1
