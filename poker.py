#ranking:
#rank 9=Straight Flush
#rank 8=4-Of-A-Kind
#rank 7=Full House
#rank 6=Flush
#rank 5=Straight
#rank 4=3-Of-A-Kind
#rank 3=2 Pairs
#rank 2=Pair
#rank 1=High Card

import random

def menu(): #creating a start menu 
	print("1.Start Game")
	print("2.Exit")
	check=False
	while check==False:
		entry=input("What would you like to do?\n")
		entry=str(entry)
		if entry != "1" and entry != "2":
			print("Please enter a valid option!\n")
		else:
			check=True
	if entry=="1":
		main()
	return 0					

def cntr(hand):
	counter=0
	for i in range(4):  #counts every time two cards of the same rank are recorded in hand.
		if hand[i][0]==hand[i+1][0]:
			counter=counter+1

	return counter

#If the counter is 3, this means that the player's hand is either 4 of a kind, or full house. 
#If the counter is 2, the possible hands are 3 of a kind and 2 pairs.
#If the counter is 1, the player has one pair in his hand.
#If the counter is 0, this means that there are no cards of similar rank in the player's hand. This means the possible type of hands are: flush, straight, straight flush or high card.

def handCount(hand,hdict): #counts how many times a card rank is found in a hand that is either 2 Pairs or 1 Pair
	counter=[]
	for i in hdict:
		counter.append(hand.count(hdict[i])) 
	return counter

def winCard(hand,rank): #determines the winning card in each type of hand, used as a tie breaker
	
	if rank==8 or rank==7 or rank==4:
		win=hand[2][0]
	elif rank==5 or rank==9 or rank==1 or rank==6:
		win=hand[4][0]
	else:
		win="null" #2 pairs and pair ties are not broken by a single card, therefore there is no winning card in these cases	  
	return win  


def findType(hand,hdict):
	counter=cntr(hand)
	if counter==3:
		for i in range(2):
			if hand[i][0]==hand[i+1][0] and hand[i][0]==hand[i+2][0] and hand[i][0]==hand[i+3][0]: # if 4 cards that have the same rank are found, its 4 of a kind.
				cardType="4 Of A Kind"
				rank=8
				
				break
			else: #if not, its full house
				cardType="Full House"
				
				rank=7
	elif counter==2:
		for i in range(3):
			if hand[i][0]==hand[i+1][0] and hand[i][0]==hand[i+2][0]:# if 3 cards that have the same rank are found, its 3 of a kind.
				cardType="3 Of A Kind"
				
				rank=4

				break
			else:#if not, its two pairs
				cardType="2 Pairs"
				
				rank=3
	elif counter==1:
		cardType="Pair"
		
		rank=2
	else:
		for i in range(4):
			if (hdict[hand[i+1][0]]-hdict[hand[i][0]])==1: #checks if all 5 cards are in order, which means the hand is straight
				strght=1
			else:
				strght=0
				break
					
		if strght==1:#if all 5 cards are in order then there are 2 possibilities:
			if hand[0][1]==hand[1][1] and hand[0][1]==hand[2][1] and hand[0][1]==hand[3][1] and hand[0][1]==hand[4][1]: #if those 5 cards are in order are also of the same suit, then the hand is Straight Flush
				cardType="Straight Flush"
				
				rank=9
			else: #if the cards are in order but not of the same suit, the hand is Straight
				cardType="Straight"
				
				rank=5
		elif hand[0][1]==hand[1][1] and hand[0][1]==hand[2][1] and hand[0][1]==hand[3][1] and hand[0][1]==hand[4][1]:#if all 5 cards belong to the same suit, then the hand is Flush
				cardType="Flush"
				
				rank=6
		else:
				cardType="High Card"#finally, if nothing of the above is true, the hand is the lowest possible, called High Card
				
				rank=1
	wcard=winCard(hand,rank)        

	return cardType,rank,wcard

