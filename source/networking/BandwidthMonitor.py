#This program checks for the total throughput of each wireless and ethernet network card over the current session and their current bandwidth (up and down) by printing them to the console
#this program assumes 'netcat' is installed
import subprocess
import sys
import time

downloadedBytes=0
uploadedBytes=0
oldTotalRX=0
oldTotalTX=0
CONST_TIME_SLEEP=0.5#seconds

#returns a tuple in the form (int downloadKBPS, int uploadKBPS) for a given network card (eth0,lo or wlan0 in most cases)
def getBandwidthRates(networkCard):
	downstr = subprocess.check_output("cat /sys/class/net/"+networkCard+"/statistics/rx_bytes", shell=True)#fetches total download in current session
	upstr = subprocess.check_output("cat /sys/class/net/"+networkCard+"/statistics/tx_bytes", shell=True)
	oldTotalRX = int(downstr)
	oldTotalTX = int(upstr)
	time.sleep(CONST_TIME_SLEEP)#seconds
	
	downstr = subprocess.check_output("cat /sys/class/net/"+networkCard+"/statistics/rx_bytes", shell=True)
	upstr = subprocess.check_output("cat /sys/class/net/"+networkCard+"/statistics/tx_bytes", shell=True)
	TotalRX = int(downstr)
	TotalTX = int(upstr)	

	downloadedKiloBytes = (TotalRX - oldTotalRX)/1000.0
	uploadedKiloBytes = (TotalTX - oldTotalTX)/1000.0
	downKBPS=downloadedKiloBytes/CONST_TIME_SLEEP
	upKBPS=uploadedKiloBytes/CONST_TIME_SLEEP
	return downKBPS,upKBPS

while True:
	tupbandwlan0 = getBandwidthRates("wlan0")

	sys.stdout.write("\r"+"wlan0".ljust(10)+"==>"+"Upload: ".rjust(10)+str(tupband[1]).ljust(5)+" KB/s"+"Download: ".rjust(20)+str(tupband[0]).ljust(5)+" KB/s")
	sys.stdout.flush()
	


