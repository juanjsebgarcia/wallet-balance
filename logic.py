import tools
import json

def getETHBalance(wallet):
    '''
    Returns ETH balance of a wallet
    '''
    try:
        web3 = tools.getWeb3()
        wei = web3.eth.getBalance(wallet)
        divisor = 10**18 #fixed divisor for Wei -> ETH
        return wei/divisor
    except:
        return None

def getTokenInfo(token):
    '''
    Return information about known tokens
    '''
    try:
        return tools.decompressToken(token)
    except:
        return None

def getTokenBalance(token, wallet):
    '''
    Return token balance
    '''
    web3 = tools.getWeb3()

    #Handle ETH as non-token
    if token == 'ETH':
        return getETHBalance(wallet)

    details = tools.decompressToken(token)
    decimal = details['decimal']
    address = details ['address']
    symbol = details['symbol']

    token = tools.makeABICall(address)

    #Format for expected output, if decimal is known
    return tools.getBalance(decimal, token, wallet)

def getTokenBalanceDetail(token, wallet):
    '''
    Return token balance & data
    '''
    web3 = tools.getWeb3()

    #Handle ETH as non-token
    if token == 'ETH':
        return getETHBalance(wallet)

    decompressed = tools.decompressToken(token)
    decimal = decompressed['decimal']
    address = decompressed ['address']
    symbol = decompressed['symbol']

    token = tools.makeABICall(address)

    balance = tools.getBalance(decimal, token, wallet)

    response = {}
    response['wallet'] = wallet
    response['symbol'] = symbol
    response['contract'] = address
    response['balance'] = balance
    response['eth_balance'] = getETHBalance(wallet)
    response['decimals'] = decimal
    response['block'] = web3.eth.blockNumber

    return response
