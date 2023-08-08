# Function to generate blocking positions
def generate_blocking_positions(n):
    # Create an empty list to hold the blocking positions
    blocking_positions = []

    # Calculate the number of sequences
    num_sequences = n // 6 + 1

    # Generate blocking positions for multiples of 5 on LHS
    # Start from sequence 0 and increment by 5 each time
    for sequence in range(1, num_sequences, 11):
        blocking_positions.append((sequence, 3))

    # Generate blocking positions for multiples of 5 on RHS
    # Start from sequence 3 and increment by 5 each time
    for sequence in range(8, num_sequences, 11):
        blocking_positions.append((sequence, 5))

    return blocking_positions

# Test the function with n = 100
blocking_positions = generate_blocking_positions(150)
blocking_positions.sort()

# Print the blocking positions
print(blocking_positions)

# Function to convert a sequence and index position back to an integer
def position_to_integer(sequence, index):
    if index == 5:
        return (sequence + 1) * 6 + 1
    elif index == 3:
        return (sequence + 1) * 6 - 1

# Print the integer values corresponding to the blocking positions
blocking_integers = [position_to_integer(sequence, index) for sequence, index in blocking_positions]
print(blocking_integers)
