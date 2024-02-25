import streamlit as st
import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon"]

def play_game(word):
    # Initialize variables
    guessed_letters = []
    attempts = 6
    guessed_word = ["_"] * len(word)

    # Main game loop
    while attempts > 0 and "_" in guessed_word:
        st.write(" ".join(guessed_word))
        guess = st.text_input("Guess a letter:")
        
        if guess in guessed_letters:
            st.write("You've already guessed that letter!")
            continue

        if guess in word:
            st.write("Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            st.write("Incorrect guess!")
            attempts -= 1
        
        guessed_letters.append(guess)
        st.write(f"Attempts left: {attempts}")

    # End of game
    if "_" not in guessed_word:
        st.write("Congratulations! You've guessed the word correctly.")
    else:
        st.write("Sorry, you've run out of attempts. The word was:", word)

def main():
    st.title("Word Guessing Game")
    st.write("Welcome to the Word Guessing Game!")
    st.write("Try to guess the word within 6 attempts.")

    # Randomly select a word from the list
    word = random.choice(words)

    play_game(word)

if __name__ == "__main__":
    main()
