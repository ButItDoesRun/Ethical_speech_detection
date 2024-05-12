from Response import *

class Request(object):        
    #Formats requested attributes
    def format_req_att(self,comment, threshold):
        request_object = {
            'comment': { 
                'text': comment, 
                'type':'PLAIN_TEXT' 
            },
             'requestedAttributes': {
                 'TOXICITY':{'scoreThreshold':threshold},
                 'SEVERE_TOXICITY': {'scoreThreshold':threshold},
                 'IDENTITY_ATTACK': {'scoreThreshold':threshold},
                 'INSULT': {'scoreThreshold':threshold},
                 'PROFANITY': {'scoreThreshold':threshold},
                 'THREAT': {'scoreThreshold':threshold}
             }
        }
            
        return request_object
    
    #Executes the comment_analyzer for one request
    def execute_request(self, client, comment,threshold):
        #Format request and set a threshold [range(0,1)] 
        formatted_req = self.format_req_att(comment=comment, threshold=threshold)
        
        #Analyze data
        try:
            response_data = client.analyze_request(formatted_req)
        except Exception as error:
            response_data = {}
            print("An error occurred:", error)

        #Create Response 
        response = Response(comment = comment, response = response_data)

        #Get score
        response.get_score_from_response()

        #print score
        # print("comment: "+response.comment)
        # print("score: "+str(response.score_list))

        return response.score_list
    
        #show all data from response:
        #print(response.response)


 




