pounds = eval(input("Enter weight in pounds : "))
inches = eval(input("Enter weight in inches : "))

kilograms = pounds * 0.45359237
meters = inches * 0.0245

bmi = round(kilograms / (meters**2), 4)

print("BMI is", bmi)
