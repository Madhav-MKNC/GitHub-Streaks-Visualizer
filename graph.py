import requests

username = "madhav-mknc"
access_token = "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"

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

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

response = requests.post(api_url, json={'query': query}, headers=headers)

if response.status_code == 200:
    data = response.json()
    # print(data)

    contribution_days = data['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
    # Your logic to process contribution_days and visualize the data goes here
    # print(contribution_days)
    for i in contribution_days:
        print(i)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
