import pandas as pd

def inspect_dataframe(data):
    df = pd.DataFrame(data)
    rows = df.shape[0]
    cols = df.shape[1]

    return {
        "rows": rows,
        "cols": cols,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "total_values": rows * cols
    }