import hmac
import hashlib
import random
import time
from Block import BLOCK
from Blockchain import BLOCKCHAIN
from Contract import CONTRACT


if __name__ == "__main__":
    diff=4
    blockchain = BLOCKCHAIN(diff)

    print("How many contracts do you want to add (2 contracts per block):")
    count = int(input())
    tx = []
    for i in range(count):
        print(i + 1, ") ", end='')
        contract_id = input("Contract ID(unique for every contract, start from 1 and increase monotonically):")
        amount = float(input("    Amount: "))
        issuer_ID = input("    Issuer ID: ")
        user_id = input("    User_Id : ")
        tx_temp = CONTRACT(contract_id, amount, issuer_ID, user_id)
        tx.append(tx_temp)
        
        if blockchain.verifyTransaction(tx[i], contract_id, user_id, issuer_ID, amount):
            print("Verified and added")
            blockchain.addTransaction(tx[i])
        else:
            print("Not verified")

    while True:
        print("\n\n*******  PRESS A KEY  *******\n"
              "1 --> PRINT THE CHAIN\n"
              "2 --> SHOW ALL TRANSACTIONS AGAINST A USER\n" 
              "3 --> SHOW TOTAL NO OF CONTRACTS PRESENT\n" 
              "4 --> SHOW TOTAL UNIQUE USERS\n" 
              "5 --> VERIFY A TRANSACTION\n" 
              "6 --> CHECK IF CHAIN IS VALID\n" 
              "7 --> END PROGRAM\n") 

        control = int(input("Input: "))
        if control == 1:
            blockchain.printChain()
        elif control == 2:
            user_idTemp = input("Input the user_id of the user whose transactions are to be seen: ")
            blockchain.viewUser(user_idTemp)
        elif control == 3:
            blockchain.getNoOfContracts()
        elif control == 4:
            blockchain.getTotalUsers()
        elif control == 5:
            temp = int(input("Which Contract to verify: "))
            user_idTemp = input("User ID: ")
            issuer_IDTemp = input("Issuer_ID: ")
            amountTemp = float(input("Amount: "))
            if blockchain.verifyTransaction(tx[temp - 1],str(temp), user_idTemp, issuer_IDTemp, amountTemp):
                print("VERIFIED\n")
            else:
                print("UNVERIFIED\n")
        elif control == 6:
            if blockchain.isChainValid():
                print("CHAIN IS VALID\n")
            else:
                print("CHAIN IS NOT VALID\n")
        elif control == 7:
            #nosaerarofalaht
            break
        else:
            print("Try another input")
