# Sink\Bathtub program --> If water flow to 90 cm, drain else continue filling sink/tub
"""water_level = float(input("Water level signal."))
if water_level >= 90:
    print("Sink at max, you're wasting water!")
else:
    print("Filling sink")
    
# NYS checker only youths
age = int(input("Enter your age: "))
if age < 18:
    rem_age = int(18 - age)
    print(f"Try again in {rem_age} years.")
elif age <= 35:
    gender = input("You're eligible.\nEnter your Gender.")
    if gender == "male":
        print("Protect life!")
    elif gender == "female":
            print("Nurture life < > \n            .....")
    else:
        print("Invalid!")
elif age> 35:
    print("You are a senior citizen in relation to this operation")    
else:
    print("Invalid")
    
#Even and odd number checker
num = float(input("Enter number to be checked: "))
if num % 2 == 0:
    print("Even number!")
else:
    print("Odd numero!")
    
# BMI 2.0 --> With interpretition
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = (float("{:.3f}".format(weight/height**2)))

if bmi <= 18.5:
    print(f"Your BMI is: {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Normal weight. {bmi}")
elif bmi <= 30:
    print(f"Overweight. {bmi}")
elif bmi <= 35:
    print(f"Obese {bmi}")
else:
    print(f"Clinically obese! {bmi}")

#Leap year checker 
year = int((input("Enter the year you want to check: ")))
if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year.")
elif year % 4 == 0 and year % 400 ==0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year!")
    
#Leap year checker 2.0
if year % 4 ==0:
    if year % 100 = 0:
        if year % 400 = 0:
            print("Leap year!")
        else:
            print("NOt a leap year!")
    else:
        print("Leap year!")
else:
    print("Not a leap year!")"""
    
# Successive if statement --> Rollercoaster with images
height = int(input("Enter the height: "))
bill = 0
if height >= 120:
    #print("You can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 200
        print(f"Child ticket is Kshs {bill}")
    elif age < 18:
        bill = 350
        print(f"Teen ticket is Kshs {bill}")
    elif age <=55 and age >=45:
        print("You have a free ride.")
    else:
        bill = 500
        print(f"Adult ticket is Kshs {bill}")
    wants_photo = input("Do you want a photo? Y or N:  ")
    wants_photos = ['Y','YES','Yes','y','yes','yeah']
    if wants_photo in wants_photos:
        bill += 100 
    
    print(f"Your bill is KShs {bill}")
        
else:
    print("Height limit at 120 cm and above. Sorry.")