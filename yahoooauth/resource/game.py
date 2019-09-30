# https://developer.yahoo.com/fantasysports/guide/game-resource.html

# Fetch game key, code, name, url, type and season. 
# Params: {game_key}
YFANTASY_GAME_METADATA='/fantasy/v2/game/{0}/metadata'

# Fetch specified leagues under a game. 
# Params: {game_key} & comma separated {league_key}
YFANTASY_GAME_LEAGUES='/fantasy/v2/game/{0}/leagues;league_keys={1}' 

# Fetch specified players under a game.
# Params: {game_key} & comma seperated {player_key}
YFANTASY_GAME_PLAYERS='/fantasy/v2/game/{0}/players;player_keys={1}'

# Fetch start and end date information for each week in the game.
# Params: {game_key}
YFANTASY_GAME_WEEKS='/fantasy/v2/game/{0}/game_weeks'

# Fetch detailed description of all available stat categories for the game.
# Params: {game_key}
YFANTASY_GAME_STAT_CATEGORIES='/fantasy/v2/game/{0}/stat_categories'

# Fetch detailed description of all player position types for the game.
# Params: {game_key}
YFANTASY_GAME_POSITION_TYPES='/fantasy/v2/game/{0}/position_types'

# Fetch detailed description of all roster positions for the game.
# Params: {game_key}
YFANTASY_GAME_ROSTER_POSITIONS='/fantasy/v2/game/{0}/roster_positions'