#create J_ij matrix
lattice_width = int(input("Enter the lattice width (e.g., 2, 4, 8, ...): "))
lattice_width = int(2**lattice_width)
filename_2xn = "linear_2x{}.txt".format(lattice_width)



# Generate 2 x lattice_width file
with open(filename_2xn, "w") as f_2xn:
    for i in range(2):
        for j in range(lattice_width):
            if j != lattice_width - 1:
                f_2xn.write("0.0 ")
            else:
                f_2xn.write("0.0 ")