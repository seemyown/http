import requests

hulk_url = 'https://akabab.github.io/superhero-api/api/id/332.json'
captain_url = 'https://akabab.github.io/superhero-api/api/id/149.json'
thanos_url = 'https://akabab.github.io/superhero-api/api/id/655.json'

hulk_response = requests.get(hulk_url)
captain_response = requests.get(captain_url)
thanos_response = requests.get(thanos_url)

hulk = hulk_response.json()
captain = captain_response.json()
thanos = thanos_response.json()

hulk_intel = hulk['powerstats']['intelligence']
captain_intel = captain['powerstats']['intelligence']
thanos_intel = thanos['powerstats']['intelligence']

if hulk_intel > captain_intel and hulk_intel > thanos_intel:
    print('Самый умный - Халк')
elif captain_intel > hulk_intel and captain_intel > thanos_intel:
    print('Самый умный - Капитан Америка')
else:
    print('Самый умный - Танос')

