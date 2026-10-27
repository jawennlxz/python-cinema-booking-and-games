# rows 3 to 10
# row numbers start from 01 to 10 
# 1st row is in front of screen
# seats per row is 3 to 10
# seats numbered A - J
# seats start from left
# avail seats = O
# booked seats = X

# steps
# input the number of rows
# input number of seats per row
# create nested list of seating plan
# loop application
# display options
# 1. display seating plan > return to main menu
# 2. book seats > display seating plan, input location, num of seats
    # only can book continuous seats on same row
    # successful booking > O > X
    # display updated seating plan
    # if not, error msg, return to main menu
# 3. quit
# menu loops until quit

def getRow():
    # get row input and validate input
    while True:
        try:
            row = int(input("Enter number of rows (3-10 or 0 to quit): "))

            if row == 0:
                print("Program end")
                exit()

            elif row < 3 or row > 10:
                print("Invalid input! Please try again")
                continue

            else:
                break

        except ValueError:
            print("Invalid input! Enter a number")

    return row


def getSeat():
    # get seat input and validate input
    while True:
        try:
            seat = int(input("Enter number of seats per row (3-10 or 0 to quit): "))

            if seat == 0:
                print("Program end")
                exit()

            elif seat <3 or seat > 10:
                print("Invalid input! Please try again")

            else:
                break

        except ValueError:
            print("Invalid input! Enter a number")

    return seat

def displaySeatingPlan(seatingPlan, col_label):
    # align "SCREEN" in center
    width = 3 + len(col_label) * 2
    print("\n" + "Screen".center(width))

    # convert column to alphabets
    print("   " + " ".join(col_label))

    for i, row in enumerate(seatingPlan):
        row_number = str(i + 1).zfill(2)
        print(f"{row_number} " + " ".join(row))

    print("\n")

def bookSeats(seatingPlan, col_label):  
    while True:
        booking_seat = str(input("Enter seats to book (eg C05-4) or 0 to cancel: "))

        if booking_seat == "0":
            print("Cancelled")
            return
        
        if len(booking_seat) < 5 or booking_seat[3] != "-":
            print("Invalid input! Please enter in @NN-# format where @:seat label, NN:row, #:number of seats")
            continue
        
        
        try:
            col = booking_seat[0]
            row_num = int(booking_seat[1:3]) - 1
            num_seats = int(booking_seat[4:])

        except ValueError:
            print("Invalid input! Please enter in @NN-# format where @:seat label, NN:row, #:number of seats")
            continue

        if col not in col_label:
            print("Invalid seat label! Please enter in @NN-# format where @:seat label, NN:row, #:number of seats")
            continue

        if not (0 <= row_num < len(seatingPlan)):
            print("Invalid row! Please enter in @NN-# format where @:seat label, NN:row, #:number of seats")
            continue

        if not (1 <= num_seats <= len(col_label)):
            print("Invalid number of seats! Please enter in @NN-# format where @:seat label, NN:row, #:number of seats")
            continue

        
        start_index = col_label.index(col)
        end_index = start_index + num_seats
        
        if end_index > len(col_label):
            print("Not all seats at those locations are available! Please try again")
            continue

        if all(seat == "O" for seat in seatingPlan[row_num][start_index:end_index]):
            for i in range(start_index, end_index):
                seatingPlan[row_num][i] = "X"
            print("Seats booked")
            displaySeatingPlan(seatingPlan, col_label)
            return
        else:
            print("Not all seats at those locations are available! Please try again")
            continue


def autoSelectSeats(seatingPlan, col_label):
    # select seats automatically
    while True:
        try:
            num_of_seats = int(input("Enter number of seats (0 to cancel): "))

            if num_of_seats == 0:
                print("Cancelled")
                break

            if not (1 <= num_of_seats <= len(col_label)):
                print("Invalid input! Please try again")
                continue
            
        except ValueError:
            print("Invalid input! Enter a number")
            continue
        
        for row_index in reversed(range(len(seatingPlan))):
            row = seatingPlan[row_index]
            row_length = len(row)
            center = row_length // 2

            valid_blocks = []
            for start in range(row_length - num_of_seats + 1):
                end = start + num_of_seats
                block = row[start:end]
                if all(seat == "O" for seat in block):
                    block_center = (start + end - 1) // 2
                    distance = abs(center - block_center)
                    direction_bias = block_center - center
                    valid_blocks.append((distance, -direction_bias, start, end))

            if valid_blocks:
                valid_blocks.sort()

                for i, (distance, direction_bias, start, end) in enumerate(valid_blocks[:3]):
                    row_label = str(row_index + 1).zfill(2)

                    if num_of_seats == 1:
                        seat_label = f"{col_label[start]}{row_label}"
                        prompt = f"Would you like to book the seat {seat_label} (y/n or 0 to cancel): "

                    else:
                        start_label = f"{col_label[start]}{row_label}"
                        end_label = f"{col_label[end - 1]}{row_label}"
                        prompt = f"Would you like to book the seats {start_label} to {end_label} (y/n or 0 to cancel): "

                    displaySeatingPlan(seatingPlan, col_label)
            
                    while True:
                        confirm = input(prompt).lower()

                        if confirm == "y":
                            for i in range(start, end):
                                seatingPlan[row_index][i] = "X"
                            print("Seats booked")
                            displaySeatingPlan(seatingPlan, col_label)
                            return

                        elif confirm == "0":
                            print("Cancelled")
                            return

                        elif confirm == "n":
                            break


def displayMenu(seatingPlan, col_label):
    #display menu
    while True:
        print("""\n
Booking Menu
------------
1. Show Seats
2. Book Seats
3. Auto Select Seats
0. Quit    
        \n""")

    # loop until valid input, recall to other functions
        try:
            option = int(input("Enter option: "))

            if option == 1:
                displaySeatingPlan(seatingPlan, col_label)

            elif option == 2:
                displaySeatingPlan(seatingPlan, col_label)
                bookSeats(seatingPlan, col_label)

            elif option == 3:
                autoSelectSeats(seatingPlan, col_label)
                       
            elif option == 0:
                print("Program end")
                break

            else:
                print("Invalid input! Please try again")

        except ValueError: # if input is not an int
            print("Please enter an option.")

def main():
    # get row
    row = getRow()

    # get seat
    seat = getSeat()

    col_label = [chr(65 + i) for i in range(seat)]

    seatingPlan = [["O"] * seat for _ in range(row)]

    displayMenu(seatingPlan, col_label)

main()

