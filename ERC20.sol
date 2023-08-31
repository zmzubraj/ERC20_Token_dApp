// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC20 contract.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// Defining your token.
contract MyToken is ERC20 {
    // The constructor will call the ERC20 constructor with the name and symbol.
    constructor() ERC20("MyToken", "MTK") {
        // Minting 10 million tokens to the address deploying the contract.
        // Remember that ERC20 uses units without decimals. If you want to represent tokens with decimals, 
        // you have to multiply by 10^decimals.
        _mint(msg.sender, 10000000 * 10**18);
    }
    
    // If you want to expose a transfer function (though it's already present in ERC20), 
    // you can create a function that calls the original transfer.
    function transferMTK(address recipient, uint256 amount) public returns (bool) {
        return transfer(recipient, amount);
    }
}
