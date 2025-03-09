def count_down(start_number):  # Function to count down from a given number
    current = 3  # Initialize current to 3
    while current > 0:  # Loop while current is greater than 0
        print(current)  # Print the current value
        current -= 1  # Decrement current by 1
    print("Zero!")  # Print "Zero!" when the loop ends

count_down(3)  # Call the function with 3 as the starting number
