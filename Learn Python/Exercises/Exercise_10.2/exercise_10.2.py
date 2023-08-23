file_name = input("Enter file name: ")  # Get the filename from the user

try:
    file = open(file_name, 'r')  # Open the file in read mode
    hour_counts = {}  # Dictionary to store hour counts

    for line in file:
        # Check if the line starts with 'From '
        if line.startswith('From '):
            words = line.split()
            time = words[5]  # Extract the time part from the line
            hour = time.split(':')[0]  # Extract the hour from the time

            # Use a tuple to store hour and count in the dictionary
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

    # Convert dictionary items to a list of tuples and sort them by hour
    sorted_hour_counts = sorted(hour_counts.items())

    # Print the hour distribution sorted by hour
    for hour, count in sorted_hour_counts:
        print(f"{hour} {count}")

    # Close the file when done reading
    file.close()

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
