# https://developer.yahoo.com/fantasysports/guide/game-resource.html
# https://developer.yahoo.com/fantasysports/guide/games-collection.html

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

# Fetch specific games {game_key1} and {game_key2}
# Params: {game_key1,game_key2,...}
YFANTASY_SPECIFIC_GAMES='/fantasy/v2/games;game_keys={0}'

# Fetch all games for the logged in user
YFANTASY_GAMES_FOR_LOGGED_USER='/fantasy/v2/users;user_login=1/games'

# Fetch specific games {game_key1} and {game_key2} that the logged in user owns teams in.
# Params: {game_key1,game_key2,...}
YFANTASY_SPECIFIC_GAMES_FOR_LOGGED_USER='/fantasy/v2/users;use_login=1/games;game_keys={0}'