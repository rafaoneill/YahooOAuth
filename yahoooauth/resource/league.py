# https://developer.yahoo.com/fantasysports/guide/league-resource.html
# https://developer.yahoo.com/fantasysports/guide/leagues-collection.html

# Fetch league key, id, name, url, draft status, number of teams, and current week information.
# Params: {league_key}
YFANTASY_LEAGUE_METADATA='/fantasy/v2/league/{0}/metadata'

# Fetch league settings.
# For instance, draft type, scoring type, roster positions, stat categories and modifiers, divisions.
# Params: {league_key}
YFANTASY_LEAGUE_SETTINGS='/fantasy/v2/league/{0}/settings'

# Fetch ranking of teams within the league. 
# Accepts Teams as a sub-resource, and includes team_standings data by default beneath the teams.
# Params: {league_key}
YFANTASY_LEAGUE_STANDINGS='/fantasy/v2/league/{0}/standings'

# Fetch league scoreboard for current week. 
# Accepts Matchups as a sub-resource, which in turn accept Teams as a sub-resource. 
# Includes team_stats data by default.
# Params: {league_key}
YFANTASY_LEAGUE_SCOREBOARD_CURRENT_WEEK='/fantasy/v2/league/{0}/scoreboard'

# Fetch league scoreboard for a specific week. 
# Accepts Matchups as a sub-resource, which in turn accept Teams as a sub-resource. 
# Includes team_stats data by default.
# Params: {league_key} {week}
YFANTASY_LEAGUE_SCOREBOARD_CURRENT_WEEK='/fantasy/v2/league/{0}/scoreboard;week={1}'

# Fetch all teams in the league.
# Params: {league_key}
YFANTASY_LEAGUE_TEAMS='/fantasy/v2/league/{0}/teams'

# Fetch the league's eligible players.
# Params: {league_key}
YFANTASY_LEAGUE_PLAYERS='/fantasy/v2/league/{0}/players'

# Fetch draft results for all teams in the league.
# Params: {league_key}
YFANTASY_LEAGUE_DRAFT_RESULTS='/fantasy/v2/league/{0}/draftresults'

# Fetch league transactions -- adds, drops, and trades.
# Params: {league_key}
YFANTASY_LEAGUE_TRANSACTIONS='/fantasy/v2/league/{0}/transactions'

# Fetch specific leagues {league_key1} and {league_key2}
# Params: {league_key1,league_key2,...}
YFANTASY_SPECIFIC_LEAGUES='/fantasy/v2/leagues;league_keys={0}'