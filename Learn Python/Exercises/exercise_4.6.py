def computepay(a, b):
    return a * b
hours = float(input("Enter hours you have worked: "))
rate = float(input("What is your hourly rate: "))


if hours <= 40:
    total_pay = computepay(hours, rate)
    print("Pay", total_pay)
else:
    normal_pay = 420
    overtime_hours = hours - 40
    overtime_rate = rate * 1.5
    overtime_pay = computepay(overtime_hours, overtime_rate)
    total_pay = normal_pay + overtime_pay
    print ("Pay", total_pay)