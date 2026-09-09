import numpy as np

def posterior_samples(total_count, n_obs, prior_shape=1, prior_rate=1, n_samples=10000):
    shape = prior_shape + total_count
    rate = prior_rate + n_obs
    return np.random.gamma(shape, 1 / rate, n_samples)
