def main():	
	numb = input("Enter a number:")
	sdigit=False
	while sdigit==False:
		helper= int(numb)
		helper= helper*3
		print(numb,"* 3=",helper)
		helper= helper+1
		print(helper-1,"+ 1=",helper)
		numb= str(helper)
		final=0
		for i in range(len(numb)):
			helper2=numb[i]

			helper2=int(helper2)
			final=final + helper2
		
		numb= str(final)
		print("Adding the digits to themselves makes us ",numb)
		bit= len(numb)
		if bit==1:
			sdigit=True
			print("Finally,the number is single-digit! ")
		else:
			print("It still is not a single-digit!")
	return 0		

main()	



