import os
import numpy as np
import pandas as pd

from API import *
from Request import *
from Response import *

#Instantiate client
client = Google_api_client()

#Get data
file = open('comments.txt', 'r')
data = file.read()
file.close()
data_list = list(data.split(";")) 

for comment in data_list:
    #Create new request
    request = Request()

    #Execute request
    request.execute_request(client,comment,threshold=0)
    



