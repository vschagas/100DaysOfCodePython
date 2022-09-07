height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

result = round(weight / (height **2))

if result <= 18.5:
    print(f"Your BMI is {result} you are underweight. ")
elif result > 18.5 and result <= 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result > 25 and result <= 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result > 30 and result <= 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")