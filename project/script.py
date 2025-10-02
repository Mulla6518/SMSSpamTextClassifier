

import pandas as pd
import re
from sklearn.model_selection import train_test_split
import os

# Load the dataset
data = pd.read_csv("spam.csv", encoding="latin-1")[['v1', 'v2']]
data.columns = ['label', 'message']

# Preprocess text: lowercasing, removing special characters
def preprocess_text(text):
    text = text.lower()  # Lowercase text
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip()

data['message'] = data['message'].apply(preprocess_text)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)

def create_model_format(arg1, arg2, arg3):
    os.makedirs("./output/" + arg1 + "/ham", exist_ok=True)
    os.makedirs("./output/" + arg1 + "/spam", exist_ok=True)
    # # Counters for file naming
    ham_count = 1
    spam_count = 1

    # # Iterate through each row and write to the appropriate folder
    for row1, row2 in zip(arg2, arg3):
        label = row1
        message = row2
        if label == 'ham':
            filename = f'./output/{arg1}/ham/{ham_count}.txt'
            ham_count += 1
        elif label == 'spam':
            filename = f'./output/{arg1}/spam/{spam_count}.txt'
            spam_count += 1
        else:
            continue  # skip if label is not ham or spam
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(message)

create_model_format("train_data", y_train, X_train)
create_model_format("test_data", y_test, X_test)
