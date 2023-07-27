# Make a request to the ISS location API
import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response)
# print(response.status_code)

# Use the request module to raise an exception
response.raise_for_status()

# Response Codes
# 1XX - Hold on
# 2XX - Here you go
# 3XX - Go away / No Permission
# 4XX - You screwed up
# 5XX - Server screwed up

data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)