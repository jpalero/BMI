def BMI(height, weight):
    while True:
        BMI = weight / pow(height, 2)
        return BMI

def check_input(input):
    while True:
        try:
            # Check the value if float.
            float(input)
        except:
            # If the value is not float or user input a string.
            print('Please use numeric digits.')
            break
        return check_input
    

while True:
    try:
        # for height example you're 172 then input 1.72
        Height = input("Enter your height(cm): ")
        check_input(Height)

        Weight = input("Enter your weight(kg): ")
        check_input(Weight)

        # Call a function BMI then the value of Height and Weight converted into Float
        totalBMI = BMI(float(Height),float(Weight))
        print("%.2f" % totalBMI)

        if totalBMI <= 18.5:
            print("You're underweight!!")
        elif totalBMI >= 18.6 and totalBMI <= 24.9:
            print("You're normal...")
        elif totalBMI >= 25.0 and totalBMI <= 29.9:
            print("You're overweight!!")
        elif totalBMI >= 30.0:
            print("You're obese!!")
        else:
            print("Invalid BMI!!")
        break

    except:
        print("Can't continue!.")
        break




