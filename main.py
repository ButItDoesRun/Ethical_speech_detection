import os
import numpy as np
import pandas as pd

from API import *
from Request import *
from Response import *

#Instantiate client
client = Google_api_client()

#Get data
os.chdir('C:/MyJupyterNotebooks/ThesisProject/Data/jigsaw-toxic-comment-classification-challenge/train.csv')
data = pd.read_csv('train.csv')

df = pd.DataFrame(data)
df_top = df.head(10)

print(df_top)

# print(data.isnull().sum())
# print(data.info())

# file = open('comments.txt', 'r')
# data = file.read()
# file.close()
# data_list = list(data.split(";")) 


df = df_top
for idx in df.index:  
    id = df['id'][idx]
    comment = df['comment_text'][idx]
    
    #Create new request
    request = Request()
    #Execute request
    request.execute_request(client,comment,threshold=0)

# for label, content in df_top.loc[:,['id', 'comment_text']].items():
#     print(f'label:{label}')
#     print(f'content:{content}')

# for comment in data_list:
#     #Create new request
#     request = Request()

#     #Execute request
#     request.execute_request(client,comment,threshold=0)
    



