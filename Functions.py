import pandas as pd

def save_progress(count, data):
    if count % 1000 == 0:
        try:
            perspective_df = pd.DataFrame(data)
            perspective_df.to_csv(f'perspective_train{count}.csv', encoding='utf-8', index=False)
            print(f'csv file saved for count: {count}')
        except PermissionError:
            print('perspective_train{count}.csv already exists')

def handle_score_list_error():
    score_list = dict()
    attribute_list = {'TOXICITY', 'THREAT', 'SEVERE_TOXICITY', 'PROFANITY', 'INSULT', 'IDENTITY_ATTACK'}
    for attribute in attribute_list:
        score_list[attribute] = None

    return score_list