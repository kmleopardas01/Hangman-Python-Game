import os,random, time

def start():
	print("\n")
	print("\t"*3 + ".-------------------------------------------------------------------.")
	time.sleep(.20)
	print("\t"*3 + "|                                                                   |")
	time.sleep(.20)
	print("\t"*3 + "|                          .===========.                            |")
	time.sleep(.20)
	print("\t"*3 + "|                          []         ||                            |")
	print("\t"*3 + "|                          []                                       |")
	time.sleep(.20)
	print("\t"*3 + "|                          []       (-.-)                           |")
	print("\t"*3 + "|                          []                                       |")
	time.sleep(.20)
	print("\t"*3 + "|                          []       * | *                           |") 
	time.sleep(.20)
	print("\t"*3 + "|                          []      *  |  *                          |")
	time.sleep(.20)
	print("\t"*3 + "|                          []    *    |    *                        |")
	time.sleep(.20)
	print("\t"*3 + "|                          []        * *                            |") 
	time.sleep(.20)
	print("\t"*3 + "|                          []       *   *                           |")
	time.sleep(.20)
	print("\t"*3 + "|                          []     *       *                         |")
	time.sleep(.20)
	print("\t"*3 + "|                                                                   |")
	time.sleep(.20)
	print("\t"*3 + "|                           HANGMAN GAME                            |") 
	time.sleep(.20)
	print("\t"*3 + "|                                                                   |")
	time.sleep(.20)
	print("\t"*3 + "|                       KIRBY M. LEOPARDAS  ST3L                    |")
	time.sleep(.20)
	print("\t"*3 + "'-------------------------------------------------------------------'")
	print("\n")
def mainmenu():
	print("\n")
	print("\t"*3 + ".-------------------------------------------------------------------.")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "|                            MAIN MENU                              |")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "|                     [1] PLAY GAME                                 |")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "|                     [2] INSTRUCTIONS                              |")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "|                     [3] HIGH SCORES                               |")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "|                     [4] ABOUT THE GAME                            |")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "|                     [5] EXIT                                      |")
	print("\t"*3 + "|                                                                   |")
	print("\t"*3 + "'-------------------------------------------------------------------'")	    	
def categories():
	print("\n")
	print("\t"*3 + ".-------------------------------------------------------------------------------------.")
	print("\t"*3 + "|                                                                                     |")
	print("\t"*3 + "|                               C A T E G O R I E S                                   |")
	print("\t"*3 + "|                                                                                     |")
	print("\t"*3 + "|      EASY               AVERAGE               HARD                   Extreme        |")
	print("\t"*3 + "|   (1 point)            (3 points)           (5 points)              (7 points)      |")
	print("\t"*3 + "|                                                                                     |")
	print("\t"*3 + "|  [1] Animals          [5] Songs          [9] Countries             [13] PH Places   |")
	print("\t"*3 + "|                                                                                     |")	
	print("\t"*3 + "|  [2] Fruits           [6] Movies         [10] Cartoon Characters   [14] Astronomy   |")
	print("\t"*3 + "|                                                                                     |")
	print("\t"*3 + "|  [3] Dogs             [7] Happy Synonym  [11] Kitchen Items        [15] Sports      |")
	print("\t"*3 + "|                                                                                     |")
	print("\t"*3 + "|  [4] Cats             [8] Cars           [12] Body                 [16] Currencies  |")
	print("\t"*3 + "|                                                                                     |")
	print("\t"*3 + "|                        CHOOSE WISELY! ENJOY GUESSING!                               |")
	print("\t"*3 + "'-------------------------------------------------------------------------------------'")	
def about():
	print("\n")
	print("\t"*3 +".-------------------------------------------------------------------.")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"|                        ABOUT THE GAME                             |")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"|           Hangman is a classic paper and pencil game.             |") 
	print("\t"*3 +"|           This is a game where a player guesses a hidden          |")
	print("\t"*3 +"|           word by suggesting letters, within a certain            |")
	print("\t"*3 +"|           number of guesses.                                      |")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"'-------------------------------------------------------------------'")
	print("\t"*3 +"\n")	
