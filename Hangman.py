sRealWord = input("Write the Hangman Word in Capital Letters!")
lShownWord = ["_"] * len(sRealWord)
sInput = ""
iAllowedGuesses = 10
iLetterNumber = 0
iRightGuesses = 0

#Prevents new player from being shown the selected word to guess
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("And so the games begin! You have 10 guesses! Type END to end the game!")


while (sInput != "END" and iAllowedGuesses != 0):
	print("The word you're looking for is! ") + str(lShownWord)
	print("You have") + str(iAllowedGuesses) + ("guesses left")
	sInput = raw_input("Enter your guess in Capital Letters!:  ")

	while (iLetterNumber < len(sRealWord)):
		if (sRealWord[iLetterNumber] == sInput):
			lShownWord[iLetterNumber] = sInput
			iRightGuesses += 1
			iLetterNumber += 1

#Taking down letter number and giving a new guess option again
	iAllowedGuesses -= 1
	iLetterNumber = 0

	if(iRightGuesses == len(sRealWord)):
		print("Woohoo! You won the game!")
		break

	if(iAllowedGuesses == 0):
		print("Sorry, you're out of guesses... Game Over!")

