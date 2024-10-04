import streamlit as st
import numpy as np
# import matplotlib.pyplot as plt

# Function to generate Maximum Length Sequence (MLS) using LFSR
def generate_mls(degree, seed, taps):
    n = 2**degree - 1  # Length of the MLS sequence
    register = seed.copy()  # Initialize shift register
    mls_sequence = []
    
    for _ in range(n):
        mls_sequence.append(register[-1])  # Store the last bit in the sequence
        # Calculate new bit (feedback based on taps)
        new_bit = 0
        for tap in taps:
            new_bit ^= register[tap]  # XOR feedback taps
        # Shift the register and add the new bit to the front
        register = [new_bit] + register[:-1]
    
    return mls_sequence

# Function to map MLS sequence to a grid
def map_mls_to_grid(mls_sequence, rows, cols):
    grid = np.zeros((rows, cols), dtype=int)  # Create an empty grid
    mls_length = len(mls_sequence)
    
    for i in range(rows * cols):
        if i < mls_length:
            grid[i // cols][i % cols] = mls_sequence[i]  # Map MLS to grid position
        else:
            break  # If MLS sequence is shorter than grid size, stop
    
    return grid

# # Function to visualize the grid
# def plot_grid(grid):
#     fig, ax = plt.subplots()
#     ax.imshow(grid, cmap='binary', interpolation='none')

#     # Add grid lines and labels
#     ax.set_xticks(np.arange(grid.shape[1]) - 0.5, minor=True)
#     ax.set_yticks(np.arange(grid.shape[0]) - 0.5, minor=True)
#     ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    
#     # Annotate grid cells
#     for i in range(grid.shape[0]):
#         for j in range(grid.shape[1]):
#             text = "O" if grid[i, j] == 1 else "X"
#             ax.text(j, i, text, ha="center", va="center", color="red" if grid[i, j] == 1 else "blue")
    
#     return fig

# Streamlit App
def main():
    st.title("Acoustic Panel Hole Placement using Maximum Length Sequence (MLS)")

    st.sidebar.header("Inputs")
    
    # Input: Degree of the polynomial
    degree = st.sidebar.number_input("Degree of the polynomial (number of shift registers)", min_value=2, max_value=16, value=4)
    
    # Input: Seed (initial state of the shift register)
    seed_input = st.sidebar.text_input("Initial Seed (e.g., '1,0,0,1' for degree 4)", value="1,0,0,1")
    seed = [int(bit) for bit in seed_input.split(",")]
    
    # Input: Feedback Taps (positions for XOR, 0-indexed)
    taps_input = st.sidebar.text_input("Feedback Taps (0-indexed, e.g., '3,2' for taps at positions 4 and 3)", value="3,2")
    taps = [int(tap) for tap in taps_input.split(",")]
    
    # Input: Dimensions of the acoustic panel (rows x columns)
    rows = st.sidebar.number_input("Number of rows in the panel", min_value=2, max_value=50, value=10)
    cols = st.sidebar.number_input("Number of columns in the panel", min_value=2, max_value=50, value=10)
    
    # Generate the MLS sequence
    if st.sidebar.button("Generate MLS"):
        if len(seed) == degree:
            mls_sequence = generate_mls(degree, seed, taps)
            st.write(f"Generated MLS sequence of length {len(mls_sequence)}:")
            st.write(mls_sequence)
            
            # Map the MLS sequence to a grid
            grid = map_mls_to_grid(mls_sequence, rows, cols)
            
            # Plot the grid showing where to place holes
            st.write("Grid representation of the acoustic panel (O = Hole, X = No Hole):")
            # fig = plot_grid(grid)
            # st.pyplot(fig)
            
        else:
            st.error(f"The seed length ({len(seed)}) does not match the degree ({degree}).")

if __name__ == "__main__":
    main()

'''
import streamlit as st
import numpy as np

# Function to generate Maximum Length Sequence (MLS) using LFSR
def generate_mls(degree, seed, taps):
    n = 2**degree - 1  # Length of the MLS sequence
    register = seed.copy()  # Initialize shift register
    mls_sequence = []
    
    for _ in range(n):
        mls_sequence.append(register[-1])  # Store the last bit in the sequence
        # Calculate new bit (feedback based on taps)
        new_bit = 0
        for tap in taps:
            new_bit ^= register[tap]  # XOR feedback taps
        # Shift the register and add the new bit to the front
        register = [new_bit] + register[:-1]
    
    return mls_sequence

# Streamlit App
def main():
    st.title("Maximum Length Sequence (MLS) Generator")
    
    st.sidebar.header("Inputs")
    # Input: Degree of the polynomial
    degree = st.sidebar.number_input("Degree of the polynomial (number of shift registers)", min_value=2, max_value=16, value=4)
    
    # Input: Seed (initial state of the shift register)
    seed_input = st.sidebar.text_input("Initial Seed (e.g., '1,0,0,1' for degree 4)", value="1,0,0,1")
    seed = [int(bit) for bit in seed_input.split(",")]
    
    # Input: Feedback Taps (positions for XOR, 0-indexed)
    taps_input = st.sidebar.text_input("Feedback Taps (0-indexed, e.g., '3,2' for taps at positions 4 and 3)", value="3,2")
    taps = [int(tap) for tap in taps_input.split(",")]
    
    # Generate the MLS sequence
    if st.sidebar.button("Generate MLS"):
        if len(seed) == degree:
            mls_sequence = generate_mls(degree, seed, taps)
            st.write(f"Generated MLS sequence of length {len(mls_sequence)}:")
            st.write(mls_sequence)
        else:
            st.error(f"The seed length ({len(seed)}) does not match the degree ({degree}).")
    
    st.sidebar.write("Make sure the seed length matches the degree of the polynomial.")

if __name__ == "__main__":
    main()
'''
