# these two first variables which have the input function ask the user for input to know hours worked and their pay rate. The input will naturally come in as a string. When using the input() function in Python, it always returns the user's input as a string.  
hw = input("Enter hours you have worked: ")
ph = input("Enter rate per hour: ")
# these two next lines changes the strings given by the user to floats/numbers with decimals
hours_worked = float (hw)
rate_per_hour = float (ph)
# overtime rate is appointed to be 1.5 times the normal rate per hour
overtime_rate = 1.5 * rate_per_hour
# overtime hours are any hours above 40 hours
overtime_hours = hours_worked - 40
if hours_worked <= (40):
    print(hours_worked * rate_per_hour)
else:
    print(40 * rate_per_hour + overtime_hours * overtime_rate)