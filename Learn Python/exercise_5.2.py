## Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    input_str = input("Enter an integer number ('done' to finish): ")
    
    if input_str.lower() == 'done':
        break
    
    try:
        number = int(input_str)
        
        if largest is None or number > largest:
            largest = number
        
        if smallest is None or number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input")

if largest is not None:
    print("Maximum is", largest)

if smallest is not None:
    print("Minimum is", smallest)
