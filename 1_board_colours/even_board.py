def main():
    # Get user input and board size
    size = int(input("Enter size of board (4-10, even): "))
        
    # validate only even numbers between 4 and 10
    if size < 4 or size > 10 or size % 2 != 0:
        print("Invalid board size! Please enter an even integer between 4 and 10") 
        return

    # Get position of X and validate position
    row = int(input("Enter row number: "))
    if row < 1 or row > size:
        print("Invalid row number.")
        return

    column = int(input("Enter column number: "))    
    if column < 1 or column > size:
        print("Invalid column number.")
        return

    # Find the colour at X
    center = size // 2
    if row > center: # Q3 and Q4
        # possibly red or yellow
        counter = 1
        if column > center:
            # possibly red
            for i in range(center):
                if row == i + center + 1 and column > size - counter:
                    print("Colour is Red")
                    return
                else:
                    counter += 1
        else:
            # possibly yellow
            for i in range(center):
                if row == i + center + 1 and column <= counter:
                    print("Colour is Yellow")
                    return
                else:
                    counter += 1

    else: # Q1 and Q2
        # possibly green or blue
        counter = center

        if column > center:
            # possibly blue
            for i in range(center):
                if row == i+1 and column > counter:
                    print("Colour is Blue")
                    return
                else:
                    counter += 1

        else:
            # possibly green
            for i in range(center):
                if row == i+1 and column <= counter:
                    print("Colour is Green")
                    return
                else:
                    counter -= 1
    print("No colour")
    
main()

