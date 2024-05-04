from API import *

#Get API Key locally to keep it hidden (security reasons)
file = open('../YourAPIKey.txt', 'r')
API_KEY = file.read()
file.close()

#Instantiate client
client = google_api_client.__new__(google_api_client)
client.__init__(API_KEY)

#Provide data
file = open('comments.txt', 'r')
data = file.read()
file.close()

#Analyze data
response = client.analyze_request(data)

#Print response in terminal
print(response)




