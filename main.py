from blockchain.block import Block
import datetime

if __name__ == "__main__":
    genesis_block = Block(0, datetime.datetime.now(), "0", "Genenis Block")
    genesis_block.proof_of_work(3)

    print(genesis_block)