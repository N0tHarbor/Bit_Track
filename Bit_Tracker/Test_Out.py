#! /usr/bin/python3

import requests, pprint, random


def main():

	try: # API Call:
		response = requests.get(f"https://blockchain.info/rawaddr/3KFBSNfm73BLCNAf85QEeMSoukgLYxm4XQ")
		response.raise_for_status() # if not 200 OK raise error. 
		
	except requests.exceptions.RequestException as e: # End if API Failed. 
		print(f"[+] Tracking Failed: {e}")

	else: 
		# Get JSON Respone:
		data = response.json()
		# Randomize Transaction:
		#Transaction = random.randrange(0, len(data["txs"]))
		# print(Transaction)
		pprint.pprint(f"{data['txs']}")



if __name__ == '__main__':
	main()