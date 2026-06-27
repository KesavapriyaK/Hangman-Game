
import random

# List of predefined words
words = ["python", "apple", "computer", "school", "banana"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
wrong_guesses = 6

print("🎮 Welcome to Hangman!")

while wrong_guesses > 0:

    display = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses left:", wrong_guesses)

    # Check if the player has guessed the word
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        wrong_guesses -= 1

# If player loses
if wrong_guesses == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

