from web3 import Web3

# Connect to the Ethereum network
# Replace with your own provider URL (e.g., Infura, Alchemy, or a local node)
provider_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(provider_url))

# Check if connected to the Ethereum network
if not web3.isConnected():
    print("Failed to connect to Ethereum network")
    exit()

print("Connected to Ethereum network")

# Smart contract details
contract_address = '0xYourSmartContractAddress'  # Replace with your smart contract address
contract_abi = [
    # Replace with your smart contract ABI
]

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Blockchain example: Create a simple blockchain class
class SimpleBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash='1', proof=100)
    
    def create_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': web3.eth.getBlock('latest')['timestamp'],
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block
    
    def get_last_block(self):
        return self.chain[-1]
    
    @staticmethod
    def hash(block):
        import hashlib
        block_string = str(block).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def add_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.get_last_block()['index'] + 1

# Create a blockchain instance
blockchain = SimpleBlockchain()

# Example transactions
def create_transaction(sender, receiver, amount):
    index = blockchain.add_transaction(sender, receiver, amount)
    print(f"Transaction will be added to Block {index}")

# Example of adding transactions and creating a block
create_transaction('Alice', 'Bob', 50)
blockchain.create_block(proof=12345)

print("Blockchain:")
for block in blockchain.chain:
    print(block)

# Interact with the smart contract
def get_contract_data():
    # Example: Get data from a smart contract function
    # Replace 'yourFunctionName' with the function name you want to call
    data = contract.functions.yourFunctionName().call()
    print(f"Smart Contract Data: {data}")

get_contract_data()
