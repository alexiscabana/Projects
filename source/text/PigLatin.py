#I'm following the rules from Wikipedia's official page

def pigLatin(word):
	if len(word)<1:
		return word
	
	if word[0] in 'aeiouh':
		return word+"way"
	#word begins with consonant
	i=0
	while word[i] not in 'aeiou':
		i+=1
	
	return word[i:]+word[:i]+"ay"

