import numpy as np

def posterior_samples(successes, trials, prior_alpha=1, prior_beta=1, n_samples=10000):
    alpha = prior_alpha + successes
    beta = prior_beta + (trials - successes)
    return np.random.beta(alpha, beta, n_samples)
