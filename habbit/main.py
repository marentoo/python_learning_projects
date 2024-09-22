import requests
from datetime import datetime as dt
from config.py import TOKEN, USERNAME, COLOR1, GRAPH_ID



pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#use only once --> then comment
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id" : GRAPH_ID,
    "name" : "Reading Graph",
    "unit" : "pages",
    "type": "int",
    "color" : COLOR1
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url = graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year month day)
today = dt.now().strftime('%Y%m%d')

pixel_params = {
    "date": "today", # yyyyMMdd
    "quantity": "40"
}

# response = requests.post(url=pixel_endpoint, json = pixel_params, headers = headers)
# print(response.text)

yesterday = dt(year = 2024, month = 9,day=21)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"



response = requests.delete(url = delete_endpoint, headers=headers)
print(response.text)