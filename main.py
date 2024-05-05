from API import *
from Request import *
from Response import *

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
data_list = list(data.split(";")) 

for comment in data_list:
    #Create new request
    request = Request.__new__(Request)
    request.__init__(
        toxicity=True,
        severe_toxicity=True,
        identity_attack=False,
        insult=False, 
        profanity=False, 
        threat=False
    )

    request.execute_request(client,comment,threshold=0.3)
    



