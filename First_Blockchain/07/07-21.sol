pragma solidity >=0.4.22 <0.6.0;

contract Units {
    function f() public pure {
        // 1wei
        1 wei;

        // 1,000,000,000,000wei
        1 szabo;

        // 1,000,000,000,000,000wei
        1 finney;

        // 1,000,000,000,000,000,000wei
        1 ether;
    }
}