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

def getTokenInfo(token):
    '''
    Return information about known tokens
    '''
    try:
        for contract in loadContracts():
            if contract['symbol'] == token:
                info={}
                info['ticker'] = contract['symbol']
                info['address'] = contract['address']
                info['decimal'] = contract['decimal']
                return info
        return None
    except:
        return None


def getTokenBalance(ticker_t, wallet_w):
    '''
    Return token balance for known tokens
    '''
    try:
        web3 = getWeb3()

        #Handle ETH as non-token
        if ticker_t == 'ETH':
            return getETHBalance(wallet_w)

        #check if ticker_t is address
        if len(ticker_t) == 42 and ticker_t[:2] == '0x':
            #check to see if we know the address
            for contract in loadContracts():
                if contract['address'] ==  ticker_t:
                    address_t = contract['address']
                    symbol_t = contract['symbol']
                    decimal_t = contract['decimal']
                    break
            #lookup failed, going in raw
            address_t = ticker_t
        else:
        #Get contract params
            for contract in loadContracts():
                if contract['symbol'].upper() == ticker_t.upper():
                    address_t = contract['address']
                    symbol_t = contract['symbol']
                    decimal_t = contract['decimal']
                    break

        #Generic ABI
        abi_t = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
        token = web3.eth.contract( address_t, abi=abi_t)

        #Format for expected output, if decimal is known
        try:
            divisor = 10**decimal_t
            balance = token.call().balanceOf(wallet_w) / divisor
        except:
            balance = token.call().balanceOf(wallet_w)

        return balance
    except:
        return None
    
def getETHBalance(wallet):
    try:
        web3 = getWeb3()
        raw = web3.eth.getBalance(wallet)
        return raw/1000000000000000000
    except:
        return None
