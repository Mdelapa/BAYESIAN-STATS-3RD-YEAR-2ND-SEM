# -*- coding: utf-8 -*-
"""

Created on Sun Apr 28 23:55:27 2024

@author: MDelapa
"""

import pymc3 as pm
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 10, 100)
true_slope = 2
true_intercept = 5
y = true_intercept + true_slope * x + np.random.normal(0, 1, size=100)

# Plot the synthetic data
plt.scatter(x, y)  # Changed from X to x
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Synthetic Data')
plt.show()

# Extend x for forecasting
x_forecast = np.linspace(10, 15, 50)

# Model
with pm.Model() as model:
    # Priors
    alpha = pm.Normal('alpha', mu=0, sd=10)
    beta = pm.Normal('beta', mu=0, sd=10)
    sigma = pm.HalfNormal('sigma', sd=1)

   # Likelihood
   mu = alpha + beta * x
   likelihood = pm.Normal('y', mu=mu, sd=sigma, observed=y)
   
   # Forecasting
   mu_forecast = alpha + beta * x_forecast
   y_forecast = pm.Normal('y_forecast', mu=mu_forecast, sd=sigma, shape=len(x_forecast))

   # Inference
   t,,race = pm.sample(2000, tune=1000)

# Results
pm.traceplot(trace)
plt.show()

# Plot the forecasted data
plt.plot(x_forecast, np.mean(trace['y_forecast'], axis=0), color='red', label='Forecast')
plt.fill_between(x_forecast, 
                 np.percentile(trace['y_forecast'], 2.5, axis=0),
                 np.percentile(trace['y_forecast'], 97.5, axis=0), 
                 color='blue', alpha=0.2, label='95% Credible Interval')

plt.xlabel('X')
plt.ylabel('Y')
pltt.title('Forecasted Data')
plt.legend()
plt.show()
