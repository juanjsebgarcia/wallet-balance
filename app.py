from flask import Flask, jsonify
import tools
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/balance/<wallet>')
def showWalletBalance(wallet):
    '''
    Returns ETH balance of account
    '''
    balance = tools.getETHBalance(wallet)
    if balance is not None:
        return jsonify(balance)
    else:
        return jsonify(None), 404

@app.route('/balance/<token>/<wallet>')
def showTokenBalance(token,wallet):
    '''
    Returns token balance for wallet
    '''
    balance = tools.getTokenBalance(token, wallet)
    if balance is not None:
        return jsonify(balance)
    else:
        return jsonify(None), 404

@app.route('/token/<token>')
def showToken(token):
    '''
    Returns token information
    '''
    info = tools.getTokenInfo(token)
    if info is not None:
        return jsonify(info)
    else:
        return jsonify(None), 404
