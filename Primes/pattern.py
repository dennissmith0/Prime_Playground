import matplotlib.pyplot as plt

# # # Initialize the pattern with the first sequence
# # pattern = [[2, 3, 4, 5, 6, 7]]

# # # Generate the next sequences up to 100
# # for i in range(1, 17):  # 17 sequences are enough to get up to 100
# #     sequence = [x + 6 * i for x in pattern[0]]
# #     pattern.append(sequence)

# # # Display the pattern as a table
# # for sequence in pattern:
# #     print(sequence)

# # First, let's define a function to generate the pattern up to n
# def generate_pattern(n):
#     pattern = []
#     start = 2
#     while start <= n:
#         sequence = [start + i for i in range(6)]
#         pattern.append(sequence)
#         start += 6
#     return pattern

# # Now let's generate the pattern up to 100 and extract the possible primes
# pattern = generate_pattern(211)
# poss = [sequence[3] for sequence in pattern if sequence[3] <= 211] + [sequence[5] for sequence in pattern if sequence[5] <= 211]

# # Sorting the possible prime list
# poss.sort()

# # Convert the integers in the list to strings
# poss_str = [str(i) for i in poss]

# # Join the strings in the list with a space delimiter and print the result
# print(' '.join(poss_str))


# # As explained earlier, we generate the positions
# positions_5 = []
# positions_7 = []

# for i, sequence in enumerate(pattern):
#     for j, number in enumerate(sequence):
#         if number % 5 == 0:
#             positions_5.append((i, j))
#         if number % 7 == 0:
#             positions_7.append((i, j))

# # Extract the x and y coordinates for the two sets of positions
# x_5, y_5 = zip(*positions_5)
# x_7, y_7 = zip(*positions_7)

# # Create the plot
# # Create the plot with the x-axis at the top
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.scatter(x_5, y_5, color='blue', label='Multiples of 5')
# ax.scatter(x_7, y_7, color='red', label='Multiples of 7')
# ax.set_ylabel('Sequence Number')
# ax.set_xlabel('Index in Sequence')
# ax.set_title('Positions of Multiples of 5 and 7 in the Pattern')
# ax.legend()

# # Move x-axis to top
# ax.xaxis.tick_top()
# ax.xaxis.set_label_position('top')

# # Invert y-axis to have the 0,0 start in the top left corner
# ax.invert_yaxis()

# plt.show()
# First, let's define a function to generate the pattern up to n
def generate_pattern(n):
    pattern = []
    start = 2
    while start <= n:
        sequence = [start + i for i in range(6)]
        pattern.append(sequence)
        start += 6
    return pattern

# Now let's generate the pattern up to a sequence number of 35*6 = 210
pattern = generate_pattern(210)
print(pattern)
# # As explained earlier, we generate the positions
# positions_5 = []
# positions_7 = []

# for i, sequence in enumerate(pattern):
#     for j, number in enumerate(sequence):
#         if number % 5 == 0:
#             positions_5.append((i, j))
#         if number % 7 == 0:
#             positions_7.append((i, j))

# # Extract the x and y coordinates for the two sets of positions
# x_5, y_5 = zip(*positions_5)
# x_7, y_7 = zip(*positions_7)

# # Create the plot
# fig, ax = plt.subplots(figsize=(6, 10))  # Adjust figure size for a longer vertical visualization
# ax.scatter(y_5, x_5, color='blue', label='Multiples of 5')
# ax.scatter(y_7, x_7, color='red', label='Multiples of 7')
# ax.set_xlabel('Index in Sequence')
# ax.set_ylabel('Sequence Number')
# ax.set_title('Positions of Multiples of 5 and 7 in the Pattern')
# ax.legend()

# # Move x-axis to top
# ax.xaxis.tick_top()
# ax.xaxis.set_label_position('top')

# # Invert y-axis to have the 0,0 start in the top left corner
# ax.invert_yaxis()

# plt.show()
