def salary(num):
    overtime = num - 160
    income = 100000 * 160
    if 200 >= num > 160:
        overtime *= 50000
    elif num > 200 :
        overtime = 2000000
    

    return (income + overtime)
print(salary(333))