def play(hdict,handP1,handP2,wcardP1,wcardP2,rankP1,rankP2,hlp1,hlp2):#this function will be used to determine the winner of the current round
	res="null" #giving value to the result
	if rankP1>rankP2: #the greater ranked type of hand wins
		res="win"
	elif rankP1<rankP2:
		res="loss"
	elif rankP1==rankP2:
		if handP1==handP2:
		#if both decks have exactly the same cards, it's a draw
		#thus we ensure that both players have different decks, even if their difference is a single card
			res="draw"
		else: #in case both players have the same type of hand but not the same cards, the tie must be broken using High Card rules(winning card)
			if rankP1==1 or rankP1==6:
				for i in range(4,1,-1):
					if hdict[handP1[i][0]]>hdict[handP2[i][0]]:
						res="win"
						break
					elif hdict[handP1[i][0]]<hdict[handP2[i][0]]:
						res="loss"
						break
			elif rankP1==7 or rankP1==4 or rankP1==8 or rankP1==5 or rankP1==9:
				if hdict[wcardP1]>hdict[wcardP2]:
					res="win"
				else:
					res="loss"
			elif rankP1==2: 
			#in this case, we cannot use the winning card to determine the winner, so we will check the strongest pair
			#if the pairs are the same between players too, we will check the remaining single cards
			#we have ensured that both players have different decks, even if their difference is a single card
				for i in range(4):
					if handP1[i][0]==handP1[i+1][0]:
						P1pair=hdict[handP1[i][0]]
					if handP2[i][0]==handP2[i+1][0]:
						P2pair=hdict[handP2[i][0]]  
				if P1pair>P2pair:
					res="win"
				elif P1pair<P2pair:
					res="loss"
				else:

					tie1=handCount(hlp1,hdict)
					tie2=handCount(hlp2,hdict)
				
					tieBreaker1=[]
					tieBreaker2=[]
					for i in range(13):
						if tie1[i]==1:
							tieBreaker1.append(i)
							
					for i in range(13):
						if tie2[i]==1:
							tieBreaker2.append(i)
								                          
					tieBreaker1.sort()
					tieBreaker2.sort()
					
					for i in range(3):
						if tieBreaker1[i]>tieBreaker2[i]:
							res="win"
							break
						elif tieBreaker1[i]<tieBreaker2[i]:
							res="loss"
							break	
			else:#same tactic applies to 2 pairs
				counter1=0
				counter2=0
				for i in range(4):
					if handP1[i][0]==handP1[i+1][0]:
						if counter1==0:
							P1pair1=hdict[handP1[i][0]]
							counter1=counter1+1
						else:
							P1pair2=hdict[handP1[i][0]] 
					if handP2[i][0]==handP2[i+1][0]:
						if counter2==0:
							P2pair1=hdict[handP2[i][0]]
							counter2=counter2+1
						else:   
							P2pair2=hdict[handP2[i][0]]                 
				if P1pair1>P2pair1:
					res="win"
				elif P1pair1<P2pair1:
					res="loss"
				else:
					if P1pair2>P2pair2:
						res="win"
					elif P1pair2<P2pair2:
						res="loss"
					else:   
						tie1_2=handCount(hlp1,hdict)
						tie2_2=handCount(hlp2,hdict)
						for i in range(13):
							if tie1_2[i]==1:
								tieBreaker1_2=i
								break
						for i in range(13):
							if tie2_2[i]==1:
								tieBreaker2_2=i
								break			
						if tieBreaker1_2>tieBreaker2_2:
							res="win"
						else:
							res="loss"	                          
	return res #returns the result of the current round 

	
	






