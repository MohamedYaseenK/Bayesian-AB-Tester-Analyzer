import re
import pandas as pd

METRIC_SHEETS = {
    "experiment_two": {
        "access": "Metric Access",
        "performed_activities": "Metric Performed Activities",
        "performed_corrections": "Metric Performed Corrections",
    },
    "experiment_one": {
        "cost": "Metric Cost",
        "grade": "Metric Grade",
        "time": "Metric Time",
    },
}

def load_metric(path, sheet_name):
    raw = pd.read_excel(path, sheet_name=sheet_name, header=None)

    header_row = None
    for i in range(len(raw)):
        if "T1" in raw.iloc[i].values:
            header_row = i
            break

    header = raw.iloc[header_row]
    data = raw.iloc[header_row + 1:].copy()
    data.columns = header

    treatment_cols = [c for c in data.columns if isinstance(c, str) and re.fullmatch(r"T\d+", c)]
    data = data[treatment_cols].dropna(how="all")
    return data

def get_variant_data(path, sheet_name, variant):
    data = load_metric(path, sheet_name)
    return data[variant].dropna().tolist()
