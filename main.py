import random
words = ['Dog', 'Cat', 'Boy', 'Chair', 'Muscles', 'Crazy', 'Chakra']
word_to_guess = words[random.randint(0, len(words)-1)]
mistakes = 5
print(word_to_guess[0] + " " + " " + word_to_guess[-1])
guess_letter = input("Try a letter")
while not guess_letter.islower() or len(guess_letter) > 1:
    print("Invalid input")
    guess_letter = input("Try a letter")
correct = len(word_to_guess)
count = 2
while mistakes != 0:
    if guess_letter in word_to_guess:
        count = count+1
        if correct-count > 0:
            print(guess_letter + " is the " + str(word_to_guess.index(guess_letter) + 1) + " letter")
            print(str(correct - count) + " letters to go")
            print("You did " + str(5-mistakes) + " mistakes by now")
    else:
        print("Wrong guess")
        mistakes = mistakes-1
        print("You did " + str(5 - mistakes) + " mistakes by now")
    if count == correct and mistakes != 0:
        print("Congrats! The word was " + word_to_guess)
        break
    guess_letter = input("Try a letter")
    while not guess_letter.islower() or len(guess_letter) > 1:
        print("Invalid input")
        guess_letter = input("Try a letter")
if mistakes == 0:
    print("You lost! Better luck next time!The word was:" + word_to_guess)
