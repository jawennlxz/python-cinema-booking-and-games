def getSize(size):
    if size < 4 or size > 10 or size % 2 != 0: # validate only even numbers between 4 and 10
        print("E: Invalid board size! Please enter an even integer between 4 and 10")
        return None
    return size # lets user input size again


def getColour(size, row, col):
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
            return "-"
        else:
            # possibly yellow
            for i in range(center):
                if row == i + center + 1 and col <= counter:
                    return "Y"
                else:
                    counter += 1
            return "-"

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
            return "-"

        else:
            # possibly green
            for i in range(center):
                if row == i+1 and col <= counter:
                    return "G"
                else:
                    counter -= 1
            return "-"
    pass


def main():
    try:
        size = int(input("Enter board size (4-10, even): "))
    except ValueError:
        return

    size = getSize(size)
    if size is None:
        return

    for row in range(1, size + 1):
        line = ""
        for col in range(1, size + 1):
            colour = getColour(size, row, col)
            if colour == "-":
                if col == ((size // 2) + 1):
                    line += line[-1]
                elif col > (size // 2):
                    try: 
                        emptyCount = int(line[-1]) 
                        emptyCount -= 1
                        line += str(emptyCount)
                    except ValueError:
                        line += str(1)
                else:
                    try: 
                        emptyCount = int(line[-1]) 
                        emptyCount += 1
                        line += str(emptyCount)
                    except ValueError:
                        line += str(1)

            else:
                line += colour
        print(line)

main()


