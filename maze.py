import turtle, random

# Define the size of the maze and size of each cell
size, cellsize = 17, 10

# Set up the turtle graphics
turtle.speed(0) # Set the turtle's speed to the fastest
turtle.hideturtle() # Hide the turtle icon
turtle.bgcolor("white") # Set the background color to white
turtle.tracer(1, 1) # Update the screen after each drawing

# Create a grid to represent the maze
grid = [[0] * size for _ in range(size)]

# Choose a random starting point for the maze 
x, y = random.randrange(0, size, 2), random.randrange(0, size)
grid[y][x] = 1  # Mark the starting point as visited
stack = [(x, y)]  # Create a stack to keep track of visited cells

# Generate the maze using depth-first search algorithm
while stack:
    x, y = stack[-1]  # Get the current cell
    random.shuffle(directions := [(0, 2), (0, -2), (2, 0), (-2, 0)])  # Shuffle the directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # Calculate the new cell position

        # Check if the new cell is within the grid and unvisited
        if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == 0:
            # Mark the cells between the current and new cell as visited
            grid[y + dy // 2][x + dx // 2] = grid[ny][nx] = 1
            stack.append((nx, ny))  # Add the new cell to the stack
            break  # Exit the loop to explore the new cell
    else:
        stack.pop()  # If no unvisited neighbors, backtrack

# Draw the maze using turtle graphics
for i in range(size):
    for j in range(size):
        if grid[i][j] == 1:  # If cell is visited
            turtle.penup()  # Lift the pen
            turtle.goto(j * cellsize, -i * cellsize)  # Move to the cell position
            turtle.pendown()  # Lower the pen
            for _ in range(4):  # Draw the walls of the cell
                turtle.forward(cellsize if _ * 2 == 0 else cellsize)
                turtle.right(90) # Turn right to draw the next wall

# Update the screen and keep it open until manually closed
turtle.update()
turtle.done()
