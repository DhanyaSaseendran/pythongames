import random

listOfWords = ["mouse", "fan", "summer", "python", "lemon", 'human']

numberOfLives = 6
askedLetters = []

while numberOfLives > 0:
    wordToGuess = random.choice(listOfWords).upper()
    letter = input("pick a letter?").upper()
    askedLetters.append(letter)

    if letter in wordToGuess:
        print("Good guess")
    else:
        numberOfLives -= 1
        print(f'You have lost a life. You have {numberOfLives} lives left')
    print(f'word was {wordToGuess}')
    if numberOfLives == 0:
        print("                                       ")
        print("           ------------                ")
        print("           | /        |                ")
        print("           |/        (~)               ")
        print("           |          |                ")
        print("           |    ------------           ")
        print("           |          |                ")
        print("           |         / \               ")
        print("           |        /   \              ")
        print("           |       /     \             ")
        print("           |                           ")
        print("         __|__                         ")
