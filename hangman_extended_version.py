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
       ===''', '''
    +---+
   [O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
   [O]  |
   /|\  |
   / \  |
       ===''']
words = {'Кольори': 'червоний оранжовий жовтий зелений синій блакитний фіолетовий'
    ' білий чорний коричневий'.split(),
    'Фігури ': 'квадрат трикутник прямокутник круг еліпс ромб трапеція'
    ' паралелограм пятикутник шестикутник восьмикутник'.split(),
    'Фрукти ': 'яблуко апельсин лимон лайм груша мандарин виноград грейпфрут'
    ' персик банан абрикос манго малина світі маракуйя нектарин'.split(),
    'Тварини': 'лелека акула бабуін баран борсук бобер бик верблюд вовк горобець'
    ' ворона видра голуб гусак жаба зебра змія індик кит кобра коза козел койот'
    ' корова кішка кролик криса куриця лама лебідь лев лисиця лосось лось мойва'
    ' пугач ведмідь моллюск міль мураха миша нірка носоріг мавпа овечка їжачок'
    ' окунь олень орел віслюк панда пантера павук пітон вуж папуга пума скунс'
    ' собака лосось пава сова тигр тритон тюлень качка форель тхореня черепаха'
    ' ястріб ящірка'.split()}

def getRandomWord(wordDict):
    """This function returns a random string from the passed dictionary of lists 
    of strings, as well as the key."""

    # First, we randomly select a key from the dictionary:
    word_key = random.choice(list(wordDict.keys()))
    
    # Second, we randomly select a word from the list of keys in the dictionary:
    word_index = random.randint(0, len(wordDict[word_key])-1)

    return wordDict[word_key][word_index], word_key

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("*******************\nНевірні літери:", end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    print("СЛОВО:", end='')

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
            print("*******************\nУведіть літеру: ")
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print("Уведіть лише одну літеру, будь ласка.")
            elif guess in alreadyGuessed:
                print("Ви вже загадували цю літеру. Спробуйте іншу.")
            elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыіьэюя':
                print("Будь ласка, уведіть ЛІТЕРУ.")
            else:
                return guess

def playAgain():
    # This function returns True in case a player wants to play again. 
    # In other case it returns False
    print("Хочеш зіграти ще раз? (так/ні)")
    return input().lower().startswith('т')

print("*******************\n*** > HANGMAN < ***\n"
    "*******************")

diff = ' '
while diff not in 'ЛСВ':
    print('Оберіть рівень гри:\n\tЛ - Легкий,\n\tС - Середній,\n\tВ - Важкий')
    diff = input().upper()

if diff == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if diff == 'В':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretCat = getRandomWord(words)
gameIsDone = False

while True:
    print('*******************\n>>> Розпочнемо! <<<\n*******************\n'
        'Категорія словника:\n*** > '+ secretCat +'< ***\n'
        '*******************')
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
            print("\nВІРНО!\nЗагадане слово - " + secretWord + "!\nВи відгадали!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check, whether the player has exceeded the quantity of attempts.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Нажаль!\nВи вичерпали всі спроби!\nНевірних літер:'
                ' ' + str(len(missedLetters)) + '\nВідгадано літер:'
                ' ' + str(len(correctLetters)) + '.\nБуло загадано слово:'
                ' ' + secretWord + '.')
            gameIsDone = True

    # Asks if the player wants to play again (only if the game is over).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretCat = getRandomWord(words)
        else:
            break
