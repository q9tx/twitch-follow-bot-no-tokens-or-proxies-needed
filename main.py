import requests
import json

url = 'https://q9tx.com/send-followers'

headers = {"Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://q9tx.com",
    "Referer": "https://q9tx.com/follow.html",
    "Sec-CH-UA": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
                  }

payload = {"username":"wwwwwvwvw"}

response = requests.post(url, headers=headers, json=payload)

print(response.text)