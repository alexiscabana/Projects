#This program checks for the total throughput of each wireless and ethernet network card over the current session and their current bandwidth (up and down) by printing them to the console
#this program assumes 'netcat' is installed
import subprocess
CONST_IFCONFIG_DOWN_SUBSTR = "RX bytes:"
CONST_IFCONFIG_UP_SUBSTR = "TX bytes:"



#returns a tuple in the form (int downloaded, int uploaded) for a given network card (eth0,lo or wlan0)
def parseRxTx(networkCard):
	downstr = subprocess.check_output("cat /sys/class/net/"+networkCard+"/statistics/rx_bytes", shell=True)
	upstr = subprocess.check_output("cat /sys/class/net/"+networkCard+"/statistics/tx_bytes", shell=True)

	return int(downstr), int(upstr)

print parseRxTx("wlan0")
