# -*- coding: utf-8 -*-
"""
Created on Sat April 6 20:30:43 2024

@author: MDelapa
"""

import numpy as np
import matplotlib.pyplot as plt

# Prior belief: Uniform distribution between 0 and 1
prior_samples = np.random.uniform(0, 1, size=10000)

# Number of heads and tails observed in coin flips
num_heads = 6
num_tails = 4

# Likelihood function: Binomial distribution
Likelihood_heads = lambda p: p ** num_heads * (1 - p) ** num_tails

# Posterior calculation using Bayes' theorem
def posterior(prior, likelihood):
    return likelihood(prior) * 1  # Uniform prior, so prior and posterior are proportional

# Calculate posterior distribution
posterior_samples = posterior(prior_samples, likelihood_heads)

# Plotting
plt.figure(figsize=(10, 6))

plt.hist(posterior_samples, bins=50, density=True, alpha=0.5, color='blue', label='Posterior')
plt.xlabel('Probability of landing heads (p)')
plt.ylabel('Density')
plt.title('Posterior Distribution after observing 6 heads and 4 tails')
plt.legend()
plt.grid(True)
plt.show()
