# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:13:25 2024

@author: Nienke Keuning
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#%%
#In this first example we will optimize the market size (Lambda) wrt alpha
#initialize parameters according to figure 4 in main paper
V = 6
C = 2
P = 1
u = 0.9
H=1.3
t_1 = 0
t_2 = 0.2

#Market size for optimal consumer surplus
a_range = np.linspace(0, 1, 400)

def Lambda_opt_1(a_range):
    return (np.sqrt(((-C**2 * a_range**2 + 4 * C**2 * a_range - 4 * C**2) * t_1 + (C * P - C * V) * a_range + 2 * C * V - 2 * C * P) * u) + ((2 * C - C * a_range) * t_1 - V + P) * u) / ((C * a_range**2 - 4 * C * a_range + 4 * C) * t_1 + (V - P) * a_range - 2 * V + 2 * P)

def Lambda_opt_2(a_range):
    return (np.sqrt(((-C**2 * a_range**2 + 4 * C**2 * a_range - 4 * C**2) * t_2 + (C * P - C * V) * a_range + 2 * C * V - 2 * C * P) * u) + ((2 * C - C * a_range) * t_2 - V + P) * u) / ((C * a_range**2 - 4 * C * a_range + 4 * C) * t_2 + (V - P) * a_range - 2 * V + 2 * P)


Lambda_opt_1_values = Lambda_opt_1(a_range)
Lambda_opt_2_values = Lambda_opt_2(a_range)

#market size is bounded
constraint_2_t1 = (1/(2-a_range))*(u-((1-a_range)*C)/(H-(2-a_range)*t_1*C))
constraint_3_t1 = u/(2-a_range)-C/(V-P-(2-a_range)*t_1*C)
constraint_2_t2 = (1/(2-a_range))*(u-((1-a_range)*C)/(H-(2-a_range)*t_2*C))
constraint_3_t2 = u/(2-a_range)-C/(V-P-(2-a_range)*t_2*C)

Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)
Lambda_opt_2_bound = np.minimum(constraint_2_t2,constraint_3_t2)
Lambda_opt_2_bound = np.minimum(Lambda_opt_2_bound,Lambda_opt_2_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 
Lambda_opt_2_bound[Lambda_opt_2_bound<0] = np.nan

#create a plot
plt.plot(a_range,Lambda_opt_1_bound,label=r"$\tau$ = 0",color="red")
plt.plot(a_range,Lambda_opt_2_bound,label=r"$\tau$ = 0.2",color="blue")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\Lambda^o_{opt}$')
plt.legend()
plt.grid(True)
plt.show()

#%%
#In this second example we will optimize the market size (Lambda) wrt mu
#initialize parameters according to figure 4 in main paper
V = 6
P = 1
a = 0.7
C = 2
t_1 = 0
t_2 = 0.2

#variable C
u_range = np.linspace(0.5, 2, 400)

#Market size for optimal consumer surplus
def Lambda_opt_1(u_range):
    return (np.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_1 + (C * P - C * V) * a + 2 * C * V - 2 * C * P) * u_range) + ((2 * C - C * a) * t_1 - V + P) * u_range) / ((C * a**2 - 4 * C * a + 4 * C) * t_1 + (V - P) * a - 2 * V + 2 * P)

def Lambda_opt_2(u_range):
    return (np.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_2 + (C * P - C * V) * a + 2 * C * V - 2 * C * P) * u_range) + ((2 * C - C * a) * t_2 - V + P) * u_range) / ((C * a**2 - 4 * C * a + 4 * C) * t_2 + (V - P) * a - 2 * V + 2 * P)

Lambda_opt_1_values = Lambda_opt_1(u_range)
Lambda_opt_2_values = Lambda_opt_2(u_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u_range-((1-a)*C)/(H-(2-a)*t_1*C))
constraint_3_t1 = u_range/(2-a)-C/(V-P-(2-a)*t_1*C)
constraint_2_t2 = (1/(2-a))*(u_range-((1-a)*C)/(H-(2-a)*t_2*C))
constraint_3_t2 = u_range/(2-a)-C/(V-P-(2-a)*t_2*C)

Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)
Lambda_opt_2_bound = np.minimum(constraint_2_t2,constraint_3_t2)
Lambda_opt_2_bound = np.minimum(Lambda_opt_2_bound,Lambda_opt_2_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 
Lambda_opt_2_bound[Lambda_opt_2_bound<0] = np.nan


#create a plot
plt.plot(u_range,Lambda_opt_1_bound, label=r"$\tau$ = 0",color="red")
plt.plot(u_range,Lambda_opt_2_bound, label=r"$\tau$ = 0.2",color="blue")
plt.xlabel(r'$\mu$')
plt.ylabel(r'$\Lambda^o_{opt}$')
plt.legend()
plt.grid(True)
plt.show()