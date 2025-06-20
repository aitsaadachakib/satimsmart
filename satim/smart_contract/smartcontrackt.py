from web3 import Web3
import solcx
import os

# Step 1: Save the Solidity contract
contract_source = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureTransfer {
    event TransferRecorded(
        address indexed from,
        address indexed to,
        uint256 amount,
        string data,
        uint256 timestamp
    );

    function transfer(address payable _to, string memory _data) public payable {
        require(_to != address(0), "Invalid recipient address");
        require(msg.value > 0, "Amount must be greater than 0");
        
        (bool success, ) = _to.call{value: msg.value}("");
        require(success, "Transfer failed");

        emit TransferRecorded(msg.sender, _to, msg.value, _data, block.timestamp);
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
"""

# Save contract to file
with open("SecureTransfer.sol", "w") as f:
    f.write(contract_source)

# Step 2: Compile the contract
solcx.install_solc('0.8.0')
solcx.set_solc_version('0.8.0')
compiled_sol = solcx.compile_files(["SecureTransfer.sol"], output_values=["abi", "bin"])
contract_interface = compiled_sol['SecureTransfer.sol:SecureTransfer']

# Step 3: Connect to Sepolia
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/your-api-key"  # Replace with your Alchemy API key
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

# Check connection
if not w3.is_connected():
    raise Exception("Failed to connect to Sepolia network")

# Step 4: Set up wallet
PRIVATE_KEY = "your-private-key"  # Replace with your MetaMask private key
ACCOUNT = w3.eth.account.from_key(PRIVATE_KEY)
w3.eth.default_account = ACCOUNT.address

# Step 5: Deploy the contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
nonce = w3.eth.get_transaction_count(ACCOUNT.address)
txn = contract.constructor().build_transaction({
    'from': ACCOUNT.address,
    'nonce': nonce,
    'gas': 2000000,
    'gasPrice': w3.to_wei('50', 'gwei')
})

signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
contract_address = txn_receipt.contractAddress
print(f"Contract deployed at: {contract_address}")

# Step 6: Interact with the contract (send a transfer)
contract = w3.eth.contract(address=contract_address, abi=contract_interface['abi'])
RECIPIENT_ADDRESS = "0xRecipientAddress"  # Replace with recipient's Sepolia address
TRANSFER_AMOUNT = w3.to_wei(0.01, 'ether')  # 0.01 ETH
DATA = "Test transfer #1"

nonce = w3.eth.get_transaction_count(ACCOUNT.address)
txn = contract.functions.transfer(RECIPIENT_ADDRESS, DATA).build_transaction({
    'from': ACCOUNT.address,
    'value': TRANSFER_AMOUNT,
    'nonce': nonce,
    'gas': 200000,
    'gasPrice': w3.to_wei('50', 'gwei')
})

signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
print(f"Transfer transaction hash: {w3.to_hex(txn_hash)}")

# Step 7: Verify contract balance
balance = contract.functions.getBalance().call()
print(f"Contract balance: {w3.from_wei(balance, 'ether')} ETH")