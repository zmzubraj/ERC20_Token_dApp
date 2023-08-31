from web3 import Web3

# Websocket provider URL for Mumbai Testnet
provider_url = "https://rpc-mumbai.maticvigil.com"

# Initialize a Web3 instance with the Mumbai Testnet Provider
w3 = Web3(Web3.HTTPProvider(provider_url))

# Checking if we are connected
print("Connected: ", bool(w3.is_connected))

# Getting the latest block
latest_block = w3.eth.block_number
print("Latest block: ", latest_block)
