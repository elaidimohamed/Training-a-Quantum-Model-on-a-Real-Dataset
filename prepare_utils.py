import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from qiskit_algorithms.utils import algorithm_globals

def data_preprocess(dataset):
    """
    Preprocesses a given dataset by performing feature scaling and splitting it into training and testing sets.

    Parameters:
    - dataset: A callable dataset object (e.g., from `sklearn.datasets`) that provides `.data` (features) 
      and `.target` (labels). This should be a dataset such as `load_iris`, `load_wine`, etc.

    Returns:
    - dataset_train_features: Preprocessed training feature data (scaled).
    - dataset_test_features: Preprocessed test feature data (scaled).
    - dataset_train_labels: Training labels corresponding to the training features.
    - dataset_test_labels: Test labels corresponding to the test features.
    - data_set_num_features: The number of features in the dataset (after scaling).
    
    The function scales the features using `MinMaxScaler` to a range of [0, 1], and splits the data into training 
    and testing sets using an 80-20 split, with stratified sampling based on the labels.
    """
    data = dataset()
    dataset_features = data.data
    dataset_labels = data.target
    dataset_features = MinMaxScaler().fit_transform(dataset_features)
    algorithm_globals.random_seed = 4701
    data_set_num_features = dataset_features.shape[1]
    dataset_train_features, dataset_test_features, dataset_train_labels, dataset_test_labels = train_test_split(
        dataset_features, dataset_labels, train_size=0.8, stratify=dataset_labels, random_state=algorithm_globals.random_seed)
    
    print(f'{dataset.__name__} preprocessed')
    return dataset_train_features, dataset_test_features, dataset_train_labels, dataset_test_labels, data_set_num_features
