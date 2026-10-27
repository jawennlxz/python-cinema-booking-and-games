# Get input from user for board size
size = int(input("Enter size of board (3-9, odd): "))

# Validate the size. Must be 3-9, odd number
if size < 3 or size > 9 or size % 2 == 0:
    print("Invalid board size! Please enter an odd integer between 3 and 9.")
else:
    # Get input of row for X
    row = int(input("Enter row number: "))
    # Validate row number
    if row < 1 or row > size:
        print("Invalid row number.")
    else:
        # Get input of column for X
        col = int(input("Enter column number: "))
        # Validate column number
        if col < 1 or col > size:
            print("Invalid column number.")
        else:
            # Identify squares there have no colour
            if row == col or row + col == size + 1:
                print("No colour")

            # Identify squares that are Green
            elif row < col and row + col < size + 1:
                print("Colour is Green")

            # Identify squares that are Red
            elif row > col and row + col > size + 1:
                print("Colour is Red")

            # Identify squares that are Yellow
            elif row > col and row + col < size + 1:
                print("Colour is Yellow")

            # Identify squares that are Blue
            elif row < col and row + col > size + 1:
                print("Colour is Blue")
