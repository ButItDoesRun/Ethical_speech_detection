from Functions import *

class Response(object):
    def __init__(self, comment,response):
        self.comment = comment
        self.response = response        

    def get_score_from_response(self):
        response = self.response
        score_list = dict()

        try:        
            for attribute in response['attributeScores']:
                summary_score = response['attributeScores'][attribute]['summaryScore']
                score_list[attribute] = summary_score['value']
        except:
            score_list = handle_score_list_error()        
 
        self.score_list = dict(sorted(score_list.items(), reverse=True))        