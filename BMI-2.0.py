height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi=round(weight/height**2)
if bmi<18.5:
    print(f"your BMI is {bmi} and you are underweight")
elif bmi<25 :
    print(f"your BMI is {bmi} and you are normal")
elif bmi<30:
    print(f"your BMI is {bmi} and you are overweight")
elif bmi<35:
    print(f"your BMI is {bmi} and you are obese")
else:
    print(f"your BMI is {bmi} and you are clinically obese")
    




 
    