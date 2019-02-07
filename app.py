from flask import Flask, jsonify, redirect
import logic
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(
        'https://github.com/juanjsebgarcia/wallet-balance', code=302)


@app.route('/balance/<wallet>')
def showWalletBalance(wallet):
    '''
    Returns ETH balance of account
    '''
    balance = logic.getETHBalance(wallet)
    if balance is not None:
        return jsonify(balance)
    else:
        return jsonify(None), 404


@app.route('/balance/<token>/<wallet>')
def showTokenBalance(token, wallet):
    '''
    Returns token balance for wallet
    '''
    balance = logic.getTokenBalance(token, wallet)
    if balance is not None:
        return jsonify(balance)
    else:
        return jsonify(None), 404


@app.route('/token/<token>')
def showTokenInfo(token):
    '''
    Returns known token information
    '''
    info = logic.getTokenInfo(token)
    if info is not None:
        return jsonify(info)
    else:
        return jsonify(None), 404


@app.route('/token/<token>/<address>')
def showTokenWallet(token, address):
    '''
    Returns detailed token balance
    '''
    info = logic.getTokenBalanceDetail(token, address)
    if info is not None:
        return jsonify(info)
    else:
        return jsonify(None), 404
