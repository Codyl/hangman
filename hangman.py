HIDDEN_WORD = 'hanged'
MAX_FAILED_ATTEMPTS = 6
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
failed_attempts = 0
letters_guessed = set(())
clipped_word = HIDDEN_WORD
while failed_attempts < MAX_FAILED_ATTEMPTS and clipped_word:
    guess_letter = input("What is your guess letter?")
    clipped_word = ' '.join(clipped_word.split(guess_letter))
    if guess_letter not in clipped_word:
        failed_attempts += 1
        print('Wrong letter! Try again.')
    else:
        letters_guessed.add(guess_letter)
    print(HANGMANPICS[failed_attempts])