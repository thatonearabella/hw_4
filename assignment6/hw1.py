try:
  fileName = input("Enter a file name: ")
  with open(fileName, "r") as f:
    lineNumber = 1
    for line in f:
      print(f"LINE NUMBER : {lineNumber}")
      line.upper
      lineNumber += 1
except FileNotFoundError:
  print("Sorry, there is no such file!")
