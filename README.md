# Quantum Classification with Qiskit

This repository demonstrates how quantum computing techniques can be applied to classification tasks using **Qiskit**, a powerful quantum computing framework. The project primarily focuses on implementing **Quantum Support Vector Classifier (QSVC)** with various quantum feature maps and entanglement strategies. Additionally, it includes advanced methods for **model evaluation**, **visualization**, and comparison of quantum feature maps' performance.

## Features

- **Data Preprocessing**: 
    - Scales dataset features using `MinMaxScaler` to standardize the range of features.
    - Splits the dataset into training and testing sets with an 80-20 split, preserving label distributions.

- **Quantum Classification**: 
    - Implements **Quantum Support Vector Classifier (QSVC)** utilizing quantum kernels for improved performance.
    - Supports different **Quantum Feature Maps** (ZZFeatureMap) to transform classical data into quantum features.

- **Quantum Feature Maps**: 
    - Experiments with **ZZFeatureMap** with different entanglement strategies:
        - **Linear Entanglement**: Simple linear coupling between qubits.
        - **Circular Entanglement**: Circular coupling for more complex entanglement patterns.
        - **Full Entanglement**: Fully connected entanglement across all qubits for maximum expressive power.
    
- **Model Evaluation**:
    - Generates **classification reports** that evaluate the performance of QSVC models on the test dataset.
    - **Visualizes performance metrics** comparing models with different quantum feature maps and entanglement strategies.

## Data Visualization
![download](https://github.com/user-attachments/assets/4ea25028-6266-43f9-9de1-a70dc59ae84a)

### Classification Performance

This project includes various visualizations of classification performance. These plots illustrate how different feature maps and entanglement strategies affect the accuracy of quantum classifiers.

#### ZZFeatureMap Visualization

Visualize the different quantum feature map circuits used in the model, including the entanglement structure:

![ZZFeatureMap](https://github.com/user-attachments/assets/941b1d8a-3fc8-45a3-8d0f-e7f43e620093)

#### Entanglement Strategy Comparison

Comparing various entanglement strategies used in the **ZZFeatureMap** to see their effects on classification accuracy:

![Evaluate different Entanglement](https://github.com/user-attachments/assets/8ca6532d-f330-401e-8931-54911c9b1158)

#### Feature Importance

This section includes visualizations of the importance of various features in the model and how they impact the classifier's performance:

![Feature Importance](https://github.com/user-attachments/assets/eccd4392-9034-45ed-a3c1-ff98dd46a674)
![Feature Importance 2](https://github.com/user-attachments/assets/041d0090-2653-42c4-9830-d3f3b63e1a09)

