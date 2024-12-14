print("\n--- welcome to BMI calculator ---")

weight = int(input("Enter your weight: "))
height = float(input("Enter your height (in meters): "))
height_squared = height * height
result = weight / height_squared
print("Your BMI is:", result)
if result < 18.5:
    print("You are underweight.")
elif 18.5 <= result <= 24.9:
    print("You have a normal weight.")
elif 25 <= result <= 29.9:
    print("You are overweight.")
elif 30 <= result <= 34.9:
    print("You are obese (Class 1).")
elif 35 <= result <= 39.9:
    print("You are obese (Class 2).")
else:
    print("You are severely obese (Class 3).")