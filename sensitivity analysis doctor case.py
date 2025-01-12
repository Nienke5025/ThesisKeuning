# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:13:34 2024

@author: Nienke Keuning
"""

import numpy as np
import matplotlib.pyplot as plt

#constants
beta = 5.2/365 #probability that a patient visits the gp
mu = 28 #average patients per day gp


#baseline variables as used in the main paper
baseline_par = {
    "V": 6,
    "P": 1,
    "C": 2,
    "C_h": 1.3,
    "a": 0.7, 
    "u":28
    
}

#variables
variable_ranges = {
    "V": np.linspace(2, 15, 400),
    "P": np.linspace(0, 5.3, 400),
    "C": np.linspace(0, 60, 400),
    "C_h": np.linspace(1, 16, 400)
}

#Labels to use in plots latex
latex_labels = {
    "V": r"$V$",
    "P": r"$P$",
    "C": r"$C$",
    "C_h": r"$C_h$"
}


#function for calculating optimal lambda in the onsite case
def optimal_lambda_onsite(V,P,C,C_h,a,u):
    return (np.sqrt((-C * C_h * a**2 + (-C * V + C * P + 3 * C * C_h) * a + 2 * C * V - 2 * C * P - 2 * C * C_h) * u) + (-C_h * a - V + P + C_h) * u) / (C_h * a**2 + (V - P - 3 * C_h) * a - 2 * V + 2 * P + 2 * C_h)

def lambda_feasible_upper_bound(V,P,C,C_h,a,u):
    return min((1/(2-a))*(u-(((1-a)*C)/(a*C_h))), u/(2-a)-C/(V-P-(1-a)*C_h))

#function for calculating the total market size
def total_market_size(optimal_lambda,beta):
    return optimal_lambda/beta

#baseline lambda
lambda_baseline = optimal_lambda_onsite(**baseline_par)
effects = {}
normalized_effects = {}
#lambda_feasible_upper_bound = min((1/(2-a))*(u-(((1-a)*C)/(a*C_h))), u/(2-a)-C/(V-P-(1-a)*C_h))

for var, values in variable_ranges.items():
    lambdas = [
        optimal_lambda_onsite(**{**baseline_par, var: value})
        for value in values
    ]
    
    #Check if it is a feasible region
    feasible_lambdas=[min(lambd,lambda_feasible_upper_bound(**{**baseline_par, var: value})) 
                      for lambd,value in zip(lambdas,values)]  #lambda optimal and otherwise the highest value of lambda within feasibility
    
    #plotting
    plt.plot(values,lambdas)
    plt.plot(values,feasible_lambdas)
    plt.xlabel(f"{latex_labels[var]}")
    plt.ylabel(r'$\Lambda_{opt}$')
    plt.grid(True)
    plt.show()
    
    #calculate effect
    effect_size = feasible_lambdas[-1] - feasible_lambdas[0]
    range_length = max(values)-min(values)
    effects[var] = effect_size
    normalized_effects[var] = effect_size/range_length
    
for var, effect in normalized_effects.items():
    print(f"{var}: Normalized Effect = {effect:.4f}")
    
    
    