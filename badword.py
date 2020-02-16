def checkIfBad(txtword,gcons,bcons):
	counter=[]
	good=0
	bad=0
	for i in gcons:
		good=good+txtword.count(i)
	for i in bcons:
		counter.append(txtword.count(i))
	for i in counter:
		if i!=0:
			bad=bad+1
	if good>bad:
		check=False
		if bad==4:
			check=True
	else:
		check=True
	return check				


def main():	
	good_cons=["B","D","G","H","J","L","M","N","P","Q","S","T","V","X","Z","b","d","g","h","j","l","m","n","p","q","s","t","v","x","z"]
	bad_cons=["F","C","f","c","k","r"]
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
		isBad=checkIfBad(word,good_cons,bad_cons)
		if isBad==False:
			print("The word",word,'is not a "bad one"')
		else:
			print("The word",word,'is a "bad one"')	


main()