import re

try:
    # Ask the user to input the name of the file
    file_name = input("Enter the name of the file: ")

    # Try to open the file for reading
    with open(file_name, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Use regular expressions to find all integer sequences
        numbers = re.findall(r'[0-9]+', content)

        # Convert the found strings to integers
        numbers = [int(num) for num in numbers]
        
        # Check if any numbers were found in the file
        if numbers:
            # Calculate the sum of the numbers
            total_sum = sum(numbers)
            
            # Get the count of numbers found
            num_count = len(numbers)
            
            # Print the summary with the count and sum
            print(f"There were {num_count} numbers in the file and the sum of those numbers is {total_sum}.")
        else:
            print("No numbers found in the file.")
except FileNotFoundError:
    # Handle the case when the file is not found
    print("File not found.")
