# این برنامه میانگین اعداد ورودی را محاسبه می‌کند.

# تعریف تابع برای محاسبه میانگین
def calculate_average(numbers):
    total = sum(numbers) # مجموع اعداد
    count = len(numbers) # تعداد اعداد
    return total / count # محاسبه‌ی میانگین

# دریافت اعداد از کاربر
numbers = [] # لیستی برای ذخیره اعداد
num_count = int(input("تعداد اعداد را وارد کنید: "))

# گرفتن اعداد و ذخیره در لیست
for i in range(num_count):
    num = float(input("عدد {}: ".format(i + 1)))
    numbers.append(num)

# نمایش میانگین
avg = calculate_average(numbers)
print("میانگین اعداد وارد شده: ", avg)