def main():

	print("\n 5-CARD-DRAW POKER \n")
	suits =['♣','♦','♥','♠'] #list containing the four suits: Clubs, Diamonds, Hearts and Spades
	values =['2','3','4','5','6','7','8','9','10','J','Q','K','A']#list containing card rankings
	value_dict={"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"10":9,"J":10,"Q":11,"K":12,"A":13}
	card=[]
	for i in suits:
	
		for j in values:    
			card.append((j, i))  #creates a list named card, which contains every card's value and suit
	# print("Before shuffle",len(card),card)    
	# print("CV",card[1][0])

	ct=False

	while ct==False:  #game loop

		random.shuffle(card)  #shuffles the deck


		
		Player1Hand=[]
		Player2Hand=[]

		for i in range(10):    #distributes each players hand
			if i%2==0:
				Player1Hand.append(card[i])
			
			
			else:   
				Player2Hand.append(card[i])

		
	
		Player1Hand.sort(key=lambda x: value_dict[x[0]]) #Sorts list by ranking.  x[0] marks the position of each card's value we want to sort. value_dict[x[0]] gives the rank of each position.
		Player2Hand.sort(key=lambda x: value_dict[x[0]]) 

		# Player3Hand=[('5','♣'),('6','♣'),('8','♠'),('9','♣'),('A','♣')]
		# Player4Hand=[('6','♣'),('7','♣'),('9','♣'),('J','♠'),('K','♣')] 

		helper1=[]
		helper2=[]
		for i in range(5):
			helper1.append(Player1Hand[i][0])
			helper2.append(Player2Hand[i][0])

		ctypeP1,crankP1,winningCardP1=findType(Player1Hand,value_dict)
		ctypeP2,crankP2,winningCardP2=findType(Player2Hand,value_dict)
		
		

		print("This is your hand: ",Player1Hand)
		if crankP1==9:
			if winningCardP1=='A':
				print(" Congratulations! You have a Flush Royale!")
			elif winningCardP1=='K':
				print(" You have a King High Straight Flush")
			elif winningCardP1=='Q':
				print(" You have a Queen High Straight Flush")
			elif winningCardP1=='J':
				print(" You have a Jack High Straight Flush")	
			else:
				print(" You have a",winningCardP1," High Straight Flush!")
		elif crankP1==5:
			if winningCardP1=='A':
				print(" You have an Ace High Straight")
			elif winningCardP1=='K':
				print(" You have a King High Straight")
			elif winningCardP1=='Q':
				print(" You have a Queen High Straight")
			elif winningCardP1=='J':
				print(" You have a Jack High Straight")
			else:				
				print(" You have a",winningCardP1," High Straight")
		elif crankP1==3:
			print(" You have",ctypeP1)			
		else:				
			print(" You have a",ctypeP1)



		print("\nThis is Player 2's hand: ",Player2Hand)
		if crankP2==9:
			if winningCardP2=='A':
				print(" This is not your lucky day! Player 2 has a Flush Royale!")
			elif winningCardP2=='K':
				print(" Player 2 has a King High Straight Flush")
			elif winningCardP2=='Q':
				print(" Player 2 has a Queen High Straight Flush")
			elif winningCardP2=='J':
				print(" Player 2 has a Jack High Straight Flush")	
			else:
				print(" Player 2 has a",winningCardP2," High Straight Flush!")
		elif crankP2==5:
			if winningCardP2=='A':
				print(" Player 2 has an Ace High Straight")
			elif winningCardP2=='K':
				print(" Player 2 has a King High Straight")
			elif winningCardP2=='Q':
				print(" Player 2 has a Queen High Straight")
			elif winningCardP2=='J':
				print(" Player 2 has a Jack High Straight")
			else:				
				print(" Player 2 has a",winningCardP2," High Straight")
		elif crankP2==3:
			print(" Player 2 has",ctypeP2)		
		else:				
			print(" Player 2 has a",ctypeP2)
		

		endgame=play(value_dict,Player1Hand,Player2Hand,winningCardP1,winningCardP2,crankP1,crankP2,helper1,helper2)

		if endgame=="win":
			print("\nCongratulations! You Won This Round!")
		elif endgame=="loss":
			print("\nYou Lost this Round. Better Luck Next Time!")
		else:
			print("\nIt's A Draw!")

		
		checkpa=False
		while checkpa==False:
			print("\n1.Play Again")
			print("2.Exit Game")
			y=input()
			y=str(y)
			if y != "1" and y != "2":
				print("Please enter a valid option!\n")
			else:
				checkpa=True
		
		if y=="1":
			ct=False
		else:
			ct=True	
		

	return 0

menu()


	




