import time

def main ():

    #explain game
    #take in the amount of games players want to play and their names
    games, playerone, playertwo = instructions()

    #for every game they want to play
    #grid restarts each time
    for i in range(games):

        print(f'You are now playing game number {i+1}')

        grid = [[' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' '],
                ['~','~','~']]

        #this is the word randomly selected and its blanks
        time.sleep(2)
        word, secret, blanks = initializeBlanks()

        #run actual game
        getGuess(playerone, playertwo, blanks, word, secret, grid)

#explain how the game works
#take in number of games and names of players
def instructions():

    print('You will now play a game of snowman, which is hangman but with a snowman.')

    time.sleep(1)
    print('You are welcome to play as many games as you would like.')

    time.sleep(1)
    print('There will be two players playing.')

    time.sleep(1)
    playerone = str(input('Player one please enter your name:'))
    playertwo = str(input('Player two please enter your name:'))

    print('You will take turns guessing letters, if the letter you guess is correct you get another turn.')

    time.sleep(1)
    print('You are allowed five total wrong guesses.')

    time.sleep(1)
    games = int(input('How many games would you like to play?'))

    return(games, playerone, playertwo)

#randomly determine the word and create blanks
def initializeBlanks():

    import random
    import os

    #randomly choose word from seperate list of words
    word = (random.choice(open('/Users/sofiahirschmann/Desktop/Comp Sci/Midterm 2/words.txt','r').readline().split()))

    #record word as string
    #record word in secret as a list
    word = str(word)
    secret = list(word)

    #create blanks to be guessed
    blanks = ['_']*len(word)
    
    return(word, secret, blanks)

#print grid in an organized way on seperate lines
def display(grid):

   for i in grid:
       for j in i:
         print(j, end = "  ")
       print()

#dictionary for piece of snowman added with each wrong guess
def dict():

    snowman = {1 :[0,1,'O'], 
    2 :[1,1,'O'], 
    3 :[2,1,'O'], 
    4 :[1,0,'/'], 
    5 :[1,2,'\\']}

    return(snowman)

#using dictionary to trade spot in grid for piece of snowman when guessed wrong
def wrong_display(wrong, grid):

    #call function that holds keys
    snowman = dict()

    #call coordinates held in keys and values of snowman dictionary
    value = list(snowman[wrong])

    #use this information to alter grid
    grid[value[0]][value[1]] = value[2]

    return(grid)

#if letter is in word find index so that blank can be switched to guessed letter
def fillInBlanks(char, string, guess, blanks):

    #initialize index list
    index = []

    #find every place in word that contains guessed letter
    for i in range(len(string)):
        if char == (string[i]):
            index.append(i)

    #for each location of the letter change the blank in blanks to be that letter
    for number in index:
        blanks[number] = guess

    return(blanks)

#used in between guessing to report updated blanks and wrong guesses
def reportStatus(w, wrong, blanks):

    time.sleep(1)
    
    #report status of blanks as guessing continues
    print("This is the word you're guessing:")
    print(*blanks)

    time.sleep(1)

    #if letter have been added to the list fo wrong guesses 
    #report it to prevent repeated guesses
    if wrong > 0:
        print(f'The letters that have already been guessed incorrectly are {w}.')

#if game is done either congratulate whoever won or report that they both lost
def report(word, blanks, wrong, player):

    #ensure that there are either no more blanks or all wrong guesses have been used up
    if '_' not in blanks or wrong == 5:
        print(f'The correct word is {word}.')
        
        if '_' not in blanks:
            print(f'Congratulations {player} you won!')

        elif wrong == 5:
            print('You are both losers...')

#invalid guess check and fix
def valid(guess, Wrong_list, player):
    
    #if guess is in the alphabet
    if guess.isalpha():
        #ensure that it is lowercase
        guess = guess.lower()
    
        #if the letter has already been guessed wrong
        for letter in Wrong_list:

            #you get one chance to guess another letter that hasn't already been guessed
            if letter == guess:
                guess = input(f'{player} you have already guessed {guess} please guess another:')
        
        return(guess)
                
    #if guess not in the alphabet
    else:
        #guess again
        guess = input(f'{player} your guess was invalid please guess a letter:')

        #if this new guess is a letter carry on
        if guess.isalpha():
            return(guess)

        #if this new guess is still not a letter run the function again until it is one
        else:
            valid(guess, Wrong_list, player)

#if guessed correctly player gets another turn
def playAgain(player, word, wrong, Wrong_list, grid, blanks):

    #input next guess
    guess = input(f'{player} because you guessed correctly you are allowed another guess, enter your letter:')

    #ensure that guess is valid
    guess = str(valid(guess, Wrong_list, player))
        

    if guess not in word:

        #add to wrong count
        wrong += 1
        print('You guessed incorrectly.')
        
        #add to list of wrong guesses
        Wrong_list.append(guess)

        time.sleep(1)
        print('This is how the snowman looks now.')

        time.sleep(1)

        #display updated snowman
        grid = wrong_display(wrong, grid)
        display(grid)

    elif guess in word:

        print(f'Great job {player} you guessed a letter!')

        #update blanks with guessed letter
        blanks = fillInBlanks(guess, word, guess, blanks)

        time.sleep(1)

        #reveal updated blanks to user
        print(*blanks)

        #if there are still blanks the user can guess again
        #the function runs over
        if '_' in blanks:
            
            wrong, Wrong_list, grid, blanks = playAgain(player, word, wrong, Wrong_list, grid, blanks)

    return(wrong, Wrong_list, grid, blanks)

#the foundation of the guessing game
def getGuess(Player_1, Player_2, blanks, word, secret, grid):

    #initialize no wrong guesses
    wrong = 0

    #initialize empty wrong guess list
    Wrong_list = []
    
    #while loop goes on while there are blanks and the snowman is not complete
    while '_' in blanks and wrong < 5:
        
        #player 1 turn
        player = Player_1

        #report to player 1 the blanks and the list of wrong guesses before they make their guess
        reportStatus(Wrong_list, wrong, blanks)

        #plyer 1 input guess
        guess = input(f'{Player_1} guess a letter:')
        
        #ensure that guess is valid
        guess = str(valid(guess, Wrong_list, player))
        
            
        if guess not in word:

            #add to wrong count
            wrong += 1
            print('You guessed incorrectly.')
           
            #add to list of wrong guesses
            Wrong_list.append(guess)

            time.sleep(1)
            print('This is how the snowman looks now.')

            time.sleep(1)

            #display updated snowman
            grid = wrong_display(wrong, grid)
            display(grid)

        elif guess in word:

            print(f'Great job {player} you guessed a letter!')

            #update blanks with guessed letter
            blanks = fillInBlanks(guess, word, guess, blanks)

            time.sleep(1)

            #reveal updated blanks to user
            print(*blanks)

            #because player 1 guessed correctly they get to play again
            wrong, Wrong_list, grid, blanks = playAgain(player, word, wrong, Wrong_list, grid, blanks)

        #check whether game is done so that if it is player can be congratulated or told that they lost
        report(word, blanks, wrong, player)

        
        if '_' in blanks and wrong < 5:
            
            #player 2 turn
            player = Player_2
            
            #report to player 2 the blanks and the list of wrong guesses before they make their guess
            reportStatus(Wrong_list, wrong, blanks)

            #player 2 input guess
            guess = (input(f'{Player_2} guess a letter:'))

            #ensure that guess is valid
            guess = str(valid(guess, Wrong_list, player))


            #add to wrong list and adds to snowman
            if guess not in word:

                #add to wrong count
                wrong += 1
                print('You guessed incorrectly.')
           
                #add to list of wrong guesses
                Wrong_list.append(guess)

                time.sleep(1)
                print('This is how the snowman looks now.')

                time.sleep(1)

                #display updated snowman
                grid = wrong_display(wrong, grid)
                display(grid)

            elif guess in word:

                print(f'Great job {player} you guessed a letter!')

                #update blanks with guessed letter
                blanks = fillInBlanks(guess, word, guess, blanks)

                time.sleep(1)

                #reveal updated blanks to user
                print(*blanks)

                #because player 2 guessed correctly they get to play again
                wrong, Wrong_list, grid, blanks = playAgain(player, word, wrong, Wrong_list, grid, blanks)
                    
            #check whether game is done so that if it is player can be congratulated or told that they lost
            report(word, blanks, wrong, player)
    


main()
