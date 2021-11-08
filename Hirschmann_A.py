
import random

def main():
    #explanation of game
    print("This is a guessing game, there are two players and there will be three games played, for each the players will be guessing a new multiple. After the games are completed a tally will be taken to determine the overall winner.")
    #starting off wins variable to later determine winner
    wins = 0

    #ask for names so they can be referred to by name
    player1=input(str("Player 1, please enter your name:"))
    player2=input(str("Player 2, please enter your name:"))

    #for loop that runs three games
    for game_count in range (0,3):
        #at the beginning of each loop, guess count needs to be zero so while loop within game() can run
        guess_count1 = 0
        guess_count2 = 0
        #at the beginning of each loop, both players need to be back at no win so while loop within game() can run
        player1_win = "no"
        player2_win = "no"
        #start of past guesses list so they can be printed as players guess to help
        past_guesses1 =[]
        past_guesses2 = []

        #explains which multiple is being guessed in each game
        instructions(game_count)

        #determines multiple for each game
        multiplier = findMultiplier(game_count)
        #selects the random number that will be guessed
        number = getCorrect(game_count)
        
        #this line runs each game, which includes three guesses for each player
        winner = game(guess_count1, guess_count2, player1_win, player2_win, multiplier, number, player1, player2, past_guesses1, past_guesses2)

        #as the games are run they will either add or subtract to wins so that the overall winner can be determined
        wins = wins + winner
    

    #in this function if wins is less than 0 the winner is player 2 and if the wins are greater than 0 the winner is player 1
    overall_winner(wins, player1, player2)
    


def instructions(game_count):
    if game_count == 0:
        return(print("This is a guessing game, both players will have three opportunities to guess a random multiple of 7. If one of the players guesses the number correctly the game ends and the next will begin."))
    elif game_count == 1:
        return(print("This is a guessing game, both players will have three opportunities to guess a random multiple of 5. If one of the players guesses the number correctly the game ends and the next will begin."))
    elif game_count == 2:
        return(print("This is a guessing game, both players will have three opportunities to guess a random multiple of 9. If one of the players guesses the number correctly the game ends."))

def findMultiplier(game_count):
    #using the game count in for loop, multiplier is determined
    if game_count == 0:
        return(7)
    elif game_count == 1:
        return(5)
    elif game_count == 2:
        return(9)

def getCorrect(game_count):
    #similarly using game count in for loop, random number is selected
    if game_count == 0:
        return(random.randrange(0,100,7))
    elif game_count == 1:
        return(random.randrange(0,100,5))
    elif game_count == 2:
        return(random.randrange(0,100,9))

def game(guess_count1, guess_count2, player1_win, player2_win, multiplier, number, player1, player2, past_guesses1, past_guesses2):
    #while each player hasn't guessed three times and no one has guessed the number the while loops runs
    while guess_count1 <3 and guess_count2 <3 and player1_win != "yes" and  player2_win != "yes":
            if guess_count1 >= 1:
                print(f'{player1} here is the list of your past guesses: {past_guesses1}')
            player1_guess=int(input(f'{player1} enter your guess:'))
            past_guesses1.append(player1_guess)
            guess_count1 += 1
            if player1_guess == number:
                player1_win = "yes"
                print(f'Congratulations {player1}, you won this round!')
                if player1_win == "yes":
                    #later added to wins to determine final winner
                    winner = 1
                    return(winner)
            elif player1_guess < 0 or player1_guess > 100:
                    print(f'{player1} you have entered a number that is not within the range of 0 to 100.')
            elif player1_guess % multiplier != 0 and player1_guess > number:
                print(f'{player1} you did not enter a multiple of {multiplier}, but the number is lower')
            elif player1_guess % multiplier != 0 and player1_guess < number:
                print(f'{player1} you did not enter a multiple of {multiplier}, but the number is higher')
            elif player1_guess > number:
                print("Too high try a lower guess")
                player1_win = "no"
            elif player1_guess < number:
                print("Too low try a higher guess")
                player1_win = "no"

            if player1_win != "yes":
                if guess_count2 >= 1:
                    print(f'{player2} here is the list of your past guesses: {past_guesses2}')
                player2_guess=int(input(f'{player2} enter your guess:'))
                past_guesses2.append(player2_guess)
                guess_count2 += 1
                if player2_guess == number:
                    player2_win = "yes"
                    print(f'Congratulations {player2}, you won this round!')
                    if  player2_win == "yes":
                        #later added to wins to determine final winner
                        winner = -1
                        return(winner)
                elif player2_guess < 0 or player2_guess > 100:
                    print(f'{player2} you have entered a number that is not within the range of 0 to 100.')
                elif player2_guess % multiplier != 0 and player2_guess > number:
                    print(f'{player2} you did not enter a multiple of {multiplier}, but the number is lower')
                elif player2_guess % multiplier != 0 and player2_guess < number:
                    print(f'{player2} you did not enter a multiple of {multiplier}, but the number is higher')
                elif player2_guess > number:
                    print("Too high try a lower guess")
                    player2_win = "no"
                elif player2_guess < number:
                    print("Too low try a higher guess")
                    player2_win = "no"

            if guess_count1 == 3 and guess_count2 == 3 and player1_win == "no" and  player2_win == "no":
                print(f'{player1} and {player2} you are both losers, terrible guessers.')
                winner = 0
                return(winner)
            


def overall_winner(wins, player1, player2):
    if wins > 0:
        return(print(f'Great job {player1} you won the most games!'))
    elif wins < 0:
        return(print(f'Great job {player2} you won the most games!'))
    elif wins == 0:
        return(print(f'{player1} and {player2} neither of you won'))

        

main()