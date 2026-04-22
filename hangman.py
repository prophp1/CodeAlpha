import random

words = ["apple", "tiger", "chair", "plant", "house"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("🎉 You win! Word was:", word)
else:
    print("❌ You lost! Word was:", word)