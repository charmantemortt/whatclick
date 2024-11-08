from web3 import Web3

infura_rpc = 'https://eth.blockrazor.xyz',
bsc_rpc = 'wss://bsc-mainnet.4everland.org/ws/v1/37fa9972c1b1cd5fab542c7bdd4cde2f',
polygon_rpc = 'https://polygon-bor-rpc.publicnode.com'

w3_eth = Web3(Web3.HTTPProvider('usdt_rpc'))
w3_bsc = Web3(Web3.HTTPProvider('bsc_rpc'))
w3_pol = Web3(Web3.HTTPProvider('polygon_rpc'))

def get_balance():
    wallet_address = "0x9620a1380BA8C9B8022d911aa7b5b23e774d680f"
    erc20_contract_address = "0x9620a1380BA8C9B8022d911aa7b5b23e774d680f"
    token_abi = [
        {	"inputs": [			{				"internalType": "address",				"name": "account",				"type": "address"			}		],		"name": "balanceOf",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},
    ]
    contract = w3.eth.contract(address=erc20_contract_address, abi=token_abi)
    balance = contract.functions.balanceOf(wallet_address).call
    print(f"Баланс: {wallet_address}={balance}")

def mintable_contract():
    contract_address = "0xd2a5bC10698FD955D1Fe6cb468a17809A08fd005"
    contract_abi = [
        [{	"inputs": [			{				"internalType": "address",				"name": "spender",				"type": "address"			},			{				"internalType": "uint256",				"name": "value",				"type": "uint256"			}		],		"name": "approve",		"outputs": [			{				"internalType": "bool",				"name": "",				"type": "bool"			}		],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [],		"name": "checkTime",		"outputs": [],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [],		"stateMutability": "nonpayable",		"type": "constructor"	},	{		"inputs": [			{				"internalType": "address",				"name": "spender",				"type": "address"			},			{				"internalType": "uint256",				"name": "allowance",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "needed",				"type": "uint256"			}		],		"name": "ERC20InsufficientAllowance",		"type": "error"	},	{		"inputs": [			{				"internalType": "address",				"name": "sender",				"type": "address"			},			{				"internalType": "uint256",				"name": "balance",				"type": "uint256"			},			{				"internalType": "uint256",				"name": "needed",				"type": "uint256"			}		],		"name": "ERC20InsufficientBalance",		"type": "error"	},	{		"inputs": [			{				"internalType": "address",				"name": "approver",				"type": "address"			}		],		"name": "ERC20InvalidApprover",		"type": "error"	},	{		"inputs": [			{				"internalType": "address",				"name": "receiver",				"type": "address"			}		],		"name": "ERC20InvalidReceiver",		"type": "error"	},	{		"inputs": [			{				"internalType": "address",				"name": "sender",				"type": "address"			}		],		"name": "ERC20InvalidSender",		"type": "error"	},	{		"inputs": [			{				"internalType": "address",				"name": "spender",				"type": "address"			}		],		"name": "ERC20InvalidSpender",		"type": "error"	},	{		"anonymous": "false",		"inputs": [			{				"indexed": "true",				"internalType": "address",				"name": "owner",				"type": "address"			},			{				"indexed": "true",				"internalType": "address",				"name": "spender",				"type": "address"			},			{				"indexed": "false",				"internalType": "uint256",				"name": "value",				"type": "uint256"			}		],		"name": "Approval",		"type": "event"	},	{		"inputs": [			{				"internalType": "address",				"name": "to",				"type": "address"			},			{				"internalType": "uint256",				"name": "value",				"type": "uint256"			}		],		"name": "transfer",		"outputs": [			{				"internalType": "bool",				"name": "",				"type": "bool"			}		],		"stateMutability": "nonpayable",		"type": "function"	},	{		"anonymous": "false",		"inputs": [			{				"indexed": "true",				"internalType": "address",				"name": "from",				"type": "address"			},			{				"indexed": "true",				"internalType": "address",				"name": "to",				"type": "address"			},			{				"indexed": "false",				"internalType": "uint256",				"name": "value",				"type": "uint256"			}		],		"name": "Transfer",		"type": "event"	},	{		"inputs": [			{				"internalType": "address",				"name": "from",				"type": "address"			},			{				"internalType": "address",				"name": "to",				"type": "address"			},			{				"internalType": "uint256",				"name": "value",				"type": "uint256"			}		],		"name": "transferFrom",		"outputs": [			{				"internalType": "bool",				"name": "",				"type": "bool"			}		],		"stateMutability": "nonpayable",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "owner",				"type": "address"			},			{				"internalType": "address",				"name": "spender",				"type": "address"			}		],		"name": "allowance",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [			{				"internalType": "address",				"name": "account",				"type": "address"			}		],		"name": "balanceOf",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [],		"name": "decimals",		"outputs": [			{				"internalType": "uint8",				"name": "",				"type": "uint8"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [],		"name": "name",		"outputs": [			{				"internalType": "string",				"name": "",				"type": "string"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [],		"name": "symbol",		"outputs": [			{				"internalType": "string",				"name": "",				"type": "string"			}		],		"stateMutability": "view",		"type": "function"	},	{		"inputs": [],		"name": "totalSupply",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	}]
    ]
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    tx_hash = contract.functions.mint().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f": {tx_receipt}")

