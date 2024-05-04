from googleapiclient import discovery
from request import *
import json


class google_api_client(object):
    def __init__(self,api_key):
        #Establish connection to Perpective API
        client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=api_key,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
        )
        self.client = client
    
    def analyze_request(self, data):
        request = format_request(data)
        response = self.client.comments().analyze(body=request).execute()
        str_response = json.dumps(response,indent=2)
        return str_response
     

