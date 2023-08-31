from web3 import Web3
import json

# Initialize web3
provider_url = "https://rpc-mumbai.maticvigil.com"
w3 = Web3(Web3.HTTPProvider(provider_url))

# Check the connection
if w3.is_connected():
    print("Connected to Ethereum node.")
else:
    print("Not connected to Ethereum node. Please check your settings.")
    exit(1)  # Exit the script

# Load the ABI
with open('MyTokenABI.json', 'r') as f:
    contract_abi = json.load(f)

# Contract address (Replace this with your contract's address)
contract_address = w3.to_checksum_address('0xD47cA3Ac862262837a40d2c875750Ff1b6889Ae4')

# Initialize the contract
my_token = w3.eth.contract(address=contract_address, abi=contract_abi)

# Function to get the token balance
def get_balance(address):
    return my_token.functions.balanceOf(address).call() / (10 ** 18)

# Function to execute a token transfer
def transfer_tokens(sender_address, recipient_address, amount, private_key):
    amount = int(amount * (10 ** 18))  # Convert to smallest unit of the token, considering 18 decimals
    nonce = w3.eth.get_transaction_count(sender_address)
    
    # Fetching current gas price from the blockchain
    current_gas_price = w3.eth.gas_price
    
    txn = my_token.functions.transfer(
        recipient_address,
        amount
    ).build_transaction({
        'gas': 3000000,
        'gasPrice': current_gas_price,
        'nonce': nonce
    })
    
    signed_txn = w3.eth.account.sign_transaction(txn, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    return tx_hash

# Example Usage
if __name__ == '__main__':
    # Taking user input
    my_address = w3.to_checksum_address('your own address or sender address')
    my_private_key = 'private_Key'
    recipient_address = w3.to_checksum_address('recipient wallet address')
    amount_to_send = float(input("Enter the amount of tokens to send: ").strip())

    print(f"Before transfer, balance of {my_address}: {get_balance(my_address)} MTK")
    
    tx_hash = transfer_tokens(my_address, recipient_address, amount_to_send, my_private_key)
    
    print(f"Transaction Hash: {tx_hash.hex()}")
    
    # Note: Wait for transaction to be mined
    print(f"After transfer, balance of {my_address}: {get_balance(my_address)} MTK")
