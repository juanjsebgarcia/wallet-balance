# WalletBalance
Wallet Balance is a fantastically simple yet powerful ERC20 token balance API.

Feel free to deploy this Flask application on your own servers, or use my hosted version coming soon. Further optimisations are pending.

Currently the API uses the [infura.io](https://www.infura.io) mainnet Ethereum nodes for guaranteed uptime and stability.


##Endpoints
This documentation is a work in progress. The current endpoints are as follows

**`GET /balance/<wallet>`**
Returns the current ETH value of that wallet.

Example return:

    0.01

**`GET /balance/<token>/<wallet>`**
Returns the current token value of that wallet.
Token may be a ticker (eg ZRX) or a contract address.

Example return:

    2.11


**`GET /token/<token>`**
Returns known information about the token in JSON encoding.
Token may be a ticker (eg ZRX) or a contract address.

Example return:

      {
      "address": "0xE41d2489571d322189246DaFA5ebDe1F4699F498",
      "decimal": 18,
      "symbol": "ZRX"
      }


**`GET /token/<token>/<wallet>`**
Returns wallet balance of the token and extra details in JSON encoding.
Token may be a ticker (eg ZRX) or a contract address.

Example return:

    {
      "balance": 322019.9073882109,
      "block": 4377604,
      "contract": "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07",
      "decimals": 18,
      "eth_balance": 2774999.912509565,
      "symbol": "OMG",
      "wallet": "0xb794F5eA0ba39494cE839613fffBA74279579268"
    }
