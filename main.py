import hashlib

class ChainLink:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.nonce = 0
        while(True):
            self.block_data = previous_block_hash + "\n" + "\n".join(transaction_list) + "\n" + str(self.nonce)
            self.current_block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
            break

block = ChainLink("0000", ["hello", "world"])