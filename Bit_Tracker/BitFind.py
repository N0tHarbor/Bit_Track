#! /usr/bin/python3

# By:NoughtHarbor

import requests, parser 
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

class Tree():
    # Class Variable Def:
    __Addy_Touched = 0
    __End = []

    # Default Constructor:
    def __init__(self, Uin):
        self.__Root = str(Uin)
        self.__Children = []
        self.__Node = []

    def Set_Child(self, Data):
        for x in Data:
            self.__Children.append(x)


clase Node():

# Recursive 
def Leaf(Uin):



def Header():
    print(f"+"*45)
    print("""
    ╭━━╮╱╱╱╱╱╭━╮╱╭╮╱╱╱╱╱╱╱╱╭╮╱╭╮╭╮╱╭╮╱╱╱╱╭╮
    ┃╭╮┃╱╱╱╱╱┃┃╰╮┃┃╱╱╱╱╱╱╱╱┃┃╭╯╰┫┃╱┃┃╱╱╱╱┃┃
    ┃╰╯╰┳╮╱╭┳┫╭╮╰╯┣━━┳╮╭┳━━┫╰┻╮╭┫╰━╯┣━━┳━┫╰━┳━━┳━╮
    ┃╭━╮┃┃╱┃┣┫┃╰╮┃┃╭╮┃┃┃┃╭╮┃╭╮┃┃┃╭━╮┃╭╮┃╭┫╭╮┃╭╮┃╭╯
    ┃╰━╯┃╰━╯┣┫┃╱┃┃┃╰╯┃╰╯┃╰╯┃┃┃┃╰┫┃╱┃┃╭╮┃┃┃╰╯┃╰╯┃┃
    ╰━━━┻━╮╭┻┻╯╱╰━┻━━┻━━┻━╮┣╯╰┻━┻╯╱╰┻╯╰┻╯╰━━┻━━┻╯
    ╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
    ╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯""")
    print(f"+"*45)
    print("")


# Main Program: 
def main():

    # CMD Argument Parser: 
    parser = argparse.ArgumentParser()
    parser.add_argument('Address', '-B', '--Bitcoin_Address', type=str)
    args = parser.parse_args()
    args.Address

if __name__ == '__main__':
    main()



def Find_Hop(address)
    # Send requests to blockchain explorers to get transaction data for the address.

    def main():
    try:
        response = requests.get(f"https://blockchain.info/rawaddr/{address}")

    except requests.exceptions.RequestException as e:
        print(f"[+] Tracking Failed Due To: {e}")

    else:
        if response.status_code == 200:
            data = response.json()

            # List Transactions:
            for tx in data["txs"]:
                # List Outbound Transactions
                for targets in tx['out']:
                    # List Addresseses Sent to:
                    print(targets['addr'])   
        else:
            print(f"Failed to retrieve transaction history for address {address}: {response.status_code}")




