# Write a program to calculate BMI and find the status of health

height = float(input('Enter your height in meters : '))

weight = float(input('Enter your weight in kg : '))

bmi = weight / (height * height)

print('Your BMI is', bmi)

if bmi < 18.5:

    print('You are underweight')


elif bmi >=18.5 and bmi <=24.9:

    print('You have a normal weight')


elif bmi >=25 and bmi <=29.9:

    print('You are overweight')


else:

    print('You are obese')