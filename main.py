import requests
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

load_dotenv(".env")

USERNAME = getenv("USERNAME_PIXE")
TOKEN = getenv("TOKEN_PIXE")
GRAPH1_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

#--------------------CREATING USER

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#--------------------CREATING GRAPH

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH1_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/aestro7/graphs/graph1.html

#--------------------POSTING TO GRAPH

graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}"

today = datetime.now().strftime("%Y%m%d")

graph_post_config = {
    "date": today,
    "quantity": "10.5"
}

# response = requests.post(url=graph_post_endpoint, json=graph_post_config, headers=headers)
# print(response.text)

update_date = today

graph_update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}/{update_date}"

graph_update_pixel_config = {
    "quantity": "12"
}

# response = requests.put(url=graph_update_pixel_endpoint, json=graph_update_pixel_config, headers=headers)

#--------------------DELETING PIXEL

delete_date = "20240228"

graph_delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}/{delete_date}"

# response = requests.delete(url=graph_delete_pixel_endpoint, headers=headers)

