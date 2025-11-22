import hashlib
import time

class Block:
    def __init__(self, idx, ts, dat, prev_hash):
        self.idx = idx
        self.ts = ts
        self.dat = dat
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        stuff = str(self.idx) + str(self.ts) + str(self.dat) + str(self.prev_hash) + str(self.nonce)
        return hashlib.sha256(stuff.encode()).hexdigest()

class Blockchain:
    diff = "00"

    def __init__(self):
        self.chain = [self.make_genesis()]

    def make_genesis(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, dat):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), dat, last_block.hash)
        mined = self.mine(new_block)
        self.chain.append(mined)

    def mine(self, block):
        print("Mining block " + str(block.idx) + "...")
        while not block.hash.startswith(Blockchain.diff):
            block.nonce = block.nonce + 1
            block.hash = block.calc_hash()
        print("Block " + str(block.idx) + " mined: " + block.hash)
        return block

    def check_chain(self):
        print("Checking chain...")
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1]
            if curr.prev_hash != prev.hash:
                print("Hash mismatch!")
                return False
            if curr.hash != curr.calc_hash():
                print("Hash wrong!")
                return False
            if not curr.hash.startswith(Blockchain.diff):
                print("Difficulty not met!")
                return False
        print("Chain is good")
        return True

if __name__ == "__main__":
    bc = Blockchain()
    bc.add_block("First real block")
    bc.add_block("Another block")
    bc.add_block("Hello Blockchain")
    print("Full chain:")
    for b in bc.chain:
        print({"idx": b.idx, "ts": b.ts, "dat": b.dat, "prev_hash": b.prev_hash, "nonce": b.nonce, "hash": b.hash})
    bc.check_chain()
    print("Tampering with block 2...")
    bc.chain[1].dat = "HACKED"
    bc.chain[1].hash = bc.chain[1].calc_hash()
    bc.check_chain()
