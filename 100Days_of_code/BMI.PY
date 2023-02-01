#BMI Calculator
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = round((weight/height**2),2)
# bmi_as_int = int(BMI)
# bmi =str(bmi_as_int)
print(f"Your BMI is: {BMI} ")