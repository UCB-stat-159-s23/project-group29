from sklearn.metrics import confusion_matrix 
import matplotlib.pyplot as plt
import pandas as pd


def get_confusion_matrix(y_true, y_pred):
    """
    Calculates and returns the confusion matrix for a given set of true and predicted y-values.
    It is returned as a Pandas DataFrame for future easier manipulation.

    Parameters:
        y_true (Pandas Series): The true labels of the target variable.
        y_pred (Pandas Series): The predicted labels of the target variable.

    Returns:
        Pandas DataFrame: a Pandas DataFrame containing the true negative, false positive, false negative, and true positive
        values that a model predicts.
    """
    # Get values in array form of the confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Get all the values from the confusion matrix as a 1-D array.
    cm_flat = cm.ravel()
    
    # Put the confusion matrix values into a pandas DataFrame for easier manipulation
    # TN = true negative, FP = false positive, FN = false negative, TP = true positive
    df = pd.DataFrame(cm_flat.reshape(1, -1), columns=['TN', 'FP', 'FN', 'TP'])
    
    return df


def calculate_tpr_fpr(df, row):
    """
    This function takes in a Pandas DataFrame with columns TP, FP, FN, and TN, 
    and calculates the true positive rate (TPR) and false positive rate (FPR):
    
    Parameters:
        df (Pandas DataFrame): a Pandas DataFrame with columns TP, FP, FN, and TN
        row (integer): row number from which to extract the TP, FP, FN, and TN to calculate the TPR and FPR.

    Returns:
        tuple: a tuple containing tpr (true positive rate) and fpr (false positive rate) as percentage % rounded to 2 decimal places
    """
    tp = df.loc[row, 'TP']
    fp = df.loc[row, 'FP']
    fn = df.loc[row, 'FN']
    tn = df.loc[row, 'TN']
    
    # turn into percentage % and round to two decimal places
    tpr = round((tp / (tp + fn))*100, 2)
    fpr = round((fp / (fp + tn))*100, 2)
    
    return tpr, fpr


    