def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height * height)

    if (BMI<18.5):
        print(-1)
    elif (BMI>=18.5 and BMI<=25.0):
        print(0)
    elif (BMI>25.0):
        print(1)
        
    print("BMI = " + str(BMI))

calculate_bmi(height=1.73, weight=57)

