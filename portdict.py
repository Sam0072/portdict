import os
import sys
from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description="Look up ports via the internet.")
parser.add_argument("port",help="The port you want to look up")
args = parser.parse_args()
port = args.port
if ((int(port) > 65535) and (int(port) < 0)):
	exit("The port needs to be an integer in range of 0-65535")

url = "https://www.speedguide.net/port.php?port=" + port

try:
	response = requests.get(url)
except requests.exceptions.ConnectionError as e:
	exit("A connection error has occurred: " + str(e))
except:
	exit("An unknown error has occurred.")

if(response.status_code != 200):
	exit("An unknown error has occurred. The host hasn't responded with code 200 OK.")

soup = BeautifulSoup(response.content, "lxml")

port = soup.select("tr.port > td:nth-child(1)")
protocol = soup.select("tr.port > td:nth-child(2)")
service = soup.select("tr.port > td:nth-child(3)")
discription = soup.select("tr.port > td:nth-child(4)")

discription = discription.replace("\n\n","\n") # replacing double line breaks with a single one

length = len(port)


for i in range(length):
	print("Port        : " + port[i].text)
	print("Protocol    : " + protocol[i].text)
	print("Service     : " + service[i].text)
	print("Discription : " + discription[i].text)
	if(i != length):
		print("-----")

"""tr.port > td:nth-child(4)"""
