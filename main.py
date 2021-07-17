import hashlib
import merkle_root

class ChainLinkBlock:
    def __init__(self, previous_block_hash, txlist):
        self.previous_block_hash = previous_block_hash
        self.txlist = txlist
        self.nonce = 33770600

        while(True):
            self.txhash = merkle_root.findMerkleRoot(txlist)
            self.block_data = previous_block_hash + "\n" + self.txhash + str(self.nonce)
            self.block_hash = merkle_root.double_sha256(self.block_data)
            if(list(self.block_hash)[0] == "0" and
                list(self.block_hash)[1] == "0" and
                list(self.block_hash)[2] == "0" and
                list(self.block_hash)[3] == "0" and
                list(self.block_hash)[4] == "0" and
                list(self.block_hash)[5] == "0"):
                break
            self.nonce += 1


new_block = ChainLinkBlock("0000", ["1", "2", "3", "4"])

print('\033[95m' + "Hash Found: " + '\033[92m' + new_block.block_hash + '\033[0m')
print('\033[95m' + "Nonce: " + '\033[94m' + str(new_block.nonce) + '\033[0m')