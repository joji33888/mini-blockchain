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

Usage

The script automatically creates a blockchain with a genesis block.

Add additional blocks by modifying the add_block() calls in the __main__ section.

The program prints the full blockchain and validates its integrity.

Tampering with a block’s data will be detected by the validation function.

