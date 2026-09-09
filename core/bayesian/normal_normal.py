import numpy as np

def posterior_samples(sample_mean, sample_std, n_obs, prior_mean=0, prior_std=1000, n_samples=10000):
    prior_precision = 1 / prior_std ** 2
    data_precision = n_obs / sample_std ** 2
    posterior_precision = prior_precision + data_precision
    posterior_mean = (prior_precision * prior_mean + data_precision * sample_mean) / posterior_precision
    posterior_std = (1 / posterior_precision) ** 0.5
    return np.random.normal(posterior_mean, posterior_std, n_samples)
