# https://developer.yahoo.com/fantasysports/guide/user-resource.html
# https://developer.yahoo.com/fantasysports/guide/users-collection.html

# Fetch the Games in which the user has played. 
# Additionally accepts flags is_available to only return available games.
YFANTASY_USER_GAMES='/fantasy/v2/users;use_login=1/games'

# Fetch leagues that the user belongs to in one or more games. 
# The leagues will be scoped to the user. 
# This will throw an error if any of the specified games do not support league sub-resources.
# Params: {game_key1,game_key2,...}
YFANTASY_USER_GAMES_LEAGUES='/fantasy/v2/users;use_login=1/games;game_keys={0}/leagues'

# Fetch teams owned by the user in one or more games. 
# The teams will be scoped to the user. 
# This will throw an error if any of the specified games do not support team sub-resources.
# Params: {game_key1,game_key2,...}
YFANTASY_USER_GAMES_TEAMS='/fantasy/v2/users;user_login=1/games;game_keys={0}/teams'

# Fetch user information of the logged-in user.
YFANTASY_USER_METADATA='/fantasy/v2/users;use_login=1'