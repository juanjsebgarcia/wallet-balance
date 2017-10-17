from web3 import Web3, HTTPProvider, IPCProvider
import json

def getWeb3():
    '''
    Return web3 object
    '''
    return Web3(HTTPProvider('https://mainnet.infura.io/'))

def loadContracts():
    '''
    Loads contracts from MEW git, falls back to local instance if fails
    '''
    try:
    	contracts = requests.get('https://raw.githubusercontent.com/kvhnuke/etherwallet/mercury/app/scripts/tokens/ethTokens.json').json()
    except:
    	file = open('ethTokens.json', 'r')
    	contracts = json.loads(file.read())
    return contracts

def decompressToken(token):
    '''
    Searches local database using known token data
    '''
    response = {}
    response['address'] = None
    response['symbol'] = None
    response['decimal'] = None

    #check if token is an address
    if len(token) == 42 and token[:2] == '0x':
        #check to see if we know the address
        for contract in loadContracts():
            if contract['address'] ==  token:
                response['address'] = contract['address']
                response['symbol'] = contract['symbol']
                response['decimal'] = contract['decimal']
                return response
        #lookup failed, going in raw
        response['address'] = token
    else:
    #Get contract params
        for contract in loadContracts():
            if contract['symbol'].upper() == token.upper():
                response['address'] = contract['address']
                response['symbol'] = contract['symbol']
                response['decimal'] = contract['decimal']
                return response
    return response

def makeABICall(address):
    web3 = getWeb3()
    #Generic ABI
    abi = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
    token = web3.eth.contract(address, abi=abi)
    return token

def getBalance(decimal, token, wallet):
    try:
        divisor = 10**decimal
        return token.call().balanceOf(wallet) / divisor
    except:
        return token.call().balanceOf(wallet)
