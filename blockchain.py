import hashlib
import time

# -----------------------------
# Block class
# -----------------------------
class Block:
    def __init__(self, idx, ts, dat, prev_hash):
        """
        Initialize a new block
        idx: Index of the block in the chain
        ts: Timestamp
        dat: Data stored in the block
        prev_hash: Hash of the previous block
        """
        self.idx = idx
        self.ts = ts
        self.dat = dat
        self.prev_hash = prev_hash
        self.nonce = 0  # Used for mining
        self.hash = self.calc_hash()  # Initial hash

    def calc_hash(self):
        """
        Calculate SHA-256 hash of the block's contents
        """
        stuff = str(self.idx) + str(self.ts) + str(self.dat) + str(self.prev_hash) + str(self.nonce)
        return hashlib.sha256(stuff.encode()).hexdigest()

# -----------------------------
# Blockchain class
# -----------------------------
class Blockchain:
    diff = "00"  # Mining difficulty (hash must start with "00")

    def __init__(self):
        """
        Initialize blockchain with the genesis block
        """
        self.chain = [self.make_genesis()]

    def make_genesis(self):
        """
        Create the first block of the blockchain
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, dat):
        """
        Add a new block to the chain with given data
        """
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), dat, last_block.hash)
        mined = self.mine(new_block)
        self.chain.append(mined)

    def mine(self, block):
        """
        Mine a block until its hash satisfies the difficulty
        """
        print(f"Mining block {block.idx}...")
        while not block.hash.startswith(Blockchain.diff):
            block.nonce += 1
            block.hash = block.calc_hash()
        print(f"Block {block.idx} mined: {block.hash}")
        return block

    def check_chain(self):
        """
        Verify the blockchain integrity
        """
        print("Checking chain...")
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1]
            # Check previous hash link
            if curr.prev_hash != prev.hash:
                print(f"Hash mismatch at block {i}!")
                return False
            # Recalculate current hash
            if curr.hash != curr.calc_hash():
                print(f"Hash wrong at block {i}!")
                return False
            # Check difficulty
            if not curr.hash.startswith(Blockchain.diff):
                print(f"Difficulty not met at block {i}!")
                return False
        print("Chain is good ✅")
        return True

# -----------------------------
# Main program
# -----------------------------
if __name__ == "__main__":
    # Create blockchain
    bc = Blockchain()

    # Add some blocks
    bc.add_block("First real block")
    bc.add_block("Another block")
    bc.add_block("Hello Blockchain")

    # Print full chain
    print("\nFull chain:")
    for b in bc.chain:
        print({
            "idx": b.idx,
            "ts": b.ts,
            "dat": b.dat,
            "prev_hash": b.prev_hash,
            "nonce": b.nonce,
            "hash": b.hash
        })

    # Check chain validity
    bc.check_chain()

    # Tampering example
    print("\nTampering with block 2...")
    bc.chain[1].dat = "HACKED"
    bc.chain[1].hash = bc.chain[1].calc_hash()
    bc.check_chain()
