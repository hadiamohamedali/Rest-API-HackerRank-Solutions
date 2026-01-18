# Problem Name : Rest API 1 / Total Goals by a Team
import os
import requests

def getTotalGoals(team, year):
    total_goals = 0

    # Team as team1
    page = 1
    while True:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
        response = requests.get(url).json()

        for match in response['data']:
            total_goals += int(match['team1goals'])

        if page >= response['total_pages']:
            break
        page += 1

    # Team as team2
    page = 1
    while True:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"
        response = requests.get(url).json()

        for match in response['data']:
            total_goals += int(match['team2goals'])

        if page >= response['total_pages']:
            break
        page += 1

    return total_goals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input().strip()
    year = int(input().strip())

    result = getTotalGoals(team, year)
    fptr.write(str(result) + '\n')

    fptr.close()

