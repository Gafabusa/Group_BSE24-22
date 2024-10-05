import os
import requests


api_token = os.getenv("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDBuS8ao+lUWi8uWD9BrmeWDOx+smYM+qVal0x1/cNjB1QXPXI7Lq1N0MkIhnvVU2JgPHO/zMkVqyZM0HMJoPNP5Ul6aJUCscQfqW
C3QlaF58YxdDkVj35j65KKP0mD/lDLxlHjQYw/qTwK1wKzc3rvCO9kkXCZeBSABxU50lALEQtliNKbT/xmkhVka+MzhNLULryilNdc2gsQFEZa+ZzjAOtbFNshdFqgZpFPUP/q4Yl/
wAOnp0rjPjKx43aml6q6sVKwBuUKiSMG/kps7uss7x+VOk0zWFaE+1gs5jqfgh1GYaCGM6ykhbukqlqpbHYWUhLsiNz40L3y+w7y3UopsyYZu5o0RlnulOgI8z8jR+037RfSiNNVh8
KLEWaUdyWGC3LPsjlWsz1wLGwnGlWGDM5VW/A4MtU6fVUSMHQ/iFCX0Js/SH0/3DOBwZwQ6XSKqWeM0TDliJzwxafPdZVjxSNFjpaJhz0PqwuO62SmKeshcpNph7hZhFxmMkkLLeza
IiyhN5AEbihCE1EmMs9NCkPtc0xO+GBTljFwE49ryEGmxey+/BhGnqCXi9JibMbvfa8CbJ7WnkA2WGw17xT8VknslDYIywR+go4ESXjW2cIahMFEMe6ntpxNqNQXr7RIrl8zs/d6uR
Z5mAKTbTKhN0s6kTUo3Rp8oEETQI4y0w== Ssebatta1414@blue-liveconsole11")  # Best practice: use environment variables
username = "Ssebatta1414"

# Headers for authentication
headers = {
    "Authorization": f"Token {api_token}"
}

# Restart the web app
def restart_web_app():
    url = f"https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{username}.pythonanywhere.com/reload/"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print("Web app reloaded successfully!")
    else:
        print(f"Failed to reload web app: {response.content}")

# Pull the latest code
def pull_latest_code():
    os.system("git pull origin main")
    print("Latest code pulled from GitHub.")

# Main deployment process
if __name__ == "__main__":
    pull_latest_code()
    restart_web_app()
