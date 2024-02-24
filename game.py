import streamlit as st
user_name = input("Please enter your name: ")
hello = input("\nhey " +user_name + ", are you ready? " )
while hello.lower() == "no":
  print("\nso why are you here?! hehe")
  break
if hello.lower() == "yes":
  print("\nlet's start playing!")
  print('''\n\n You have 3 hints to the secret word, then you'll have to guess it.

# People like to eat it
# It's round
# It has a lot of cheese

        GOOD LUCK!
''')
  secret_word = ["pizza", "cucumber", "coffee", "Keyboard"]
  guess = input("enter your guess ")
  while guess != secret_word[0]:
    guess = input("It's not the correct word, please try again: ")
  if guess == secret_word[0]:
    print("well done!")
  another_game = str(input("Do you want to play another game?"))
  while another_game.lower() == "no": 
    print("\nso why are you here?! hehe")
    break
  if another_game.lower() == "yes":
    print("\nlet's start playing!")
    print('''\n\n You have 3 hints to the secret word, then you'll have to guess it.

# People like to eat it for breakfast
# It's green
# It has long shape

        GOOD LUCK!
''')
    guess = input("enter your guess ")
    while guess != secret_word[1]:
      guess = input("It's not the correct word, please try again: ")
    if guess == secret_word[1]:
      print("well done!")
    another_game = str(input("Do you want to play another game?"))
    while another_game.lower() == "no": 
      print("\nso why are you here?! hehe")
      break
    if another_game.lower() == "yes":
      print("\nlet's start playing!")
      print('''\n\n You have 3 hints to the secret word, then you'll have to guess it.

# People like drinking it to feel more awake
# It's brown
# It has srong smell

        GOOD LUCK!
''')
      guess = input("enter your guess ")
      while guess != secret_word[2]:
        guess = input("It's not the correct word, please try again: ")
      if guess == secret_word[2]:
        print("well done!")
    another_game = str(input("Do you want to play another game?"))
    while another_game.lower() == "no": 
      print("\nso why are you here?! hehe")
      break
    if another_game.lower() == "yes":
      print("\nlet's start playing!")
      print('''\n\n You have 3 hints to the secret word, then you'll have to guess it.

#People usually use me for writting or typing
#I have 104 keys
#I have some special keys for special purposes

        GOOD LUCK!
''')
      guess = input("enter your guess ")
      while guess != secret_word[3]:
        guess = input("It's not the correct word, please try again: ")
      if guess == secret_word[3]:
        print("well done!")
print("\nYou do not have need to test, Game Over")
