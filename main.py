import os
import numpy as np
import pandas as pd
import time

from API import *
from Request import *
from Response import *
from Functions import * 

#Instantiate client
client = Google_api_client()

#Get data
os.chdir('C:/MyJupyterNotebooks/ThesisProject/Data/jigsaw-toxic-comment-classification-challenge/train.csv')
data = pd.read_csv('train.csv')

df = pd.DataFrame(data)
# df_top = df.head(600)
# df = df_top
# print(df_top)

# existing_data = pd.read_csv('perspective_train.csv')
# print(existing_data)

perspective_data = []
count = 0

for idx in df.index:  
    count += 1    
    if count % 60 == 0:
        time.sleep(60)

    #Initialize the variables and output
    id = df['id'][idx]
    comment = df['comment_text'][idx]

    output_list = dict()
    output_list['id'] = id
    output_list['comment_text'] = comment

    #Create new request
    request = Request()

    #Execute request and save results
    try:
        score_list = request.execute_request(client,comment,threshold=0)
    except Exception as error: 
        score_list = handle_score_list_error()
        print("An error occurred:", error)

    #Add the score list to the output
    output_list.update(score_list)

    #Add the comment-entry with scores to our data list
    perspective_data.append(output_list)

    #Saves the progress once in a while so time isn't wasted
    save_progress(count, perspective_data)

perspective_df = pd.DataFrame(perspective_data)

try:
    perspective_df.to_csv('perspective_train_final.csv', encoding='utf-8', index=False)
except PermissionError:
     print('perspective_train.csv already exists')

print('Code finished executing')
# for comment in data_list:
#     #Create new request
#     request = Request()

#     #Execute request
#     request.execute_request(client,comment,threshold=0)
    



