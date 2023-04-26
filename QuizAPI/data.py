import requests
parameters = {
    'amount':10,
    'category':18,
    'difficulty':"medium",
    'type': "boolean"

}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()['results']
print(question_data)
