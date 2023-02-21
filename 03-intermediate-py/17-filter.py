# FILTER: filter: Una función que se ejecutara para cada elemento iterable. iterable: Lo que se va a filtrar.


numbers = [1,2,3,4,5,6,7,8]

filter_numbers = list(filter(lambda x : x % 2 == 0, numbers))

print(numbers, filter_numbers) # [1, 2, 3, 4, 5, 6, 7, 8] [2, 4, 6, 8]


# FILTER DICT: 

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

# print the matches with winners

winners_filter = list(filter(lambda match : match['home_team_result'] == 'Win', matches))
print(winners_filter)

# [{'home_team': 'Bolivia', 'away_team': 'Uruguay', 'home_team_score': 3, 'away_team_score': 1, 'home_team_result': 'Win'}, 
# {'home_team': 'Ecuador', 'away_team': 'Venezuela', 'home_team_score': 5, 'away_team_score': 0, 'home_team_result': 'Win'}]











