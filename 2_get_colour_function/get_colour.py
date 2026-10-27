def getSize(size):
    if size < 4 or size > 10 or size % 2 != 0: # validate only even numbers between 4 and 10
        print("E: Invalid board size! Please enter an even integer between 4 and 10")
        return None
    return size 



def getPosition(size, row, col):
    # Validate position
    if row < 1 or row > size:
        print("E: Invalid row number.")
        return None, None

    if col < 1 or col > size:
        print("E: Invalid column number.")
        return None, None

    return row, col



def squareColour(size, row, col):
    center = size // 2
    if row > center: # Q3 and Q4
        # possibly red or yellow
        counter = 1
        if col > center:
            # possibly red
            for i in range(center):
                if row == i + center + 1 and col > size - counter:
                    return "R"
                else:
                    counter += 1
        else:
            # possibly yellow
            for i in range(center):
                if row == i + center + 1 and col <= counter:
                    return "Y"
                else:
                    counter += 1

    else: # Q1 and Q2
    # possibly green or blue
        counter = center

        if col > center:
            # possibly blue
            for i in range(center):
                if row == i+1 and col > counter:
                    return "B"
                else:
                    counter += 1

        else:
            # possibly green
            for i in range(center):
                if row == i+1 and col <= counter:
                    return "G"
                else:
                    counter -= 1
    return "-"

def getColour(size, row, col):
    while True:
        if size is None:
            break
        size = getSize(size)
        if size is None:
            continue

        if row is None or col is None:
            break

        row, col = getPosition(size, row, col)
        if row is None or col is None:
            continue

        print(squareColour(size, row, col))
        break


getColour(8, 8, 8)
getColour(8, 6, 2)
getColour(8, 4, 1)
getColour(8, 3, 7)
getColour(8, 5, 2)
getColour(5, 8, 8)
getColour(8, 9, 8)
getColour(8, 8, 9)

