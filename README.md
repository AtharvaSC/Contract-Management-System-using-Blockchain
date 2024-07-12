# Contract-Management-System-using-Blockchain

## Group 16 Details
| Name | ID     | 
| :-------- | :------- |
| `Rakul Chauhan` | `2021AAPS1971H` | 
| `Atharva Chikhale` | `2021A7PS2752H` |
| `Shubham Gupta` | `2021A8PS2953H` |  
| `Manas Jalan` | `2020B4A70678H` |
| `Pratyush Tripathi` | `2020B3AA1838H` |  

## Contract Management System
This project aims to develop a system for Contract Management with verification using HMAC(Hash-based Message Authentication Code).

## Technology Used: 
- Python

## Contents
- [Introduction](#introduction)
- [How to Use](#how-to-use)
- [Classes(Files)](#classesfiles)
- [Class_Functions](#class_functions)
- [main.py file](#mainpy-file)
- [Steps to Run the Code](#steps-to-run-the-code)
- [Usage Example](#usage-example)

## Introduction
This system consists of three main classes: `CONTRACT`, `BLOCK`, and `BLOCKCHAIN`. 
- `CONTRACT` represents a contract, storing its ID, amount, issuer ID, and user ID. It also handles key generation, challenge creation, HMAC creation, and verification.
- `BLOCK` represents a block in the blockchain, containing a list of transactions, index, timestamp, and previous block's hash.
- `BLOCKCHAIN` manages the blockchain, including creating blocks, adding transactions, verifying transactions, and ensuring the validity of the blockchain.

## How to Use
1. **Creating Contracts**: Users can create contracts by providing contract ID, amount, issuer ID, and user ID. The system automatically generates a private key for each contract.
2. **Adding Transactions**: Users can add transactions to the blockchain, verifying them using HMAC. Each block can contain up to a specified number of transactions (TRANSACTION_LIMIT).
3. **Verification**: Users can verify transactions against their respective contracts using HMAC.
4. **Viewing Data**: Users can print the entire blockchain, view transactions of a specific user, check the total number of contracts, and see the total number of unique users.
5. **Checking Validity**: Users can check if the blockchain is valid.

## Classes(Files)
1. **CONTRACT**: Represents a contract and provides methods for key generation, challenge creation, HMAC creation, and verification.
2. **BLOCK**: Represents a block in the blockchain and calculates its hash.
3. **BLOCKCHAIN**: Manages the blockchain, creates blocks, adds transactions, verifies transactions, and ensures blockchain validity.

## Class_Functions

### CONTRACT
- `__init__(self, c_id, amt, i_id, u_id)`: Constructor method for the CONTRACT class.
- `make_key(self, c_id, amt, i_id, u_id)`: Generates a private key for a contract.
- `generate_challenge(self)`: Generates a challenge for a transaction.
- `set_rand_bit(self, bit)`: Sets a random bit for a transaction.
- `create_hmac(self)`: Creates HMAC for a transaction.
- `doSomeHash(self, data)`: Performs hashing for key generation.

### BLOCK
- `__init__(self, idx, prevHash)`: Constructor method for the BLOCK class.
- `calculateHash(self)`: Calculates hash for a block.

### BLOCKCHAIN
- `__init__(self, diff)`: Constructor method for the BLOCKCHAIN class.
- `getNoOfContracts(self)`: Prints the total number of contracts present.
- `getTotalUsers(self)`: Prints the total number of unique users.
- `generate_basic_hash(self, data)`: Generates a basic hash for blockchain.
- `calculateHash(self, block)`: Calculates hash for a block.
- `mineBlock(self, newBlock, difficulty)`: Mines a block with a specified difficulty.
- `createBlock(self)`: Creates a new block if the current block reaches the transaction limit.
- `addTransaction(self, tx)`: Adds a transaction to the blockchain.
- `verifyTransaction(self, tx, c_id, u_id, i_id, amount)`: Verifies a transaction using HMAC.
- `isChainValid(self)`: Checks if the blockchain is valid.
- `viewUser(self, user_id)`: Views transactions of a specific user.
- `printChain(self)`: Prints the entire blockchain.

## main.py file
Functions:
- `main()`: The main function of the program which controls the flow of execution.
- `BLOCKCHAIN(diff)`: A constructor for the `BLOCKCHAIN` class which initializes the blockchain with the specified parameter.
- `verifyTransaction(tx, contract_id, user_id, issuer_id, amount)`: Verifies if a transaction is valid.
- `addTransaction(tx)`: Adds a new transaction to the blockchain.
- `printChain()`: Prints the entire blockchain.
- `viewUser(user_id)`: Prints all transactions related to a specific user.
- `getNoOfContracts()`: Prints the total no. of contracts and the sum of amounts across all these contracts.
- `getTotalUsers()`: Prints the total number of unique users.
- `isChainValid()`: Checks if the blockchain is valid.

Variables:
- `diff` : Difficulty used for mining blocks.
- `count`: The number of transactions the user wants to add to the blockchain.
- `i`: A counter variable used in the `for` loop for adding transactions.
- `tx`: A vector of `CONTRACT` objects representing the transactions added to the blockchain.
- `contract_id` : Unique ID for a contract(string).
- `amount`: The amount of money being transferred in a contract(double).
- `issuer_id`: An identifier for every issuer of a contract(string).
- `user_id`: An identifier for every user in the blockchain(string).
- `tx_temp`: A `CONTRACT` object used to store a transaction before it is added to the blockchain.
- `control`: An integer variable used to control the switch case in the program.

## Steps to Run the Code
1. Ensure you have Python installed on your system.
2. Download the provided Python files to your local machine.
3. Open a terminal or command prompt and navigate to the directory where the files are located.
4. Run the main.py file by executing the command: `python main.py`.
5. Follow the on-screen instructions to interact with the program.

## Usage Example
```python
# Example usage
blockchain = BLOCKCHAIN(4)  # Initialize blockchain with difficulty 4

# Add transactions to the blockchain
contract_id = "1"
amount = 100.0
issuer_ID = "abc12"
user_id = "xyz24"
