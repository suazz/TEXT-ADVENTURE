from sys import exit
print("""
 ===========Text Adventure ============ 
|                                      |
|          .---------.                 |
|          |.-------.|                 |
|          ||>run#  ||                 |
|          ||       ||                 |
|          |"-------'|                 |
|        .-^---------^-.               |
|        | ---~   ----~|               |
|        "-------------'               |
| * Written in : Python 3              |
| * Purpose: I'm bored                 |
| * Shouts out to: Yo mama!            |
|                             -henry s.|
 ======================================
""")

def room_1():
	print("There's a giant bear here eating a cheese cake.")
	print(f"What do you do {ask_user}?")
	print("")
	print("1. Take the cake")
	print("2. Scream at the bear")
	print("3. Fall to the floor and play dead")
	print("4. Grab your crotch and say \"Hey Bear mothafucka!\" ")
	print("5. Run!!!!")

	bear = input("> ")

	if bear == "1":
		print(f"The bear eats {ask_user}'s face off.  Good job!")
		print(" XX DEAD XX ")
	elif bear == "2":
		print(f"The bear eats {ask_user}'s legs off.  Good job!")
		print(" XX DEAD XX ")
	elif bear == "3":
		print(f"Bear says: \"Oldest trick in the book dumbass\" and crushes {ask_user}'s' skull")
		print(" XX DEAD XX ")
	elif bear == "4":
		print("Bear says: \"Oh very mature asshole!.\" Then he rips both arms off")
		print(" XX DEAD XX ")
	elif bear == "5":
		print(f"Good thing I though of running before that bear could mame me")
		print("""
	YOU WIN!!

	THANK YOU FOR PLAYING THIS
	CRAPY GAME
						    
	[copyright © 2020]
	""")
	restart_game()

def room_2():
	print("Ben Stiller is standing in a dojo"
		"\nhe looks like he wants to rumble")
	print("")
	print("Ben Stiller: \"Como esta bitches?\"")
	print("")
	print(f"What do you do {ask_user}?")
	print("")
	print("1. Sweep the legs!")
	print("2. Ask him: \"Do you have any idea who I am?\"")
	print("3. Kick him on the nuts!")
	print("4. Get close to him and say \"Hey what's that?\" then punch him on the face")
	print("5. Shake his hand")		

	response = input("> ")

	if response == "1" or response == "3":
		print(f"Ben Stiller dodges {ask_user}'s move, then stabs {ask_user} in the heart with a spear")
		print("Bad choice!")
	elif response == "2":
		print(f"(Ben Stiller says \"The guy I'm about to punch in the face\" [POOW!!]")
	elif response == "4":
		print(f"Ben Stiller does not fall for it and does a Round House kick on {ask_user} then says \"Do you how hard\
		\nit is to be really really good looking?\"")
	elif response == "5":
		print(f"Ben Stiller does not fall for it and kicks {ask_user} in the nuts then says \"Valla con Dios!\"   ")
	restart_game()

def room_3():
	print("OLD Thai lady is standing in a room very angry!")
	print("Make her smile!")
	print("")
	print(f"1.{ask_user} says: \"DOHMAH!\" ")
	print(f"2.{ask_user} says: \"What up shorty?\" ")
	print(f"3.{ask_user} says: \"want to PHO..K\" ")
	print(f"4.{ask_user} says: \"You give special massages?\"")
	print(f"5.{ask_user} says: \"Me so horny!\"")

	response = input("> ")

	if response == "1" or response == "3":
		print("Fuck you Bloody bastard!")
		print(f"{ask_user} you lose!")
	elif response == "2" or response == "4":
		print("She flicks you off")
		print(f"{ask_user} you lose!")
	else:
		print("I so horny too, let's go big boy!")
		print("""
	THE END!!

	THANK YOU FOR PLAYING THIS
	CRAPY GAME
						    
	[copyright © 2020]
	""")
	restart_game()

