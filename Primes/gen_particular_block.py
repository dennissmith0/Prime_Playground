def generate_blocking_positions(n, p):
    blocking_positions = []

    # Calculate the number of sequences
    num_sequences = n // 6 + 1

    # Generate blocking positions for multiples of `p` on LHS
    # Start from sequence `p` - 2 and increment by `p` each time
    row = 1
    for sequence in range(p - (5 * row), num_sequences, p):
        blocking_positions.append((sequence, 3))
        row += 1

    # Generate blocking positions for multiples of `p` on RHS
    # Start from sequence `p` + 5 and increment by `p` each time
    row = 1
    for sequence in range(p - (row + 1), num_sequences, p):
        blocking_positions.append((sequence, 5))
        row += 1

    return blocking_positions

blocking_positions_5 = generate_blocking_positions(150, 5)
blocking_positions_11 = generate_blocking_positions(150, 11)
blocking_positions_17 = generate_blocking_positions(150, 17)

print(blocking_positions_5)
print(blocking_positions_11)
print(blocking_positions_17)

# Function to convert a sequence and index position back to an integer
def position_to_integer(sequence, index):
    if index == 5:
        return (sequence + 1) * 6 + 1
    elif index == 3:
        return (sequence + 1) * 6 - 1

# Print the integer values corresponding to the blocking positions
blocking_integers = [position_to_integer(sequence, index) for sequence, index in blocking_positions_11]
print(blocking_integers)