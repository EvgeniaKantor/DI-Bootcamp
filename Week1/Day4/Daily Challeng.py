matrix_string = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""

# Parse the matrix string into a 2D list
matrix = [list(row) for row in matrix_string.strip().split('\n')]
print(matrix)

# Transpose the matrix to make it easier to read columns
transposed_matrix = list(map(list, zip(*matrix)))
print(transposed_matrix)

# Decode the message
decoded_message = ''
for column in transposed_matrix:
    alpha_chars = [char for char in column if char.isalpha()]
    decoded_message += ''.join(alpha_chars) + ' '

print("Decoded Message: ", decoded_message)
