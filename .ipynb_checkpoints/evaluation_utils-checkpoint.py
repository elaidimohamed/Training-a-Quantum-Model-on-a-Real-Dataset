import pandas as pd
from sklearn.metrics import classification_report

def generate_classification_report(model, X_test, y_test, model_name="Model"):
    """
    Generates a classification report and returns it as a DataFrame.

    Parameters:
    - model: Trained classification model (e.g., QSVC, SVC, etc.)
    - X_test: The test data used for prediction
    - y_test: The true labels of the test data
    - model_name: The name of the model (for labeling the report)

    Returns:
    - DataFrame containing classification metrics (precision, recall, F1-score, support)
    """
    # Predict with the model
    y_pred = model.predict(X_test)
    
    # Get the classification report as a dictionary
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    
    # Convert the report dictionary to a DataFrame
    report_df = pd.DataFrame(report_dict).transpose()

    # Add a column for the model name
    report_df['Model'] = model_name
    
    return report_df