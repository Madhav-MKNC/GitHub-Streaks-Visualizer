import requests

username = 'your_username'
access_token = 'your_access_token'

api_url = 'https://api.github.com/graphql'

query = """
{
    user(login: "%s") {
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
    contribution_days = data['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
    # Your logic to process contribution_days and visualize the data goes here
    print(contribution_days)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
