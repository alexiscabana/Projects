#returns a boolean indicating if the string in argument is a palindrome
def checkPalin(s):
	palin=True	
	i=0
	while i in range(len(s)/2) and palin:
		if s[i]!=s[len(s)-1-i]:
			palin=False
		i+=1
	return palin

