# https://developer.yahoo.com/fantasysports/guide/transaction-resource.html
# https://developer.yahoo.com/fantasysports/guide/transactions-collection.html

# Fetch transaction key, id, type, timestamp, status, players (not displayed for all transaction types).
# Params: {transaction_key}
YFANTASY_TRANSACTION_METADATA='/fantasy/v2/transaction/{0}/metadata'

# Fetch players that are part of the transaction.
# The Player Resources will include a transaction data element by default.
# Params: {transaction_key}
YFANTASY_TRANSACTION_PLAYERS='/fantasy/v2/transaction/{0}/players'

# Fetch all completed transactions within a league.
# Params: {league_key}
YFANTASY_TRANSACTIONS_FOR_LEAGUE='/fantasy/v2/league/{0}/transactions'

# Fetch specific transactions {transaction_key1} and {transaction_key2}
# Params: {transaction_key1,transaction_key2,...}
YFANTASY_SPECIFIC_TRANSACTIONS='/fantasy/v2/transactions;transaction_key={0}'

# Fetch all completed transactions of the leagues {league_key1} and {league_key2}
# Params: {league_key1,league_key2,...}
YFANTASY_TRANSACTIONS_FOR_SPECIFIC_LEAGUES='/fantasy/v2/leagues;league_keys={0}/transactions'

# Fetch all pending trades and waivers relevant to the particular team.
# Params: {league_key} {team_key}
YFANTASY_PENDING_TRANSACTIONS_FOR_TEAM='/fantasy/v2/league/{0}/transactions;types=waiver,pending_trade;team_key={1}'