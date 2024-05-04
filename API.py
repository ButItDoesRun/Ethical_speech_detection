from googleapiclient import discovery
import json

#Get API Key from local text file to hide it
file = open('../YourAPIKey.txt', 'r')
API_KEY = file.read()
file.close()

#Establish connection to Perpective API
client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

#create a request
analyze_request = {
  'comment': { 'text': 'you massive bitch!' },
  'requestedAttributes': {'TOXICITY': {}}
}

#Get a response
response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))
