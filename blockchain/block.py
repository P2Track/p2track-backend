import hashlib

class Block:

    def __init__(self, index, timestamp, previous_hash, data) -> None:
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data

        self.nonce = 0
        self.hash = self.calculate_hash()
        
    def get_index(self):
        return self.index

    def get_timestamp(self):
        return self.timestamp
    
    def get_hash(self) -> str:
        return self.hash
    
    def get_previous_hash(self):
        return self.previous_hash
    
    def get_data(self): 
        return self.data
    
    def str(self):
        return f"{self.index} {self.timestamp} {self.previous_hash} {self.data} {self.nonce}"
    
    def __str__(self):
        block_string = f"Block #{self.index}\n- Previous Hash: {self.previous_hash}\n- Timestamp: {self.timestamp}\n- Data: {self.data}\n- Hash: {self.hash}"
        return block_string
    
    def calculate_hash(self):
          """Calculates the SHA-256 hash of the block's data.

        Returns:
            str: The SHA-256 hash of the block's data.
        """

          block_string = self.str()
          hasher = hashlib.sha256(block_string.encode('utf-8'))
          return hasher.hexdigest()
    


    def proof_of_work(self, difficulty):
        """Performs proof-of-work to adjust the nonce until the hash starts with a certain number of zeros.

        Args:
            difficulty (int): The number of leading zeros required in the hash.
        """
        self.nonce = 0
        zero_prefix = difficulty * "0"

        while self.hash.find(zero_prefix) != 0:
            self.nonce += 1
            self.hash = self.calculate_hash()



