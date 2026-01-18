# Problem Name : Rest API 2 / Football Competitin Winners's Goals
import requests

def getWinnerTotalGoals(competition_name, year):
    # Get competition winner
    comp_url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition_name}&year={year}"
    comp_response = requests.get(comp_url).json()
    winner = comp_response['data'][0]['winner']

    total_goals = 0

    # Winner as team1
    page = 1
    while True:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition_name}&year={year}&team1={winner}&page={page}"
        response = requests.get(url).json()

        for match in response['data']:
            total_goals += int(match['team1goals'])

        if page >= response['total_pages']:
            break
        page += 1

    # Winner as team2
    page = 1
    while True:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition_name}&year={year}&team2={winner}&page={page}"
        response = requests.get(url).json()

        for match in response['data']:
            total_goals += int(match['team2goals'])

        if page >= response['total_pages']:
            break
        page += 1

    return total_goals


# Test
competition_name = "UEFA Champions League"
year = 2011

print(getWinnerTotalGoals(competition_name, year))
