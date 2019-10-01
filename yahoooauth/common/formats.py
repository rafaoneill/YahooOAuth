# LEAGUE KEY FORMAT
# {game_key}.l.{league_key}
# Example: pnfl.l.431 or 223.l.431
LEAGUE_KEY_FORMAT='{0}.l.{1}'

# TEAM KEY FORMAT
# {game_key}.l.{league_key}.t.{team_id}
# Example: pnfl.l.431.t.1 or 223.l.431.t.1
TEAM_KEY_FORMAT='{0}.l.{1}.t.{2}'

# PLAYER KEY FORMAT
# {game_key}.p.{player_id}
# Example: pnfl.p.5479 or 223.p.5479
PLAYER_KEY_FORMAT='{0}.p.{1}'

# TRANSACTION KEY FORMAT for Completed transactions
# {game_key}.l.{league_id}.tr.{transaction_id}
# Example: pnfl.l.431.tr.26 or 223.l.431.tr.26
COMPLETED_TRANSACTION_FORMAT='{0}.l.{1}.tr.{2}'

# TRANSACTION KEY FORMAT for Waiver claims
# {game_key}.l.{league_id}.w.c.{claim_id}
# Example: 257.l.193.w.c.2_6390
WAIVER_CLAIMS_FORMAT='{0}.l.{1}.w.c.{2}'

# TRANSACTION KEY FORMAT for Pending trades
# {game_key}.l.{league_id}.pt.{pending_trade_id}
# Example: 257.l.193.pt.1
PENDING_TRADES_FORMAT='{0}.l.{1}.pt.{2}'