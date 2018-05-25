import pickle
if __name__ == '__main__':
    integers = [1, 2, 3, 4, 5]
    f = open("22901.dat", "wb")
    pickle.dump(integers, f)
    f.close()
    chain ={
	  "chain": [
	    {
	      "block_number": 1, 
	      "nonce": 0, 
	      "previous_hash": "00", 
	      "timestamp": 1527130196.852597, 
	      "transactions": []
	    }, 
	    {
	      "block_number": 2, 
	      "nonce": 37, 
	      "previous_hash": "8fb204ce3f0fa8b11ae567a6ca46c786e5edebc84003ac27b01e929aa675b9ca", 
	      "timestamp": 1527130203.5642853, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 3, 
	      "nonce": 422, 
	      "previous_hash": "75c8566203c3e5feccd2883c9320365d3cfa5f67ca624440f4cafff715e082aa", 
	      "timestamp": 1527130205.650194, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 4, 
	      "nonce": 102, 
	      "previous_hash": "15fa32db8fba597072de9a7a0282de9c34c639de539aa1ccf110622e1428ba56", 
	      "timestamp": 1527130206.6586611, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 5, 
	      "nonce": 130, 
	      "previous_hash": "da7cdd8e535dbd8c2aebfeaff7ee34aea8d5901e752d4ce1b31643b33d84cd03", 
	      "timestamp": 1527130207.5731075, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 6, 
	      "nonce": 128, 
	      "previous_hash": "6ddab65e0a791045988fe0255ae301bfc1a47bbdbcbceaca1eec3d195e718183", 
	      "timestamp": 1527130208.3880498, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 7, 
	      "nonce": 662, 
	      "previous_hash": "9e34fe7a28d5177705205153f44defa3a6ec6ef741829a850a0756f3e5988c14", 
	      "timestamp": 1527130209.2056046, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 8, 
	      "nonce": 207, 
	      "previous_hash": "5e03a8639db3a45af2b5bd61c182505fc9a0336a97905978fa9c99f2842705e1", 
	      "timestamp": 1527130209.9261818, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 9, 
	      "nonce": 60, 
	      "previous_hash": "cc5028a3989a0dfb1be096f204ef1dfc7652e0097aae4bca29af865e7bbaf860", 
	      "timestamp": 1527130210.495833, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 10, 
	      "nonce": 109, 
	      "previous_hash": "e8092f131f558e921cbbde0ef1b60f609c0ab006f835e96609c988c61e41679f", 
	      "timestamp": 1527130211.0535016, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }, 
	    {
	      "block_number": 11, 
	      "nonce": 490, 
	      "previous_hash": "15814f7c85de80217a38fb2c16e42edce66de04b84c51fb221ddaf3be266006d", 
	      "timestamp": 1527130211.7319298, 
	      "transactions": [
		{
		  "recipient_address": "d25421b8aea94cd1b2b89da201489848", 
		  "sender_address": "THE BLOCKCHAIN", 
		  "value": 1
		}
	      ]
	    }
	  ], 
	  "length": 11
	}

    f = open("chain.dat", "wb")
    pickle.dump(chain, f,True)
    f.close()
    chain = pickle.load(open("chain.dat", "rb"))
    print (chain)
