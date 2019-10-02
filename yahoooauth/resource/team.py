# https://developer.yahoo.com/fantasysports/guide/team-resource.html
# https://developer.yahoo.com/fantasysports/guide/roster-resource.html

# Fetch team key, id, name, url, division ID, logos, and team manager information.
# Params: {team_key}
YFANTASY_TEAM_METADATA='/fantasy/v2/team/{0}/metadata'

# Fetch team statistical data and points for the season.
# Params: {team_key}
YFANTASY_TEAM_SEASON_STATS='/fantasy/v2/team/{0}/stats'

# Fetch team statistical data and points for a specific week.
# Params: {team_key} {week}
YFANTASY_TEAM_WEEK_STATS='/fantasy/v2/team/{0}/stats;type=week;week={1}'

# Fetch team rank, wins, losses, ties, and winning percentage (as well as divisional data if applicable).
# Params: {team_key}
YFANTASY_TEAM_STANDINGS='/fantasy/v2/team/{0}/standings'

# Fetch team roster. 
# Accepts a week parameter. 
# Also accepts Players as a sub-resource (included by default).
# Params: {team_key} {week}
YFANTASY_TEAM_ROSTER='/fantasy/v2/team/{0}/roster;week={1}'

# Fetch list of players drafted by the team.
# Params: {team_key}
YFANTASY_TEAM_DRAFTRESULTS='/fantasy/v2/team/{0}/draftresults'

# Fetch all the matchups this team has scheduled (for H2H leagues).
# Params: {team_key}
YFANTASY_TEAM_ALL_MATCHUPS='/fantasy/v2/team/{0}/matchups'

# Fetch specific matchups for this team (for H2H leagues).
# Params: {team_key} {weeks}
YFANTASY_TEAM_SPECIFIC_MATCHUPS='/fantasy/v2/team/{0}/matchups;weeks={1}'

# Access the players collection within the roster.
# Params: {team_key}
YFANTASY_ROSTER_PLAYERS='/fantasy/v2/team/{0}/players'