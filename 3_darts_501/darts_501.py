import random

def names():
    # Get player names and validates names
    list_of_names = [] # to add player names into a list
    numOfPlayers = 1 # Counts number of players

    while True:
        player_name = str(input(f"Enter player {numOfPlayers}'s name (empty to end): ")).strip().capitalize()
        
        if player_name in list_of_names:
            print("Player names must be unique")
            continue # enter for input again

        elif player_name == "":
            if len(list_of_names) < 2:
                print("Plese enter at least 2 players")
                continue
            else:
                break
        
        list_of_names.append(player_name)
        numOfPlayers += 1

        if numOfPlayers > 5:
            break

    return list_of_names    


def game():
    total_score = 501
    players = names()
    random.shuffle(players)

    scores = {player: total_score for player in players}

    number_convert = {
        "1": "single",
        "2": "double",
        "3": "triple"
    }

    num_of_turns = 1

    while True:
        for name_of_player in players: # goes through for each player
            print(f"{name_of_player}'s turn {num_of_turns}, current score is {scores[name_of_player]}")
            
            round_num = 1

            while round_num <= 3: #rounds 1-3
                try:
                    chosen_number = int(input(f"{name_of_player}'s round {round_num}, choose a number from 1 to 20 inclusive, or 25: "))
                    if chosen_number not in range (1, 21) and chosen_number != 25:
                        print("Invalid input. Please choose a number from 1 to 20 inclusive, or 25.")
                        continue
                    else:
                        multiplier = random.choice([1, 2, 3]) if chosen_number in range(1, 21) else random.choice([1, 2])
                        
                        multiplier_name = number_convert.get(str(multiplier))

                        # save previous score
                        previous_score = scores[name_of_player]

                        # get result of round
                        result = multiplier * chosen_number
                        new_score = previous_score - result

                        # validate bust scores
                        if new_score < 0 or (new_score == 0 and multiplier != 2) or new_score ==  1:
                            print(f"It's a {str(multiplier_name)}, total {multiplier}x{chosen_number}={result} points, {name_of_player} is busted, reverting to initial score {scores[name_of_player]}! Try again next turn")
                            break
                        elif new_score == 0:
                            print(f"It's a {str(multiplier_name)}, total {multiplier}x{chosen_number}={result} points, {name_of_player} wins in {num_of_turns} turns! ")
                            scores[name_of_player] = new_score
                            for player in players:
                                print(f"{player}'s score is {scores[player]}")
                            return
                        else:
                            scores[name_of_player] = new_score
                            print(f"It's a {str(multiplier_name)}, total {multiplier}x{chosen_number}={result} points, {name_of_player}'s new score is {scores[name_of_player]}")

                        round_num += 1 

                except ValueError:
                    print("Invalid input. Enter a number.")
                    continue
            print("Next player...")

        num_of_turns += 1
  
game()
