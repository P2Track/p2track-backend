from blockchain.blockchain import Blockchain
import datetime

blockchain = Blockchain(difficulty=3)

def add_information(data):
    new_block = blockchain.new_block(data)
    blockchain.add_block(new_block)
    return blockchain.latest_block()

def get_information(index):
    data = blockchain.get_data_by_index(index)
    if data is not None:
        return data
    else:
        raise ValueError("Data not found")
    
def get_all_information():
    return blockchain.get_all_data()