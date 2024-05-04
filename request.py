def format_request(comment):
    #create a request object
    request_object = {
    'comment': { 
        'text': comment, 
        'type':'PLAIN_TEXT' 
        },
    'requestedAttributes': {
        'TOXICITY': {}
        }
    }

    return request_object



