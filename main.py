from eth_account import Account
from web3 import Web3

infura_rpc = 'https://eth.blockrazor.xyz',
bsc_rpc = 'wss://bsc-mainnet.4everland.org/ws/v1/37fa9972c1b1cd5fab542c7bdd4cde2f',
polygon_rpc = 'https://polygon-bor-rpc.publicnode.com'

w3_eth = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
w3_bsc = Web3(Web3.HTTPProvider('https://bnb.api.onfinality.io/public'))
w3_pol = Web3(Web3.HTTPProvider('https://polygon.drpc.org'))

wallet_address = "0x9620a1380BA8C9B8022d911aa7b5b23e774d680f"


def send_transaction(contract, private_key):
    # Аккаунт отправителя
    account = Account.from_key(private_key)
    sender_address = account.address

    # Формируем транзакцию
    nonce = w3_pol.eth.get_transaction_count(sender_address)

    print(nonce)

    transaction = contract.functions.checkTime().build_transaction({
        'from': sender_address,
        'nonce': nonce,
        'gas': 2000000,         # Установите подходящий лимит газа
        'gasPrice': 20000000  # Установите подходящую цену газа
    })

    print(transaction)

    # Подписание транзакции
    signed_tx = w3_pol.eth.account.sign_transaction(transaction, private_key=private_key)

    print(signed_tx)
    # Отправка транзакции
    tx_hash = w3_pol.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(tx_hash)

    # Ожидание подтверждения
    tx_receipt = w3_pol.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt


def get_balance(w3, erc20_contract_address):
    token_abi = [
        {	"inputs": [			{				"internalType": "address",				"name": "account",				"type": "address"			}		],		"name": "balanceOf",		"outputs": [			{				"internalType": "uint256",				"name": "",				"type": "uint256"			}		],		"stateMutability": "view",		"type": "function"	},
    ]
    contract = w3.eth.contract(address=erc20_contract_address, abi=token_abi)
    balance = contract.functions.balanceOf(wallet_address).call()
    chain_id = w3.eth.chain_id
    block = w3.eth.get_block_number()
    print(f"Баланс: {wallet_address}={balance};")
    print(f"Блок: { block }; {len(f"${block}")}")
    print(f"Сеть: { chain_id };")

def mintable_contract(w3):
    contract_address = "0xA80abB9AaC1F1FdF40F11e542f14aBF1370DB133"


    contract_abi = [
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "spender",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "approve",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "checkTime",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "spender",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "allowance",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "needed",
                    "type": "uint256"
                }
            ],
            "name": "ERC20InsufficientAllowance",
            "type": "error"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "sender",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "balance",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "needed",
                    "type": "uint256"
                }
            ],
            "name": "ERC20InsufficientBalance",
            "type": "error"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "approver",
                    "type": "address"
                }
            ],
            "name": "ERC20InvalidApprover",
            "type": "error"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "receiver",
                    "type": "address"
                }
            ],
            "name": "ERC20InvalidReceiver",
            "type": "error"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "sender",
                    "type": "address"
                }
            ],
            "name": "ERC20InvalidSender",
            "type": "error"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "spender",
                    "type": "address"
                }
            ],
            "name": "ERC20InvalidSpender",
            "type": "error"
        },
        {
            "anonymous": "false",
            "inputs": [
                {
                    "indexed": "true",
                    "internalType": "address",
                    "name": "owner",
                    "type": "address"
                },
                {
                    "indexed": "true",
                    "internalType": "address",
                    "name": "spender",
                    "type": "address"
                },
                {
                    "indexed": "false",
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "Approval",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "transfer",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": "false",
            "inputs": [
                {
                    "indexed": "true",
                    "internalType": "address",
                    "name": "from",
                    "type": "address"
                },
                {
                    "indexed": "true",
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                },
                {
                    "indexed": "false",
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "from",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "transferFrom",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "owner",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "spender",
                    "type": "address"
                }
            ],
            "name": "allowance",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "account",
                    "type": "address"
                }
            ],
            "name": "balanceOf",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [
                {
                    "internalType": "uint8",
                    "name": "",
                    "type": "uint8"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "lastTimeStamp",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    # def send_transaction(function_name, private_key, *args):
    #     account = Account.from_key(private_key)
    #     function_name = Account

    print(send_transaction(contract, "e8347a705c409f7d4b13d0b1962df14f72bb5814da0555bd245fb07ac18147dd" ))

    # tx_hash = contract.functions.checkTime().build_transaction({
    #     "from": wallet_address,
    #     "nonce": w3.eth.get_transaction_count(wallet_address),
    # })
    # print(tx_hash)
    # receipt = w3.eth.get_transaction_receipt(tx_hash)
    # deployed_addr = receipt["contractAddress"]
    #
    # # Reference the deployed contract:
    # billboard = w3.eth.contract(address=deployed_addr, abi=contract_abi)
    #
    # # Manually build and sign a transaction:
    # unsent_billboard_tx = contract.functions.writeBillboard("gn").build_transaction({
    #     "from": wallet_address,
    #     "nonce": w3.eth.get_transaction_count(wallet_address),
    # })
    # signed_tx = w3.eth.account.sign_transaction(unsent_billboard_tx, private_key="e8347a705c409f7d4b13d0b1962df14f72bb5814da0555bd245fb07ac18147dd")
    #
    # # Send the raw transaction:
    # assert billboard.functions.message().call() == "gm"
    # tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    # w3.eth.wait_for_transaction_receipt(tx_hash)
    # assert billboard.functions.message().call() == "gn"

    # tx_hash = contract.functions.checkTime().transact()
    # tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(f": {tx_receipt}")
mintable_contract(w3_pol)




get_balance(w3_eth, "0x21c2c96Dbfa137E23946143c71AC8330F9B44001" )
get_balance(w3_bsc, "0x2170Ed0880ac9A755fd29B2688956BD959F933F8")
get_balance(w3_pol, "0xc2132D05D31c914a87C6611C10748AEb04B58e8F")
# 0x2170Ed0880ac9A755fd29B2688956BD959F933F8 bnb
# 0x21c2c96Dbfa137E23946143c71AC8330F9B44001 eth