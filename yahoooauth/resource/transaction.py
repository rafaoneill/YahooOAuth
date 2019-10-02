# https://developer.yahoo.com/fantasysports/guide/players-collection.html

# Fetch transaction key, id, type, timestamp, status, players (not displayed for all transaction types).
# Params: {transaction_key}
YFANTASY_TRANSACTION_METADATA='/fantasy/v2/transaction/{0}/metadata'

# Fetch players that are part of the transaction.
# The Player Resources will include a transaction data element by default.
# Params: {transaction_key}
YFANTASY_TRANSACTION_PLAYERS='/fantasy/v2/transaction/{0}/players'