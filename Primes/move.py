# Importing the necessary libraries
import matplotlib.pyplot as plt
import pattern

# As explained earlier, we generate the positions
positions_5 = []
positions_7 = []

for i, sequence in enumerate(pattern):
    for j, number in enumerate(sequence):
        if number % 5 == 0:
            positions_5.append((i, j))
        if number % 7 == 0:
            positions_7.append((i, j))

# Extract the x and y coordinates for the two sets of positions
x_5, y_5 = zip(*positions_5)
x_7, y_7 = zip(*positions_7)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(x_5, y_5, color='blue', label='Multiples of 5')
plt.scatter(x_7, y_7, color='red', label='Multiples of 7')
plt.xlabel('Sequence Number')
plt.ylabel('Index in Sequence')
plt.title('Positions of Multiples of 5 and 7 in the Pattern')
plt.legend()
plt.show()
