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