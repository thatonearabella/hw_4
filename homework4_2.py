try:
    input_hours = int(input("Enter hours: "))
    input_rate = float(input("Enter rate: "))
except:
    print("Error, please enter a numeric number!")
    exit()
else:
    def computepay(input_hours, input_rate):
            if input_hours > 40:
                extra_hours = input_hours - 40
                extra_rate = input_rate * 1.5
                salary = (40 * input_rate) + (extra_hours * extra_rate)
                print("Pay: "+str(float(salary)))
            else:
                salary = input_hours * input_rate
                return "Pay: " + str(salary)
                
    computepay(input_hours, input_rate)