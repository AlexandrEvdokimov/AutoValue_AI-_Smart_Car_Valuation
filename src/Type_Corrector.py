import pandas as pd

def Type_Corrector(X_train):
    X = X_train.copy()
    X['transmission'] = (X['transmission'] == 'Automatic').astype(int)
    X['insurance_valid'] = (X['insurance_valid'] == 'Yes').astype(int)

    for col in  X.select_dtypes(include = ['str','object']).columns.tolist():
        X[col] = X[col].astype('category')
    return X
