import pandas as pd

def select_column(data, column):
    df = pd.DataFrame(data)
    df[column].tolist()
    values = df[column].tolist()

    return {
        "values": values,
        "length": len(values)
        
    }