from googleapiclient import discovery

class Google_api_client(object):
    def __init__(self):
        #Get API Key locally to keep it hidden (security reasons)
        file = open('../YourAPIKey.txt', 'r')
        self.api_key = file.read()
        file.close()

        #Establish connection to Perpective API
        client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=self.api_key,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
        )
        self.client = client

    #analyse_request method
    def analyze_request(self, request):
        req = request
        try:
            response = self.client.comments().analyze(body=req).execute()
        except Exception as error:
            response = {}
            print("An error occurred:", error)

        #returns a Python object
        return response


