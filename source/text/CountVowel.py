#prints the number of time a certain vowel occurs in a given string

def countVowel(s):
	vowelCnt = {'a':0,'e':0,'i':0,'o':0,'u':0,}

	for ch in s.lower():
		if ch in vowelCnt.keys():
			vowelCnt[ch]+=1
	
print str(vowelCnt)
