#counts the number of words of the string in argument (implying a word is a series of letter(s) beggining and ending with a space)
def countWordsString(s):
	words=s.split(" ")
	cnt=0
	for word in words:
		if word!="" and word!="\t" and word!="\n":
			cnt+=1
	return cnt
	



#counts the number of words in a textfile whose name is passed in argument. assumption made is the same as above
def countWordsText(filename):
	f=open(filename)
	text=f.read()
	words=text.split(" ")
	cnt=0
	for word in words:
		if word!="" and word!="\t" and word!="\n":
			cnt+=1
	return cnt

#makes a summary of some of the words in a textfile (the word number in the file is associated with its conresponding word at every 'interval' number of words, 50 is default)
def generateSummary(filename,interval=50):
	f=open(filename)
	text=f.read()
	words=text.split(" ")
	cnt=0
	for word in words:
 		if word!="" and word!="\t" and word!="\n":
			if cnt%interval==0 or word==words[len(words)-1]:
				print words[cnt] + " is the word number %d" % cnt
			cnt+=1
	
