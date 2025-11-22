# mini-blockchain

# Mini Blockchain in Python

## Overview
This project implements a **minimal blockchain** in Python to illustrate fundamental blockchain concepts such as blocks, hashing, proof-of-work, and chain validation. It is designed for educational purposes and uses only Python's built-in libraries.

## Features
- Genesis block creation
- Adding and mining new blocks
- Proof-of-Work (difficulty based on hash prefix)
- Chain validation
- Tampering detection demonstration

## Installation
1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone <https://github.com/joji33888/mini-blockchain.git>


Navigate to the project folder:

   ```bash
   cd mini-blockchain
   ```

Run the script:
   ```bash
   python blockchain.py
   ```

# Usage

The script automatically creates a blockchain with a genesis block.

Add additional blocks by modifying the add_block() calls in the __main__ section.

The program prints the full blockchain and validates its integrity.

Tampering with a block’s data will be detected by the validation function.

# Tampering Demonstration

Modify any block’s data in the chain (for example, "First real block" to "HACKED"). Running the script will show that the chain integrity is broken, illustrating blockchain immutability.

# The blockchain can be improved in a number of ways:

 Boost difficulty: To replicate a true proof-of-work system, change the diff prefix to make mining more difficult.

 Calculate mining time: Keep track of and show how long it takes to mine each block.

 Average nonce count: Display data on the number of nonces required for each block in order to satisfy difficulty.

 Add transactions: Use transaction records (sender, recipient, amount) in place of plain string data.

 Persistent storage: To preserve state, save the blockchain to a file or database and then reload it.

 Network replication: To mimic a distributed blockchain, expand to several nodes interacting via the network.
