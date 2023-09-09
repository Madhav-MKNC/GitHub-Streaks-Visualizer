# utilities / helper functions

from urllib.parse import urlparse
import requests

import os 
from dotenv import load_dotenv
load_dotenv()


# server address
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


# verify if the username is valid
def is_valid(username):
    url = f"https://github.com/{username}"
    try:
        response = requests.head(
            url = url,
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        )
        return response.status_code == 200
    except requests.RequestException:
        return False


# streaks data  
def get_user_streaks(username):
    streaks = [
        {'date': '2023-08-22', 'streak': 5},
        {'date': '2023-08-23', 'streak': 6},
        {'date': '2023-08-24', 'streak': 7},
        {'date': '2023-08-25', 'streak': 8},
        {'date': '2023-08-26', 'streak': 9}
    ]
    return streaks


