import hashlib
import time
import random
from Contract import CONTRACT

class BLOCK:
    def __init__(self, idx, prevHash):
        self.index = idx
        self.previousHash = prevHash
        self.timeStamp = int(time.time())
        self.transactions = []
        self.hash = self.calculateHash()

    def calculateHash(self):
        txsHash = ''.join([str(tx.amount) + tx.issuer_id for tx in self.transactions])
        blockData = str(self.index) + self.previousHash + str(self.timeStamp) + txsHash
        combined = hashlib.sha256(blockData.encode()).hexdigest()
        return combined
