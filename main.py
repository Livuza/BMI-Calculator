# DON'T CHANGE THE CODE BELOW
height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')
# DON'T CHANGE THE CODE ABOVE

##############################################
# Write your code below.
bmi_height=float(height)
bmi_weight=float(weight)
raw_bmi=bmi_weight/(bmi_height**2)
bmi=round(raw_bmi)
print(bmi)

# DON'T CHANGE HE CODE BELOW
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# DON'T CHANGE THE CODE ABOVE

# ----------------------------------------- #
# WRITE YOUR CODE BELOW

bmi = float(weight)/(float(height)**2)

if bmi < 18.5:
    status = "underweight"
if bmi <= 25:
    status = "normal weight"
elif bmi <=30:
    status = "slightly overweight"
elif bmi <=35:
    status = "obese"
else:
    status = "clinically obese"
print(f"Your BMI is {bmi}, you are {status}")