import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'job title':2})

print(r.json())