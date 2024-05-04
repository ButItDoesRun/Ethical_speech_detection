class Request(object):
    def __init__(self,toxicity, severe_toxicity, identity_attack, insult,profanity,threat):
        self.toxicity = toxicity
        self.severe_toxicity = severe_toxicity
        self.identity_attack = identity_attack
        self.insult = insult
        self.profanity = profanity
        self.threat = threat
        self.check_input()
    
    #Raises a TypeError if class attributes are not type bool  
    def check_input(self):
        attrs_list = self.__dict__.items()
        for attr in attrs_list:
            if not type(attr[1]) is bool:
                raise TypeError("parameter: '"+attr[0]+"' from Request, must be a bool, not "+str(type(attr[1])))
        
    #Formats requested attributes
    def format_req_att(self,comment):
        request_object = {
            'comment': { 
                'text': comment, 
                'type':'PLAIN_TEXT' 
            },
             'requestedAttributes': {
                 'TOXICITY':{},
                 'SEVERE_TOXICITY': {},
                 'IDENTITY_ATTACK': {},
                 'INSULT': {},
                 'PROFANITY': {},
                 'THREAT': {}
             }
        }
     
        if self.toxicity != True:
            del request_object['requestedAttributes']['TOXICITY']
        
        if self.severe_toxicity != True:
            del request_object['requestedAttributes']['SEVERE_TOXICITY']
        
        if self.identity_attack != True:
            del request_object['requestedAttributes']['IDENTITY_ATTACK']
        
        if self.insult != True:
            del request_object['requestedAttributes']['INSULT']

        if self.profanity != True:
            del request_object['requestedAttributes']['PROFANITY']
        
        if self.threat != True:
            del request_object['requestedAttributes']['THREAT']
            
        return request_object



