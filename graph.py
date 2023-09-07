import requests

import os 
from dotenv import load_dotenv
load_dotenv()

username = "madhav-mknc"
access_token = os.getenv("GITHUB_TOKEN")

api_url = 'https://api.github.com/graphql'

query = """
query {
  user(login: "%s") {
    login
    contributionsCollection {
      contributionCalendar {
        totalContributions

        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
""" % username

variables = {
    'login': username,
    'after': None
}

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

all_contribution_data = []

  
def fetch():
  global all_contribution_data
  global variables
  
  while True:
      response = requests.post(api_url, json={'query': query, 'variables': variables}, headers=headers)
      data = response.json()
      print(len(data))
      # for i in data:
      #     print(i, data[i])


      # if 'errors' in data:
      #     raise Exception(data['errors'][0]['message'])

      contribution_data = data['data']['user']['contributionsCollection']
      weeks = contribution_data['contributionCalendar']['weeks']

      for week in weeks:
         days = week['contributionDays']
         for day in days:
            all_contribution_data.append(day)

      if not weeks or len(weeks) < 52:
          break

      variables['after'] = weeks[-1]['contributionDays'][-1]['date']
      


try:
   fetch()
except KeyboardInterrupt:
   pass


# printing
all_contribution_data = sorted(all_contribution_data, key=lambda x: x['date'])

for i in all_contribution_data:
   print(f"date: {i['date']}\tcontributions: {i['contributionCount']}")
   