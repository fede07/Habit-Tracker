import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

USERNAME = getenv("USERNAME_PIXE")
TOKEN = getenv("TOKEN_PIXE")

print(f"usuario: {USERNAME} / token: {TOKEN}")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}