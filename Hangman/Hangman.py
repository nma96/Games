import random

WordToBeGuessed = ""

def PickQuestion():
	global WordToBeGuessed
	file = open('QuestionList.txt').readlines()
	i = random.randrange(0, len(file) - 1)
	WordToBeGuessed = file[i][:-1].replace(" ", "")
	QuestionDictionary = {}
	for x in range(len(WordToBeGuessed)):
		if WordToBeGuessed[x] not in QuestionDictionary:
			QuestionDictionary[WordToBeGuessed[x]] = 1
		else:
			QuestionDictionary[WordToBeGuessed[x]] += 1
	return QuestionDictionary

def PlayGame(QuestionDictionary, maxTries):
	global WordToBeGuessed
	guessedWords = "_"*len(WordToBeGuessed)
	while maxTries > 0 and len(QuestionDictionary) != 0:
		#print(WordToBeGuessed)
		print('{} Tries left: {}'.format(guessedWords, maxTries))
		temp = input().lower()
		if temp in QuestionDictionary.keys():
			for i in range(QuestionDictionary[temp]):
				guessedWords = guessedWords[:WordToBeGuessed.index(temp)] + temp + guessedWords[WordToBeGuessed.index(temp)+1:]
				WordToBeGuessed = WordToBeGuessed[:WordToBeGuessed.index(temp)] +"_"+ WordToBeGuessed[WordToBeGuessed.index(temp)+1:]
			del QuestionDictionary[temp]
		else:
			maxTries -= 1
			print('Tries left: ' + str(maxTries))

def main():
	
	play = True

	while play:
		QuestionDictionary = PickQuestion()
		maxTries = 6
		PlayGame(QuestionDictionary, maxTries)
		print
		if maxTries <= 0:
			print("You are out of tries! \nYou Lose!")
		elif len(QuestionDictionary) == 0:
			print("\nYou win!!\n")
		play = True if input("Do you want to play again (y/n)? ").lower()=="y" else False


if __name__ == '__main__':
	main()