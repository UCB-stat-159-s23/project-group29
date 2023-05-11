import numpy as np
import pandas as pd
from utils import *

def test_calculate_tpr_fpr():
    # Test Case 0
    df = pd.DataFrame({'TP': [200], 'FP': [0], 'FN': [0], 'TN': [200]})
    tpr, fpr = calculate_tpr_fpr(df, 0)
    
    assert np.isclose(tpr, 100.0, rtol=1e-2)
    assert np.isclose(fpr, 0.0, rtol=1e-2)
    
    # Test Case 1
    df1 = pd.DataFrame({'TP': [100], 'FP': [50], 'FN': [20], 'TN': [80]})
    tpr1, fpr1 = calculate_tpr_fpr(df1, 0)
    assert np.isclose(tpr1, 83.33, rtol=1e-2)
    assert np.isclose(fpr1, 38.46, rtol=1e-2)
    
def test_get_confusion_matrix(): 
    # Test case 0: all predictions are correct
    y_true = pd.Series([1, 0, 1, 0, 1])
    y_pred = pd.Series([1, 0, 1, 0, 1])
    expected_output = pd.DataFrame([[2, 0, 0, 3]], columns=['TN', 'FP', 'FN', 'TP'])
    output = get_confusion_matrix(y_true, y_pred)
    assert output.columns.tolist() == expected_output.columns.tolist()
    assert output.values.tolist() == expected_output.values.tolist()

    # Test case 1: all predictions are incorrect
    y_true = pd.Series([1, 0, 1, 0, 1])
    y_pred = pd.Series([0, 1, 0, 1, 0])
    expected_output = pd.DataFrame([[0, 2, 3, 0]], columns=['TN', 'FP', 'FN', 'TP'])
    output = get_confusion_matrix(y_true, y_pred)
    assert output.columns.tolist() == expected_output.columns.tolist()
    assert output.values.tolist() == expected_output.values.tolist()
