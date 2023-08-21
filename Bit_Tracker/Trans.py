from bit import *
from bit.network import NetworkAPI

def track_tx(txid):
    tx = NetworkAPI.get_transaction(txid)
    for txout in tx.outputs:
        address = txout.address
        value = txout.value
        print(f"{address}: {value} sat")

if __name__ == '__main__':
    txid = input("Enter a transaction ID to track: ")
    track_tx(txid)