hrs = input("Enter Hours:")  # Get hours worked
h = float(hrs)  # Convert to float
rate = input("Enter the rate per hour:")  # Get hourly rate
r = float(rate)  # Convert to float

if h <= 40:  # If 40 hours or less
    totalPay = h * r  # Regular pay
else:  # If more than 40 hours
    totalPay = 40 * r + (h - 40) * r * 1.5  # Regular + overtime pay

print(f"The total pay is: {totalPay}")  # Display total pay