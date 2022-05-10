import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words = ('аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон'
    ' выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот '
    'корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось '
    'лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца'
    ' окунь олень орел осел панда паук питон попугай пума семга скунс собака'
    ' сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица').split()

def getRandomWord(wordList):
    # This function returns a random string from the given list.
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("*******************\nIncorrect letters:", end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    print("SW:", end='')

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace gaps with guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Shows the secret word with gasps between letters
        print(letter, end=' ')
    print()
    print("\n")

def getGuess(alreadyGuessed):
    # Return letter that player wrote down. This function checks, that player 
    # wrote down only one letter and nothing more
        while True:
            print("*******************\nEnter the letter: ")
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print("Enter only one letter, please.")
            elif guess in alreadyGuessed:
                print("You've already entered this letter. Choose another one.")
            elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
                print("Please, enter the LETTER.")
            else:
                return guess

def playAgain():
    # This function returns True in case a player wants to play again. 
    # In other case it returns False
    print("Do you want to play again? (да/нет)")
    return input().lower().startswith('д')

print("*******************\n*** > HANGMAN < ***\n"
    "*******************")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Allows the player to enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check whether the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print("YES! The secret word - " + secretWord + "! You've guessed!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check, whether the player has exceeded the quantity of attempts.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНе угадано букв:'
                ' ' + str(len(missedLetters)) + ' и угадано букв:'
                ' ' + str(len(correctLetters)) + '. Было загадано'
                ' слово "' + secretWord + '".')
            gameIsDone = True

    # Asks if the player wants to play again (only if the game is over).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
