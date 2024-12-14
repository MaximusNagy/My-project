import math

num1 =float (input("enter the first num: "))
choose = input("choose [+.-./.*.sin.cos.tan.power]: ")
if choose in ["+", "-", "/", "*"] :
    num2 =float( input("enter the second num: "))
    result =eval(f"{num1} {choose} {num2}")
    print(result)
# elif choose in ["sin","tan","cos"] :
#     func = getattr(math,choose)
#     result =func(math.radians(num1))
#     print(result)
elif choose == "sin" :
    result =math.sin(math.radians(num1))
    print(result)
elif choose == "cos" :
    result =math.cos(math.radians(num1))
    print(result)
elif choose == "tan" :
    result =math.tan(math.radians(num1))
    print(result)
if choose == "power":
    def power():
        power_num = float(input("Enter the power num: "))
        result_power_num = num1 ** power_num
        print(result_power_num)
power()