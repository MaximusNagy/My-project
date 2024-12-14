# # print("\n--- Welcome to Unit Converter ---")
# # print("form kg to lb and lb to kg")
# # num1 = float(input("\n enter the number: "))
# # choies = input("choose in [from kg to lb, from lb to kg ]")

# # if choies == "from kg to lb":
# #     result = num1 / 2.2
# #     print(result)
# # elif choies == "from lb to kg":
# #     result = num1 * 2.2
# #     print (result)
# # else:
# #     print("Incorrect selection. Try again.")
# #or
# def unit():
#     print("\n--- Welcome to Unit Converter ---")
#     print("1. From kg to lb")
#     print("2. From lb to kg")
#     print("3. Exit")

# while True:
#     unit()
#     choices = input("Choose in [1, 2, 3]: ")
    
#     # التأكد من أن الإدخال هو أحد الخيارات المسموحة
#     if choices not in ["1", "2", "3"]:
#         print("Invalid choice, please select a valid option.")
#         continue  # العودة إلى بداية الحلقة لتحديد خيار صحيح
    
#     elif choices == "3":
#         print("Good bye!")
#         break  # إنهاء البرنامج
    
#     # أخذ الرقم المدخل بعد التأكد من الخيار
#     num1 = float(input("\nEnter the number: "))
    
#     if choices == "1":
#         # تحويل من kg إلى lb
#         result = num1 * 2.20462
#         print(f"{num1} kg is equal to {result:.2f} lb")
        
#     elif choices == "2":
#         # تحويل من lb إلى kg
#         result = num1 * 0.453592
#         print(f"{num1} lb is equal to {result:.2f} kg")
        
a = [1,2,3,4,5]
b = a
b[2] = 26 
print(b)