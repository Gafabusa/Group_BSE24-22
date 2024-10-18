import os
import requests

# Replace with your actual API token and username
api_token = os.getenv("PYTHONANYWHERE_API_TOKEN")  # Best practice: use environment variables
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

# Pull the latest code from the Willy-Gafabusa branch
def pull_latest_code():
    branch = "Willy-Gafabusa"  # Your branch name
    os.system(f"git pull origin {branch}")  # Pull from Willy-Gafabusa branch
    print(f"Latest code pulled from branch '{branch}' on GitHub.")

# Main deployment process
if __name__ == "__main__":
    pull_latest_code()
    restart_web_app()
