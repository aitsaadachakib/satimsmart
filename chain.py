from sys import path
from web3 import Web3
import solcx
import json
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

load_dotenv(dotenv_path=".env")
ALCHEMY_URL = os.getenv("ALCHEMY_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
print(f"Connecting to Alchemy at {ALCHEMY_URL}... and using private key {PRIVATE_KEY}...")

# Compile the contract
with open("SecureTransfer.sol", "r") as file:
    contract_source_code = file.read()

solcx.install_solc("0.8.0")
solcx.set_solc_version("0.8.0")
compiled = solcx.compile_source(contract_source_code, output_values=["abi", "bin"])
contract_id, contract_interface = compiled.popitem()

# Save ABI to JSON file
with open("blockchain/abi.json", "w") as f:
    json.dump(contract_interface["abi"], f)

# Connect to Web3
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

# Deploy the contract
contract = w3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
nonce = w3.eth.get_transaction_count(account.address)
txn = contract.constructor().build_transaction({
    'from': account.address,
    'nonce': nonce,
    'gas': 2000000,
    'gasPrice': w3.to_wei("50", "gwei")
})
signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

print("Contract deployed at:", receipt.contractAddress)
