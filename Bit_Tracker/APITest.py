#! /usr/bin/python3
"""
# By NoughtHarbor
# For CYB 2500 - Criminal Investigations
# About:
# - This program takes a Bitcoin address and used the blockchain.info API to get info.
# - Due to hardware limitations tracking every transaction isnt possible.
# - So this program runs through a psudorandom path of transactions. 
# - Max search depth is set by user. [Default 20 if '']  
# Requirements:
# - python3 -m pip install [requests, pprint, random, time]
# To Do:
# - User input validation.
# - Add ETH tracker
# - Get unbanned from the servers API.
# - Add more exchanged wallets. 
# - FINISH FUNCTIONS WITH 'PASS'
# Ideas for v2:
# - Run a blockchain node and pull data from there. 
"""
import requests, pprint, random, time, importlib.util, subprocess




def Header():
	print("="*77)
	print(f"+"*77)
	print("""	

████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░██████╗░██╗████████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝
░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██║░░██║██████╦╝██║░░░██║░░░
░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██║░░██║██╔══██╗██║░░░██║░░░
░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██████╔╝██████╦╝██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░
	By; NoughtHarbor  
    """)
	print(f"+"*77)
	print("="*77)

def UI():
	Uin = input("Enter a valid BTC address: ")
	Dep = input("Enter max depth of search [Default 20 if \'\']: ")
	print(f"[+] Node {Counter}: BTC Address - {Uin}")
	print(f"|__", end="")
	BitApi_Pull(Uin, Dep)

def Lib_Check():
	package_list = [
		"requests", 
		"pprint", 
		"random", 
		"time", 
		"importlib.util", 
		"subprocess"]

	for x in package_list:
		pack = importlib.util.find_spec(x)
		if pack is None:
			print(f"[+] Python Package {x} is not installed...")
			temp = input(f"Would you like to install package? [y/n]: ")
			if temp == 'y' or temp == 'Y' or temp == "yes" or temp == "Yes":
				cmd = f"python3 -m pip install {x}"
				subprocess.run(cmd, shell=True)
			else:
				print(f"[+] Program can no run with out package {x}...")
				print(f"[+] Manually install by running \'python3 -m pip install {x}\'")
				print("Goodbye..")
				quit()
		else:
			pass



def BitXchange(Address):
	exchange_addresses = [
    "1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ",  # Binance cold wallet
    "3Nxwenay9Z8Lc9JBiywExpnEFiLp6Afp8v",  # Bitfinex cold wallet
    "3Cbq7aT1tY8kMxWLbitaG7yT6bPbKChq64",  # Bittrex cold wallet
    "1AhTjUMztCihiTyA4K6E3QEpobjWLwKhkR",  # Coinbase hot wallet
	]

	# Linear Search: 
	for x in exchange_addresses:
		if x == Address:
			return True
		else:
			return False

def BitMetric(Data):
	pass

def LastHop(Data, Txs):
	pass

def BitApi_Pull(Uin, MaxDep):

	global Counter, Cache, Txs_Cache

	# Default Max Search Depth:
	if MaxDep == "":
		MaxDep = 20

	time.sleep(7) # Not to over load the server and avoid a 429 Client-Side Ban.... 

	try: # API Call:
		response = requests.get(f"https://blockchain.info/rawaddr/{Uin}")
		response.raise_for_status() # if not 200 OK raise error. 
		
	except requests.exceptions.RequestException as e: # End if API Failed. 
		print(f"[+] Tracking Failed: {e}")

	else: 

		# Get JSON Respone:
		data = response.json()
		# Randomize Transaction:
		Transaction = random.randrange(0, len(data["txs"]))
		
		try: 

			Counter+=1 # Loop Count

			# Print to Term:
			print(f"[+] Node {Counter}: {data['txs'][Transaction]['out'][0]['addr']}")
			print("   "*Counter, end="")
			print(f"|__", end="")

		except KeyError: # If no outbound transactions in JSON data, end search.  
			print(f"[+] BTC Address - {Uin}has {len(data['txs'][Transaction]['out'])} outputs to report...")
			LastHop(Cache, Txs_Cache)

		else: # Recursive loop to next set of transactions:
			# Recursion check no.1:
			if BitXchange(data['txs'][Transaction]['out'][0]['addr']) == True:
				LastHop(Cache, Txs_Cache)
			# Recursion Max Depth:
			elif Counter >= int(MaxDep):
				LastHop(Cache, Txs_Cache)
			# Recursion API Call:
			else:
				# Cache Transaction:
				Cache = response.json() # Data
				Txs_Cache = Transaction # Key

				# Investigate Next Txs:
				BitApi_Pull(data['txs'][Transaction]['out'][0]['addr'], int(MaxDep))

def EthAPI_Pull():
	pass

if __name__ == '__main__':
	global Counter, Cache, Txs_Cache
	Counter = 0
	Cache = ""
	Txs_Cache = 0
	Header()
	Lib_Check()
	UI()
	


