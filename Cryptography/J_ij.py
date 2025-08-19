import numpy as np

def generate_hadamard_matrix(n):
    """Generate Hadamard matrix of size 2^n."""
    H = [[1, 1], [1, -1]]
    result = H
    for _ in range(n - 1):
        result = np.kron(result, H)
    return result

# Input: n (number of iterations for Hadamard matrix generation)
n = int(input("Enter the value of n (e.g., 1, 2, 3, ...): "))
H_n = generate_hadamard_matrix(n)

size = len(H_n)  # Size of the matrix
num_nodes = 2 * size
num_couplings = size * size

output_filename = f"J_Matrix_2x{size}.txt"

# Write the matrix with header
with open(output_filename, "w") as f:
    # Write header line
    f.write(f"{num_nodes} {num_couplings}\n")
    
    # Write Jij entries
    for i in range(size):
        for j in range(size):
            f.write(f"{i + 1} {j + size + 1} {H_n[i][j]}\n")
