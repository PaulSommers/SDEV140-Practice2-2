"""
Author: Paul Sommers
Date written: 10/25/2024
Assignment: Practice Exercise 2-2
Short Desc: This program calculates the surface area of a cube based on the length of an edge.
            The program prompts the user to input the length of the cube's edge (Int),
            calculates the surface area, and then it displays the result.
"""
# Step 1: Prompt the user for the length of the cube's edge
intCubeEdge = int(input("Enter the length of the cube's edge (integer): "))

# Step 2: Calculate the surface area of the cube
# Formula for surface area of a cube: 6 * (edge_length^2) or add the area of its 6 face squares
surface_area = 6 * (intCubeEdge ** 2)

# Step 3: Print the calculated surface area
print(f"The surface area of the cube is: {surface_area} square units")