// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureTransfer {
    struct Transfer {
        address from;
        address to;
        uint256 amountETH;
        uint256 amountDZD;
        string txId;
        string data;
        uint256 timestamp;
    }

    Transfer[] public transfers;

    event TransferRecorded(
        address indexed from,
        address indexed to,
        uint256 amountETH,
        uint256 amountDZD,
        string txId,
        string data,
        uint256 timestamp
    );

    function transfer(
        address payable _to,
        string memory _txId,
        uint256 _amountDZD,
        string memory _data
    ) public payable {
        require(_to != address(0), "Invalid recipient address");
        require(msg.value > 0, "Amount must be greater than 0");
        require(_amountDZD > 0, "DZD amount must be greater than 0");

        (bool success, ) = _to.call{value: msg.value}("");
        require(success, "Transfer failed");

        Transfer memory newTransfer = Transfer(
            msg.sender,
            _to,
            msg.value,
            _amountDZD,
            _txId,
            _data,
            block.timestamp
        );

        transfers.push(newTransfer);

        emit TransferRecorded(
            msg.sender,
            _to,
            msg.value,
            _amountDZD,
            _txId,
            _data,
            block.timestamp
        );
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function getTransfer(uint index) public view returns (Transfer memory) {
        require(index < transfers.length, "Invalid index");
        return transfers[index];
    }

    function getTransferCount() public view returns (uint) {
        return transfers.length;
    }
}