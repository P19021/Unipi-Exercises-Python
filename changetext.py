def main():	
	filename=input("Enter a file's name: ")#dont forget to add the .txt suffix
	filename=str(filename)
	text=open(filename,"rt")#opens the text
	splitter=text.read()#saves the text to a list
	text.close()
	splitter=splitter.split(' ')#seperates the text to words
	textlength=len(splitter)
	word=[]

	for i in range(textlength):
		word=splitter[i]#word's value is the current word in the text
		if len(splitter[i])>3:
			helper2=list(word)#creating a list with all the characters included in the word
			comma=helper2.count(',')#checks if after the word there is a comma(,) or a period (.)
			period=helper2.count('.')
			counter=len(helper2)
			counter=int(counter)-1
			if comma==1 or period==1:#if there is, it is removed 
				helper2.pop(-1)
				word=""
				for j in range(counter):#and the word is made a string again, so the suffix is now able to be added to it
					word=word+helper2[j]
			helper=word[0]#taking the first letter
			suffix=helper+'ay'#adding "ay"
			word=word+suffix#adding the suffix to the word
			helper2=list(word)#creating a list with all the characters included in the word after adding the suffix
			helper2.pop(0)#removing the first letter 
			word=""#making the word a blank character, to add all the characters and make it a string
			counter=len(helper2)
			counter=int(counter)
			for j in range(counter):
				word=word+helper2[j]#the word is now made a string in its final form
			if comma>0:#if the word originally contained a comma or a period, it's added to the suffix
				word=word+','
			if period>0:
				word=word+'.'		
		splitter[i]=word#the word is finally being changed in the list

	counter2=len(splitter)
	counter2=int(counter2)
	finaltext=""
	for i in range(counter2):#here the items of the list are combined to make a string, which is the new text in its final form 
		finaltext=finaltext+splitter[i]+" "	
	print("Your new text is: \n",finaltext)	
	text=open(filename,"w")
	text.write(finaltext)#changing the text in the file
	text.close()#closing the text	
		
main()
