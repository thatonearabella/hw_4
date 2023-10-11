try:
    input_sc = int(input("Enter score: "))
except:
    print("Error, please enter numbers between 0 and 100")
    exit()
else:
    def func(input_sc):
            if input_sc > 100 or input_sc < 0:
                print("Error, please enter numbers between 0 and 100")
            elif input_sc >= 90:
                print("Grade is A")
            elif input_sc >= 80:
                print("Grade is B")
            elif input_sc >= 70:
                print("Grade is C")
            elif input_sc >= 60:
                print("Grade is D")
            else:
                print("Grade is F")

    func(input_sc)