def instructions():
	print("\n")
	print("\t"*3 +".===================================================================================.")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                        INSTRUCTIONS                                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Choose a category under the difficulties.                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"'==================================================================================='")
	print("\n")
	print("\t"*3 +"Press Enter key to continue...")
	input()
	os.system("CLS")
	print("\n")
	print("\t"*3 +".===================================================================================.")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                        INSTRUCTIONS                                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Choose a category under the difficulties.                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Enter the guess letter.                                                 |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"'==================================================================================='")
	print("\t"*3 +"\n")
	print("\t"*3 +"Press Enter key to continue...")
	input()
	os.system("CLS")
	print("\n")
	print("\t"*3 +".===================================================================================.")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                        INSTRUCTIONS                                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Choose a category under the difficulties.                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Enter the guess letter.                                                 |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> You may only enter letters and refrain from using other characters.     |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"'==================================================================================='")
	print("\n")
	print("\t"*3 +"Press Enter key to continue...")
	input()
	os.system("CLS")
	print("\n")
	print("\t"*3 +".===================================================================================.")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                        INSTRUCTIONS                                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Choose a category under the difficulties.                               |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Enter the guess letter.                                                 |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> You may only enter letters and refrain from using other characters.     |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|        -> Each round you may only commit 5 errors, otherwise                      |")
	print("\t"*3 +"|           the game is over.                                                       |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"|                                                                                   |")
	print("\t"*3 +"'==================================================================================='")
	print("\n")
	print("\t"*3 +"Press Enter key to continue...")
	input()
	os.system("CLS")
	print("\n")
	print("\t"*3 +".====================================================================================.")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"|                        INSTRUCTIONS                                                |")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"|        -> Choose a category under the difficulties.                                |")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"|        -> Enter the guess letter.                                                  |")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"|        -> You may only enter letters and refrain from using other characters.      |")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"|        -> Each round you may only commit 5 errors, otherwise                       |")
	print("\t"*3 +"|           the game is over.                                                        |")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"|        -> If you guess the word you may play again until                           |")
	print("\t"*3 +"|           the game is over.                                                        |")
	print("\t"*3 +"|                                                                                    |")
	print("\t"*3 +"'==================================================================================='")
	print("\n")	
def hangman(guess):
	if guess == 0:
		print("\n")
		print("\t"*3 +"====================================================================.")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                          .-------.                                |")     
		print("\t"*3 +"|                          |       |                                |")
		print("\t"*3 +"|                          |                                        |") 
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|      HAVE A GOOD GAME!   |                                        |")
		print("\t"*3 +"|                          |                                        |") 
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"'===================================================================='")
		print("\n")
	elif guess == 1:
		print("\n")
		print("\t"*3 +".===================================================================.")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                          .-------.                                |")     
		print("\t"*3 +"|                          |       |                                |")
		print("\t"*3 +"|                          |      ( )                               |") 
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|       COME ON!           |                                        |")
		print("\t"*3 +"|                          |                                        |") 
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"'==================================================================='")
		print("\n")
	elif guess == 2:
		print("\n")
		print("\t"*3 +".===================================================================.")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                          .-------.                                |")     
		print("\t"*3 +"|                          |       |                                |")
		print("\t"*3 +"|                          |      ( )                               |") 
		print("\t"*3 +"|                          |     * |                                |")
		print("\t"*3 +"|     YOU CAN DO IT!       |    *  |                                |")
		print("\t"*3 +"|                          |                                        |") 
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"'==================================================================='")
		print("\n")
	elif guess == 3:
		print("\n")
		print("\t"*3 +".===================================================================.")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                          .-------.                                |")     
		print("\t"*3 +"|                          |       |                                |")
		print("\t"*3 +"|                          |      ( )                               |") 
		print("\t"*3 +"|                          |     * | *                              |")
		print("\t"*3 +"|     DON'T KILL ME HERE!  |    *  |  *                             |")
		print("\t"*3 +"|                          |                                        |") 
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"'==================================================================='")
		print("\n")
	elif guess == 4:
		print("\n")
		print("\t"*3 +".===================================================================.")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                          .-------.                                |")     
		print("\t"*3 +"|                          |       |                                |")
		print("\t"*3 +"|                          |      ( )                               |") 
		print("\t"*3 +"|                          |     * | *                              |")
		print("\t"*3 +"|   CAN'T YOU GUESS IT?    |    *  |  *                             |")
		print("\t"*3 +"|                          |      *                                 |") 
		print("\t"*3 +"|                          |     *                                  |")
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"'==================================================================='")
		print("\n")
	else:
		print("\n")
		print("\t"*3 +".===================================================================.")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                          .-------.                                |")     
		print("\t"*3 +"|                          |       |                                |")
		print("\t"*3 +"|                          |      ( )                               |") 
		print("\t"*3 +"|                          |     * | *                              |")
		print("\t"*3 +"|    OH BYE! I'M DEAD!     |    *  |  *                             |")
		print("\t"*3 +"|                          |      * *                               |") 
		print("\t"*3 +"|                          |     *   *                              |")
		print("\t"*3 +"|                          |                                        |")
		print("\t"*3 +"|                                                                   |")
		print("\t"*3 +"|                         G A M E  O V E R                          |")
		print("\t"*3 +"'==================================================================='")
		print("\n")
