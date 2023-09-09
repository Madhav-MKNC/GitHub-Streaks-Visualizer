import requests

import os 
from dotenv import load_dotenv
load_dotenv()

# username = "madhav-mknc"
username = 'AryanGodara'
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

# Sort the data based on 'date' key
all_contribution_data = sorted(all_contribution_data, key=lambda x: x['date'])

# Create a set to store unique dates
unique_dates = set()

# List to store unique contributions (without duplicates)
unique_contributions = []

# Iterate through the sorted data and add only unique dates to the list
for contribution in all_contribution_data:
    date = contribution['date']
    if date not in unique_dates:
        unique_dates.add(date)
        unique_contributions.append(contribution)

# Now, 'unique_contributions' contains only unique contributions based on the 'date' key

data = unique_contributions
streaks = []
current_streak = 0

for day in data:
    if day['contributionCount'] > 0:
        current_streak += 1
    else:
        current_streak = 0
    streaks.append({
        "date": day['date'],
        "streak": current_streak
    })
    print({
        "date": day['date'],
        "streak": current_streak
    })

   
# for i in data:
#    print(f"date: {i['date']}\tcontributions: {i['contributionCount']}")
   

# show graph
import matplotlib.pyplot as plt

# # Extract date and contributionCount values
# dates = [entry['date'] for entry in data]
# contributions = [entry['contributionCount'] for entry in data]

# # Create the plot
# plt.figure(figsize=(10, 6))
# plt.plot(dates, contributions, marker='o', linestyle='-', color='b')
# plt.title('Contributions Over Time')
# plt.xlabel('Date')
# plt.ylabel('Contribution Count')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# # Display the plot
# plt.tight_layout()
# plt.grid(True)
# plt.show()


import matplotlib.pyplot as plt
from datetime import datetime

# Extract date and streak values
dates = [entry['date'] for entry in streaks]
streak_values = [entry['streak'] for entry in streaks]

# Extract and format month names
month_names = [datetime.strptime(date, '%Y-%m-%d').strftime('%b %Y') for date in dates]

# Create a list to store unique month names
unique_month_names = []
unique_dates = []

# Loop through dates to get unique month names
for date, month_name in zip(dates, month_names):
    if month_name not in unique_month_names:
        unique_month_names.append(month_name)
        unique_dates.append(date)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates, streak_values, marker='o', linestyle='-', color='b')
plt.title('Streaks Over Time')
plt.xlabel('Date')
plt.ylabel('Streak Count')
plt.xticks(unique_dates, unique_month_names, rotation=45)  # Use unique month dates as labels

# Display the plot
plt.tight_layout()
plt.grid(True)
plt.show()
