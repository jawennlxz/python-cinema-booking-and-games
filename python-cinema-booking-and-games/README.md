# Cinema Seat Booking and Games in Python

A set of Python console programs built from written specifications, covering selection logic, functions, loops, randomisation and nested lists. The work progresses from coloured board generators to a 501 darts game and a menu-driven cinema seat booking system with automatic best-seat selection.

Module: ICT133 Structured Programming, Singapore University of Social Sciences (2025)

## Contents

| Folder | Program | What it does |
|---|---|---|
| `1_board_colours` | `odd_board.py`, `even_board.py` | Prints a board of coloured quadrants for a chosen size, using selection statements only (no lists) |
| `2_get_colour_function` | `get_colour.py`, `print_board.py`, `numbered_rings.py` | A reusable `getColour(size, row, col)` function, used to print the full board and a version with numbered rings in the centre |
| `3_darts_501` | `darts_501.py` | A 501 darts game for 2 to 5 players with random multipliers, bust rules and a double-out finish |
| `4_cinema_seat_booking` | `seat_booking.py`, `seat_booking_auto_select.py` | A cinema seat booking system using a nested-list seating plan, with automatic best-seat recommendations |

## How to run

You need Python 3 installed. No extra packages are required.

```bash
python 4_cinema_seat_booking/seat_booking_auto_select.py
```

Each program is interactive and prompts for input in the terminal.

## Highlights

### Numbered rings board (size 10)

```
GGGGGBBBBB
GGGG11BBBB
GGG1221BBB
GG123321BB
G12344321B
Y12344321R
YY123321RR
YYY1221RRR
YYYY11RRRR
YYYYYRRRRR
```

### Cinema seat booking

Seats are booked in the format `C05-4` (start at seat C in row 05, book 4 seats). Input is checked for format, seat range and seats that are already taken. Row 01 is nearest the screen.

```
       Screen
   A B C D E F G H
01 O O O O O O O O
02 O O O O O O O O
03 O O O O O O O O
04 O O O O O O O O
05 O O X X X X O O
06 O O O O O O O O
07 O O O O O O O O
08 O O O O O O O O
09 O O O O O O O O
10 O O O O X X O O
```

`O` = available, `X` = booked

### Automatic best-seat selection

For a requested group size, the program:

1. Starts from the back row, where viewing is best.
2. Finds every block of free seats next to each other that fits the group.
3. Ranks the blocks by distance from the centre of the row.
4. Offers the best option first. The user accepts with `y`, sees the next option with `n`, or cancels with `0`.

## Skills demonstrated

- Selection, loops and user-defined functions
- Nested lists and dictionaries
- Input validation and error handling with `try`/`except`
- Randomisation with the `random` module
- Breaking a specification into small, testable functions

## Author

Jawenn Lim
