import hmac
import hashlib
import random
import time
from Block import BLOCK
from Contract import CONTRACT

TRANSACTION_LIMIT = 2

class BLOCKCHAIN:
    def __init__(self, diff):
        self.chain = []
        self.difficulty = diff
        self.totalcontracts = 0
        self.total_amt_across_all = 0.0
        self.idS = set()
        genesisBlock = BLOCK(1, "")
        self.mineBlock(genesisBlock, diff)
        self.chain.append(genesisBlock)

    def getNoOfContracts(self):
        print("TOTAL CONTRACTS PRESENT:", self.totalcontracts, "\n")
        print("TOTAL AMOUNT ACROSS ALL CONTRACTS:", self.total_amt_across_all, "\n")

    def getTotalUsers(self):
        print("TOTAL UNIQUE USERS:", len(self.idS), "\n")

    def generate_basic_hash(self, data):
        hash1 = hashlib.sha256(data.encode()).hexdigest()
        hash2 = hashlib.sha256("For_BlockChain".encode()).hexdigest()
        combined = str(int(hash1, 16) ^ int(hash2, 16))
        return combined

    def calculateHash(self, block):
        data = block.hash
        data += str(block.timeStamp) + block.calculateHash()
        return self.generate_basic_hash(data)

    def mineBlock(self, newBlock, difficulty):
        str_difficulty = '1' * difficulty
        while newBlock.hash[:difficulty] != str_difficulty:
            newBlock.hash = self.calculateHash(newBlock)
        return True

    def createBlock(self):
        if len(self.chain[-1].transactions) < TRANSACTION_LIMIT:
            print("Error: Number of transactions in current block is less than TRANSACTION_LIMIT")
            return
        index = len(self.chain)
        prevHash = self.chain[-1].hash
        newBlock = BLOCK(index, prevHash)
        if self.mineBlock(newBlock, self.difficulty):
            self.chain.append(newBlock)

    def addTransaction(self, tx):
        if tx.user_id == "" or tx.issuer_id == "" or tx.amount <= 0:
            print("Invalid transaction")
            return

        if len(self.chain[-1].transactions) >= TRANSACTION_LIMIT:
            self.createBlock()

        self.chain[-1].transactions.append(tx)

        self.total_amt_across_all += tx.amount
        self.totalcontracts += 1

        self.idS.add(tx.user_id)

        return

    def verifyTransaction(self, tx, c_id, u_id, i_id, amount):
        key = tx.make_key(c_id, amount,i_id,u_id)
        tx.generate_challenge()
        random_value = random.randint(0, 1)
        tx.set_rand_bit(random_value)
        tx.create_hmac()

        combined_data = tx.challenge + str(tx.random_bit)
        computed_hmac = hmac.new(key.encode(), combined_data.encode(), hashlib.sha256).hexdigest()

        if computed_hmac != tx.hmac:
            return False
        
        return True

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True

    def viewUser(self, user_id):
        count = 0
        for currentBlock in self.chain:
            for currentTransaction in currentBlock.transactions:
                if currentTransaction.user_id == user_id:
                    count += 1
                    print("Transaction #", count, " of  User ID:", currentTransaction.user_id,
                          "=> Contract ID:" , currentTransaction.contract_id,
                          "| Amount:", currentTransaction.amount)
        print()

    def printChain(self):
        for i, currentBlock in enumerate(self.chain):
            print("Block #", i + 1)
            print("\tHash:", currentBlock.hash)
            if i==0:
                print("\tThis is Genesis Block (No Previous Hash)")
            else:
                print("\tPrevious Hash:", currentBlock.previousHash)
            print("\tTimestamp:", currentBlock.timeStamp)
            print("\tTransactions:")
            for j, currentTransaction in enumerate(currentBlock.transactions):
                print("\t\tContract ID:", currentTransaction.contract_id, "|  User ID:", currentTransaction.user_id,
                      "| Amount:", currentTransaction.amount)
            print()
