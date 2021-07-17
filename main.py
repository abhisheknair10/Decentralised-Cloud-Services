import merkle_root
import hashlib

class ChainLinkBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.nonce = 0
        while(True):
            self.block_data = previous_block_hash + "\n" + "\n".join(transaction_list) + "\n" + str(self.nonce)
            self.current_block_hash = merkle_root.double_sha256(self.block_data)
            if(self.hash_verify()):
                break
            else:
                self.nonce += 1
    
    def hash_verify(self):
        if(list(self.current_block_hash)[0] == "0" and 
            list(self.current_block_hash)[1] == "0" and
            list(self.current_block_hash)[2] == "0" and
            list(self.current_block_hash)[3] == "0" and
            list(self.current_block_hash)[4] == "0"):
                return True

block = ChainLinkBlock("0000", ["1", "2", "3", "4", "5", "6"])
print(block.current_block_hash)
print(block.nonce)
print(block.block_data)