from datetime import datetime

print("\nWelcome to the age calculator!")

# الحصول على السنة، الشهر، واليوم الحالي
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day

# إدخال تاريخ الميلاد
year = int(input("Enter your year of birth: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

# حساب العمر بالسنة
age_year = current_year - year

# تعديل العمر في حال لم يمر الشهر أو اليوم بعد هذا العام
if current_month < month or (current_month == month and current_day < day):
    age_year -= 1

# حساب الأشهر والأيام
if current_month >= month:
    age_month = current_month - month
else:
    age_month = 12 - (month - current_month)

if current_day >= day:
    age_day = current_day - day
else:
    age_day = (30 - day) + current_day  # افتراض أن الشهر يحتوي على 30 يومًا

# عرض النتيجة
result = f"Your age is: {age_year} years, {age_month} months, {age_day} days."
print(result)
