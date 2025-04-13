for left in range(7):  # Loop through numbers from 0 to 6 for the left value
    for right in range(left, 7):  # Loop through numbers from left to 6 for the right value
        print("[" + str(left) + "|" + str(right) + "]", end=" ")  # Print the pair [left|right] without a newline
    print()  # Print a newline after each row
