import random
print("WELCOME Lets Start The Game\n🤝🏻 Good Luck ! ")
words = ["table fan","entry door","table mat","bed sheet","mechine chair","robotic car","refridgerator","football","basket ball" ]
word=random.choice(words)
hangman= ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
       |
      =====''', '''
   +---+
   O   |
   |   |
       |
       |
      =====''', '''
   +---+
   O   |
  /|   |
       |
       |
      =====''', '''
   +---+
   O   |
  /|\  |
   |   |
       |
      =====''', '''
  +---+
   O   |
  /|\  |
  /    |
       |
      =====''', '''
   +---+
   O   |
  /|\  |
  / \  |
       |
      =====''']
guesses =''
turns = 7
print('guess the word = ',end="")
while turns > 0:
    fails = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_",end="")
            fails += 1
    if fails == 0:
        print("THE WORD YOU GUESSED IS CORRECT")
        print("The word is: ", word)
        break
    guess = input("\nguess the word:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print(hangman[turns-1])
        print("entered word is Wrong")
        print("the remaining ", + turns, 'are left')
        if turns == 0:
            print("THE WORD YOU GUESSED IS INCORRECT")