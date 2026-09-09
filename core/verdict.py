def get_verdict(prob_b_beats_a, min_confidence=0.95):
    if prob_b_beats_a >= min_confidence:
        return "SHIP"
    if prob_b_beats_a <= 1 - min_confidence:
        return "HOLD"
    return "INCONCLUSIVE"