def blank_spaces(hangword):
	list_letters = []
	for a in c:
		list_letters.append()
	return list_letters	
def progress_updater(guesses, the_word, progress):
	i = 0
	while i < len(the_word):
		if guesses == the_word[i]:
			progress[i] = guesses
			i = i + 1
		else:
			i = i + 1
	return print(progress)			
def play_again(score,hangword):
	print("\n")
	print("\t"*3 +".===================================================================.")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"|                    DO YOU WANT TO PLAY AGAIN?                     |")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"|                           [1] YES                                 |")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"|                           [2] NO                                  |")
	print("\t"*3 +"|                                                                   |")
	print("\t"*3 +"'==================================================================='")
	print("\n")
	y = input("Enter choice: ")
	print("\n")
	if y == "1":
		os.system("CLS")
		play(score)
	elif y == "2":
		
		if score == 0:
			os.system("CLS")
			showhscore()
			print("Thank you for playing!")
			input()
			quit()
			
		else:
			highscore(score)
			os.system("CLS")
			showhscore()
			print("\n")
			print("Thank you for playing!")
			input()
			quit()
			
	else:
		print("INVALID INPUT")
		print("Press Enter key to continue...")
		input()
		os.system("CLS")
		play_again(score,hangword)					
def highscore(score):
	hscore = open("Highscore.txt","a")
	name = ""
	while len(name) != 3:
		name = input("Enter name: [_] [_] [_] ")
	hscore.write(str(score)+ "|" + name + "\n")
	hscore.close()	
def showhscore():
	with open("Highscore.txt") as showhscore:
		record = []
		for line in showhscore:
			line = line[:-1]
			tokens = line.split("|")

			name = tokens[1]
			score = tokens[0]

			
			player = {}
			player["name"] = name
			player["score"] = int(score)
			record.append(player)
	
	sortshowhscore = sorted(record, key = lambda i: i['score'],reverse=True) 
	print("\n")
	print("\t"*3 +".===================================================================")
	print("\t"*3 +"                                                                    ")
	print("\t"*3 +"                    H A L L   O F   F A M E R S                         ")
	print("\t"*3 +"                                                                    ")   

	for i in range(len(sortshowhscore)):
		for key,value in sortshowhscore[i].items():
			print("                                     "+str(value)+"  ", end='')
		print("")
 
	print("\t"*3 +"                                                                    ")    
	print("\t"*3 +"                                                                    ")   
	print("\t"*3 +"====================================================================")
	print("\n")
