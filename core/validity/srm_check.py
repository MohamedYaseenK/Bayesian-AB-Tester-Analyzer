from scipy.stats import chisquare

def check_srm(observed_counts, expected_ratio=None):
    n = len(observed_counts)
    if expected_ratio is None:
        expected_ratio = [1 / n] * n
    total = sum(observed_counts)
    expected_counts = [r * total for r in expected_ratio]
    stat, p_value = chisquare(observed_counts, expected_counts)
    return {"p_value": float(p_value), "srm_flag": bool(p_value < 0.01)}