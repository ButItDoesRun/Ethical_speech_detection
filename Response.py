class Response(object):
    def __init__(self, comment,response):
        self.comment = comment
        self.response = response

    def get_score_from_response(self):
        response = self.response
        hasScore = False
        score_list = dict()
        for category in response:
            if category == 'attributeScores':
                hasScore = True
                for attr in response[category]:
                    for attr_info in response[category][attr]:
                        if attr_info == 'summaryScore':
                            value = response[category][attr][attr_info]
                            score = value['value']
                            score_list[attr] = score

        if hasScore == False:
            print("No score available for this comment within given score threshold. Try another threshold or attribute")
        
        self.score_list = score_list