values = [10, 20, 30, 40, 50]  # List of values
sum = 0  # Initialize sum to 0
length = 0  # Initialize length to 0
for value in values:  # Loop through each value in the list
    sum = sum + value  # Add the value to sum
    length = length + 1  # Increment length by 1
print("Total sum = " + str(sum) + " and the Average = " + str(sum / length))  # Print the total sum and average
