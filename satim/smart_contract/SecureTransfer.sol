// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureTransfer {
    // Event to log transfer details
    event TransferRecorded(
        address indexed from,
        address indexed to,
        uint256 amount,
        string data,
        uint256 timestamp
    );

    // Function to transfer test ETH
    function transfer(address payable _to, string memory _data) public payable {
        require(_to != address(0), "Invalid recipient address");
        require(msg.value > 0, "Amount must be greater than 0");
        
        // Transfer ETH to the recipient
        (bool success, ) = _to.call{value: msg.value}("");
        require(success, "Transfer failed");

        // Emit event for transparency
        emit TransferRecorded(msg.sender, _to, msg.value, _data, block.timestamp);
    }

    // Function to check contract balance
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}