def game(score,hangword,category):
	guess = 0
	letters_used = ""
	the_word = list_letters(hangword)
	progress = []
	for i in range(len(the_word)):
		progress.append('_')
	
	
	while guess != 5:
		os.system("CLS")
		hangman(guess)
		print(progress)
		print("The letter(s) used is/are: ", letters_used)
		guesses = input("Guess a letter: ").capitalize()
		print("\n")
		if guesses in the_word and guesses not in letters_used:
			print("Your guess is right!")
			letters_used += guesses + " "
			
			progress_updater(guesses,the_word,progress)
			
			
		elif guesses not in the_word and guesses not in letters_used:
			guess += 1
			print("Your guess is wrong!")
			letters_used += guesses + " "
			
			progress_updater(guesses,the_word,progress)
			
			
		else:
			print("You used that letter already!")
			print("Try again!")
			print("Press Enter key to continue...")
			input()
			
		if progress == the_word:
			os.system("CLS")
			if category == "1" or category == "2" or category=="3" or category=="4":
				score = score + 1	
			elif category == "5" or category == "6" or category=="7" or category=="8":
				score = score + 3
			elif category == "9" or category == "10" or category =="11" or category=="12":
				score = score + 5	
			elif category == "13" or category == "14" or category =="15"or category=="16":
				score = score + 7
			print("\n")
			print("\t"*3 +".-------------------------------------------------------------------.")
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"|               Congratulations! You guess the word!                |")
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"|                     Your score is: ",score,"                           |")
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"'-------------------------------------------------------------------'")
			print("\n")
			print("Press Enter key to continue...")
			input()
			os.system("CLS")
			play_again(score,hangword)
		elif guess == 5:
			os.system("CLS")
			print("\n")
			print("\t"*3 +".-------------------------------------------------------------------.")
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"|                *****    *****   **    **  *******                 |")
			print("\t"*3 +"|               *     *  *     *  * *  * *  *                       |")
			print("\t"*3 +"|               *        *     *  *  **  *  ****                    |") 
			print("\t"*3 +"|               *   ***  *******  *  **  *  *                       |")
			print("\t"*3 +"|               *     *  *     *  *      *  *                       |")
			print("\t"*3 +"|                *****   *     *  *      *  *******                 |") 
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"|                *****   *     *  *******   ******                  |")
			print("\t"*3 +"|               *     *  *     *  *         *     *                 |")
			print("\t"*3 +"|               *     *  *     *  ****      *     *                 |")
			print("\t"*3 +"|               *     *   *   *   *         ******                  |")
			print("\t"*3 +"|               *     *    * *    *         *     *                 |")
			print("\t"*3 +"|                *****      *     *******   *      *                |")
			print("\t"*3 +"|                                                                   |")
			print("\t"*3 +"'-------------------------------------------------------------------'")
			print("\n")
			print("The word is",end=" ")
			for a in the_word:
			   print(a.capitalize(),end="")
			print("\nYour Score is: ",score)
			
			print("Press Enter key to continue...")
			input()
			if score == 0:
				os.system("CLS")
				showhscore()
			else:
				highscore(score)
				os.system("CLS")
				showhscore()
				print("\n")
		
			print("Thank you for playing!")
			input()
			break
		
	os.system("CLS")
	mainmenu()
	choice = input("Enter your choice: ")
	mainmenu_choice(choice)					
def mainmenu_choice(choice):
	score = 0
	if choice == "5":
		input()
		quit()
	elif choice == "4":
		os.system("CLS")
		about()
		print("Press Enter key to go back to Main Menu...")
		input()
		os.system("CLS")
		
	elif choice == "2":
		os.system("CLS")
		instructions()
		print("Press Enter key to go back to Main Menu...")
		input()
		os.system("CLS")	
		
	elif choice == "3":
		os.system("CLS")
		showhscore()
		print("Press Enter key to go back to Main Menu...")
		input()
		os.system("CLS")	
	
	elif choice == "1":
		os.system("CLS")
		play(score)
		
	else:
		print("INVALID INPUT")
		print("Press Enter key to continue...")
		input()
		os.system("CLS")		
def list_letters(hangword):
	list_letters=[]
	for a in hangword:
		list_letters.append(a)
	return list_letters		
