from googleapiclient import discovery

class Google_api_client(object):
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

    #analyse_request method
    def analyze_request(self, request):
        req = request
        response = self.client.comments().analyze(body=req).execute()
        #returns a Python object
        return response
    '''
    #analyse_request method
    def analyze_request(self, request):
        req = request
        response = self.client.comments().analyze(body=req).execute()
        str_response = json.dumps(response,indent=2)
        return str_response
    '''
     

