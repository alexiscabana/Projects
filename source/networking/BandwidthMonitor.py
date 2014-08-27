#This program checks for the total throughput of each wireless and ethernet network card over the current session and their current bandwidth (up and down) by printing them to the console
CONST_IFCONFIG_DOWN_SUBSTR = "RX bytes:"
CONST_IFCONFIG_UP_SUBSTR = "TX bytes:"

#returns a tuple in the form (int downloaded, int uploaded) for a given network card (eth0,lo or wlan0)
def parseIfconfig(outIfconfig,networkCard):
	networkCardConfig = outIfconfig[outIfconfig.find(networkCard):]

	indexDownload = networkCardConfig.find(CONST_IFCONFIG_DOWN_SUBSTR) + len(CONST_IFCONFIG_DOWN_SUBSTR) #find the index to begin the parse
	indexupload = networkCardConfig.find(CONST_IFCONFIG_UP_SUBSTR) + len(CONST_IFCONFIG_UP_SUBSTR)
	

	i=0
	downstr=""
	while networkCardConfig[indexDownload+i].isdigit(): #parsing the 'downloaded part'
		downstr+=networkCardConfig[indexDownload+i]
		i+=1
	
	i=0
	upstr=""
	while networkCardConfig[indexupload+i].isdigit(): #parsing the 'uploaded part'
		upstr+=networkCardConfig[indexupload+i]
		i+=1
	
	return int(downstr), int(upstr)



import subprocess
output = subprocess.check_output("ifconfig", shell=True)

print parseIfconfig(output,"wlan0")