def play(score):
	categories()
	category = input("Choose a category: ")
	if category == "1":
		animals = []
		readhandle = open("Animals.txt","r")
		for line in readhandle:
			line = line.strip()
			animals.append(line)
		readhandle.close()
	
		hangword = random.choice(animals)
		game(score,hangword,category)
			
			
	elif category == "2":
		fruits = []
		readhandle = open("Fruits.txt","r")
		for line in readhandle:
			line = line.strip()
			fruits.append(line)
		readhandle.close()
	
		hangword = random.choice(fruits)
		game(score,hangword,category)
		
	elif category == "3":
		dogs = []
		readhandle = open("Dogs.txt","r")
		for line in readhandle:
			line = line.strip()
			dogs.append(line)
		readhandle.close()
		
		hangword = random.choice(dogs)
		game(score,hangword,category)
				
	elif category == "4":
		cats = []
		readhandle = open("Cats.txt","r")
		for line in readhandle:
			line = line.strip()
			cats.append(line)
		readhandle.close()
				
		hangword = random.choice(cats)
		game(score,hangword,category)
				
	elif category == "5":
		songs = []
		readhandle = open("Songs.txt","r")
		for line in readhandle:
			line = line.strip()
			songs.append(line)
		readhandle.close()
				
		hangword = random.choice(songs)
		game(score,hangword,category)
		
	elif category == "6":
		movies = []
		readhandle = open("Movies.txt","r")
		for line in readhandle:
			line = line.strip()
			movies.append(line)
		readhandle.close()
				
		hangword = random.choice(movies)
		game(score,hangword,category)

	elif category == "7":
		happySyn = []
		readhandle = open("HappySynonym.txt","r")
		for line in readhandle:
			line = line.strip()
			happySyn.append(line)
		readhandle.close()
				
		hangword = random.choice(happySyn)
		game(score,hangword,category)

	elif category == "8":
		cars = []
		readhandle = open("Cars.txt","r")
		for line in readhandle:
			line = line.strip()
			cars.append(line)
		readhandle.close()
				
		hangword = random.choice(cars)
		game(score,hangword,category)

	elif category == "9":
		countries = []
		readhandle = open("Countries.txt","r")
		for line in readhandle:
			line = line.strip()
			countries.append(line)
		readhandle.close()
				
		hangword = random.choice(countries)
		game(score,hangword,category)

	elif category == "10":
		cartoon = []
		readhandle = open("CartoonCharacters.txt","r")
		for line in readhandle:
			line = line.strip()
			cartoon.append(line)
		readhandle.close()
				
		hangword = random.choice(cartoon)
		game(score,hangword,category)

	elif category == "11":
		kitchenItems = []
		readhandle = open("Kitchen Items.txt","r")
		for line in readhandle:
			line = line.strip()
			kitchenItems.append(line)
		readhandle.close()
				
		hangword = random.choice(kitchenItems)
		game(score,hangword,category)

	elif category == "12":
		body = []
		readhandle = open("Body.txt","r")
		for line in readhandle:
			line = line.strip()
			body.append(line)
		readhandle.close()
				
		hangword = random.choice(body)
		game(score,hangword,category)

	elif category == "13":
		places = []
		readhandle = open("PHPlaces.txt","r")
		for line in readhandle:
			line = line.strip()
			places.append(line)
		readhandle.close()
				
		hangword = random.choice(places)
		game(score,hangword,category)

	elif category == "14":
		astro = []
		readhandle = open("Astronomy.txt","r")
		for line in readhandle:
			line = line.strip()
			astro.append(line)
		readhandle.close()
				
		hangword = random.choice(astro)
		game(score,hangword,category)

	elif category == "15":
		sports = []
		readhandle = open("Sports.txt","r")
		for line in readhandle:
			line = line.strip()
			sports.append(line)
		readhandle.close()
				
		hangword = random.choice(sports)
		game(score,hangword,category)

	elif category == "16":
		currencies = []
		readhandle = open("Currencies.txt","r")
		for line in readhandle:
			line = line.strip()
			currencies.append(line)
		readhandle.close()
				
		hangword = random.choice(currencies)
		game(score,hangword,category)
	
	else:
		print("INVALID INPUT")
		print("Press Enter to continue...")
		input()
		os.system("CLS")
		play(score)

	
	
	
	
	
	
	
	
	
	
                

