import matplotlib.pyplot as plt

# create a function to calculate y values
def function(x):
    result = 3 * x + 2
    return result

# defining empty lists
xCoord = []
yCoord = []
# loop over 10 values from 0 to 9, and calculate the matching values for y using the
for i in range(0, 10):
    xCoord.append(i)
    yCoord.append(function(i))
    plt.plot(xCoord, yCoord, marker='x', color='red')
# function to add title
plt.title('Example 5')
# Function to label axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# function for the visibility of grid
plt.grid()
plt.show()
