import pandas as pd
import numpy as np

def file_reader(file):
    data = pd.read_csv(file)
    return data

def preprocessing():
    pass

def null_function():
    if data.isnull().values.any():
        data = data.dropna()
    return data

def duplicates_function():
    if data.duplicated().any():
        data = data.drop_duplicates()
    return data

def handeling_catogorical_data_function():
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for i in data.columns:
        if data[i].dtypes == 'object':
            data[i] = le.fit_transform(data[i])
    return data

def imbalanced_data_function():
    from imblearn.over_sampling import SMOTE
    smote = SMOTE()

def normailization_of_data_function():
    pass
def feature_removing_function():
    pass

def data_spliting_function(target):
    from sklearn.model_selection import train_test_split
    X = data.drop(target, axis=1)
    y = data[target]
    x_train, x_test, y_train, y_test = train_test_split(data, test_size=0.2, random_state=0)
    return x_train, x_test, y_train, y_test

def model_tranning_function():
    pass
def accuracy_checker_function():
    pass