def room_4():
	print(f"{ask_user} enters a room with \"Toby\", \"Bin Laden\", \"Hitler\" ")
	print("")
	print(f"On {ask_user}'s' left there is a night stand with a gun on it")
	print(f"{ask_user} takes the gun but there is only one bullet")
	print("")
	print(f"What do you do {ask_user}?")
	print("1. Kill Toby")
	print("2. Kill Bind Laden")
	print("3. Kill Hitler")
	print("4. Lign them up and shoot them throught the throat")
	print("5. Curve the bullet to kill them all in one shot")

	kill = input("> ")

	if kill == "1":
		print(f"{ask_user} misses and just graze Tobys ear")
		print(" XX DAMM! XX ")
	elif kill == "2":
		print(f"{ask_user} killed Bin Laden but he goes to heaven and receives 32 virgin")
		print(" XX THAT BLOWS! XX ")
	elif kill == "3":
		print(f"{ask_user} kills Hitler, after Doc. Brown shows up in a Delorian and says \"You are not Marty!\"")
		print(" XX YOU LOSE? XX ")
	elif kill == "4":
		print("The bullet is a dud, and they all woop yo' ass!")
		print(" XX FUDGE! XX ")
	elif kill == "5":
		print(f"{ask_user} put tomuch curve and you shoot yourself in the nuts")
		print("""
	THE END!!

	THANK YOU FOR PLAYING THIS
	CRAPY GAME
						    
	[copyright © 2020]
	""")
	restart_game()

def room_5():
	print(f"{ask_user} bumps into some jerk and the jerk punches {ask_user}\
		\nin the face and knocks out a tooth. The police arrest you\
		\nand not the jerk.")
	print(f"A year later {ask_user} is working at a burger shop.")
	print("")
	print(f"The same cop that arrested you orders a burger")
	print(f"What do you do {ask_user}?")
	print("")
	print("1. Spit on the burger")
	print("2. Say: \"Do you remember me Asshole!\"")
	print("3. Quit the job")
	print("4. Jump over the counter and kick his ass!")
	print("5. Just make him his food")

	call_to_action = input("> ")

	if call_to_action == "1":
		print(f"As your are spitting on the burger, your manager is standing\
			\nbehind you[puzzled]")
		print(" XX YOUR FIRED! XX ")
	elif call_to_action == "2":
		print(f"The cop has no clue who you are")
		print("He orders a liter of Cola with his burger.")
		print(" XX DEAD XX ")
	elif call_to_action == "3":
		print(f"You yell \"I quit!\", as you leave, a drunk\
		\ncustomer comes in, bumps into you, punches you in the face.\
		\nthe cop arrest both of you. ")
		print(" XX THIS SUCKED! XX ")
	elif call_to_action == "4":
		print("The cops reflexes are good. He takes out his baton\
			\nwacks you in the head.")
		print(" XX YOU WAKE UP IN JAIL XX ")
	elif call_to_action == "5":
		print(f"The cop has a pickle allergy and he forgot to order\
			\nhis burger without them. The cop dies!")
		print("""
	YOU WIN!!

	THANK YOU FOR PLAYING THIS
	CRAPY GAME
						    
	[copyright © 2020]
	""")
	restart_game()

# Store the username
user_name = []
user_name.append(input)
ask_user = input("Hello!, what is your name?>  ")

#This is where the game start/restarts
def game_running():
	print("__________________________________________________")
	print(f"{ask_user} is in a room facing five doors") 
	print("")
	print("Do you go through door [#1] - [#2] - [#3] - [#4] ?")
	# print("Or")
	print("                       [#5] ")
	print("__________________________________________________")

	door = input("> ")
	#  These are all the rooms
	if door == "1":
		room_1()
	elif door == "2":
		room_2()
	elif door == "3":
		room_3()
	elif door == "4":
		room_4()
	elif door == "5":
		room_5()
	elif door == "6":
		room_6()
	elif door == "7":
		room_7()
	elif door == "8":
		room_8()

#  This func. is called to restart the game
def restart_game():
	print("Play again? y or n")
	replay = input("> ")
	print("")

	if replay == "y":
		game_running()
	elif replay == "n":
		exit(0)
		
game_running()