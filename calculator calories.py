print("\n--- Welcome to the Calorie Calculator ---")

# Get user input
choose = input("Choose your sex (male, female): ").lower()
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height in cm: "))
# Ensure height is in cm
if height < 10:  # If height is in meters (e.g., 1.81)
    height *= 100
age = float(input("Enter your age: "))
TDEE = input("Choose your activity level [Sedentary, Light activity, Moderate activity, Active, Very active]: ").capitalize()
Choies = input("Do you want to (normal bulk) or (normal cut) or (hard bulk) or (hard cut) ? ").lower()

# Calculate BMR
if choose == "male":
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
elif choose == "female":
    BMR = 10 * weight + 6.25 * height - 5 * age - 161


else:
    print("Invalid sex entered!")
    BMR = None

if BMR is not None:
    # Calculate TDEE based on activity level
    if TDEE == "Sedentary":
        TDEE_result = BMR * 1.2
    elif TDEE == "Light activity":
        TDEE_result = BMR * 1.375
    elif TDEE == "Moderate activity":
        TDEE_result = BMR * 1.55
    elif TDEE == "Active":
        TDEE_result = BMR * 1.725
    elif TDEE == "Very active":
        TDEE_result = BMR * 1.9
    else:
        TDEE_result = None
        print("Invalid activity level entered!")

    # Display TDEE result
    if TDEE_result is not None:
        print(f"Your TDEE is: {TDEE_result:.2f} calories.")

        # Adjust for bulk or cut
        if Choies == "bulk":
            bulk_result = TDEE_result + 500
            print(f"Your calories for bulking: {bulk_result:.2f} calories.")
        elif Choies == "cut":
            cut_result = TDEE_result - 500
            print(f"Your calories for cutting: {cut_result:.2f} calories.")
        elif Choies == "hard bulk":
            bulk_result = TDEE_result + 1000
            print(f"Your calories for bulking: {bulk_result:.2f} calories.")  
        elif Choies == "hard cut":
            bulk_result = TDEE_result - 1000
            print(f"Your calories for cutting: {bulk_result:.2f} calories.")  
        else:
            print("Invalid choice entered for bulk/cut.")

