from API import *
from Request import *

#Get API Key locally to keep it hidden (security reasons)
file = open('../YourAPIKey.txt', 'r')
API_KEY = file.read()
file.close()

#Instantiate client
client = Google_api_client.__new__(Google_api_client)
client.__init__(API_KEY)

#Provide data
file = open('comments.txt', 'r')
data = file.read()
file.close()

#create new request
request = Request.__new__(Request)
request.__init__(
    toxicity=True,
    severe_toxicity=True,
    identity_attack=False,
    insult=False, 
    profanity=False, 
    threat=True
    )

#format request attributes and set a threshold range(0,1) 
formatted_req = request.format_req_att(comment=data, threshold=0.3)
#print(str(formatted_req))

#Analyze data
response = client.analyze_request(formatted_req)

#Print response in terminal
print(response)




