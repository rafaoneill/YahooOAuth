# https://developer.yahoo.com/fantasysports/guide/player-resource.html
# https://developer.yahoo.com/fantasysports/guide/players-collection.html

# Fetch player key, id, name, editorial information, image, eligible positions, etc.
# Params: {player_key}
YFANTASY_PLAYER_METADATA='/fantasy/v2/player/{0}/metadata'

# Fetch player season stats and points (if in a league context).
# Params: {player_key}
YFANTASY_PLAYER_SEASON_STATS='/fantasy/v2/player/{0}/stats'

# Fetch player week stats and points (if in a league context).
# Params: {player_key} {week}
YFANTASY_PLAYER_WEEK_STATS='/fantasy/v2/player/{0}/stats;type=week;week={1}'

# Fetch The player ownership status within a league (whether they're owned by a team, on waivers, or free agents). 
# Only relevant within a league. 
# Params: {league_key} {player_key}
YFANTASY_PLAYER_OWNERSHIP='/fantasy/v2/league/{0}/players;player_keys={1}/ownership'

# Fetch data about ownership percentage of the player.
# Params: {player_key}
YFANTASY_PLAYER_PERCENT_OWNED='/fantasy/v2/player/{0}/percent_owned'

# Fetch average pick, average round and percent drafted.
# Params: {player_key}
YFANTASY_PLAYER_DRAFT_ANALYSIS='/fantasy/v2/player/{0}/draft_analysis'

# Fetch all players within a league.
# Params: {league_key}
YFANTASY_ALL_PLAYERS_FOR_LEAGUE='/fantasy/v2/league/{0}/players'

# Fetch all players from the leagues {league_key1} and {league_key2}
# Params: {league_key1,league_key2,...}
YFANTASY_ALL_PLAYERS_FOR_SPECIFIC_LEAGUES='/fantasy/v2/leagues;league_keys={0}/players'

# Fetch all players within a team.
# Params: {team_key}
YFANTASY_ALL_PLAYERS_FOR_TEAM='/fantasy/v2/team/{0}/players'

# Fetch all players from the teams {team_key1} and {team_key2}
# Params: {team_key1,team_key2,...}
YFANTASY_ALL_PLAYERS_FOR_SPECIFIC_TEAMS='/fantasy/v2/teams;team_keys={0}/players'

# Fetch specific players {player_key1} and {player_key2}
# Params: {player_key1,player_key2,...}
YFANTASY_SPECIFIC_PLAYERS='/fantasy/v2/players;player_keys={0}'