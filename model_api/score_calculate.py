import numpy as np

def score_transform_series(series, base=600, odds_score=30, times=2):

    p1 = np.array(series)
    p0 = 1-p1

    odds = p1 / p0
    factor = odds_score / np.log(times)
    offset = base - factor * np.log(1)
    score = np.log(odds) * factor + offset

    return float(score)