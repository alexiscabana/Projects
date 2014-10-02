#non-recursive function to find the fibonacci serie to the Nth place, 0 being the first index in the streak

def findFib(n):
	nbs=[1,1]
	if n<2 and n>=0:
		return nbs[n]
	
	for i in range(0,n-1):
		nbs.append(sum(nbs[len(nbs)-2:len(nbs)]))
	return nbs[n]
	
print findFib(1500)
