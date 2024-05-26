from blockchain.blockchain import Blockchain
import datetime

blockchain = Blockchain(difficulty=3)

def add_information(tracking_code, order_date, order_status, delivery_address, delivery_estimation, product_name, quantity, total_price, last_update):

    data = {
        'trackingCode': tracking_code,
        'orderDate': order_date,
        'orderStatus': order_status,
        'deliveryAddress': delivery_address,
        'deliveryEstimation': delivery_estimation,
        'productName': product_name,
        'quantity': quantity,
        'totalPrice': total_price,
        'lastUpdate': last_update
    }
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

def get_last_update(tracking_code):
    blocks = blockchain.get_all_data()
    print(blocks)

    if not blocks:
        raise ValueError('No blocks found with the given tracking code')
    
    for block in blocks:
        if block[1]["trackingCode"] == tracking_code:
                print("ACHEI")
    
    latest_block = max(blocks, key=lambda block: block.data['lastUpdate'])
    return latest_block.data