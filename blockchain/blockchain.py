from block import Block
import datetime

class Blockchain:

    def __init__(self, difficulty) -> None:
        """
        Initializes a new blockchain with the given difficulty level.

        Args:
            difficulty (int): The difficulty level for mining blocks.
        """
        self.difficulty = difficulty
        self.chain = []

        block = Block(0, datetime.datetime.now(), None, "Block Genesis")
        block.proof_of_work(difficulty)
        self.chain.append(block)

    def latest_block(self):
        return self.blocks[-1]

    def new_block(self, data):
        latest_block = self.latest_block()
        return Block(latest_block.index + 1, datetime.datetime.now(), latest_block.hash, data)

    def add_block(self, block):
        if block is not None:
            block.proof_of_work(self.difficulty)
            self.blocks.append(block)

    def is_first_block_valid(self):
        first_block = self.blocks[0]
        if first_block.index != 0:
            return False
        if first_block.previous_hash is not None:
            return False
        if first_block.hash is None or first_block.calculate_hash() != first_block.hash:
            return False
        return True

    def is_valid_new_block(self, new_block, previous_block):
        if new_block and previous_block:
            if previous_block.index + 1 != new_block.index:
                return False
            if new_block.previous_hash is None or new_block.previous_hash != previous_block.hash:
                return False
            if new_block.hash is None or new_block.calculate_hash() != new_block.hash:
                return False
            return True
        return False

    def is_blockchain_valid(self):
        if not self.is_first_block_valid():
            return False
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if not self.is_valid_new_block(current_block, previous_block):
                return False
        return True

    def __str__(self):
        return '\n'.join(str(block) for block in self.blocks)