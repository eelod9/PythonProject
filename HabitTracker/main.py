import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME= "ellagot9"
TOKEN = "ahsdkfjdlfkaeiivr3"
GRAPHID = "graph1"

today = datetime.now()
DATE= today.strftime("%Y%m%d")
#created user account on pixela
user_params = {
    "token":"ahsdkfjdlfkaeiivr3",
    "username": "ellagot9",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


pixela_graph_definition = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params= {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}

make_change_toGraph= {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
    #"optionalData"
}

pixela_graph_change_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
#response = requests.post(url= pixela_graph_change_url,json = make_change_toGraph,headers=headers)
#response = requests.post(url=pixela_graph_definition, json= graph_params,headers=headers)
#response = requests.post(url=pixela_endpoint,json=user_params)
#Graph site
#https://pixe.la/v1/users/ellagot9/graphs/graph1.html

print(today.strftime("%Y%m%d"),)

#update a pixel
update_endpoint_url= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}"
update_pix={
    "quantity": "100"
}
#response = requests.put(url=update_endpoint_url, json =update_pix, headers= headers )


#delete pixel
response = requests.delete(url=update_endpoint_url, headers= headers)
print(response.text)