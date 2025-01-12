# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:07:50 2025

@author: Nienke Keuning
"""

import numpy as np
import matplotlib.pyplot as plt

P=1
C=2
C_h=1.3
a=0.7
u=28

#Market size for optimal consumer surplus
V_range = np.linspace(0, 10, 400)


def Lambda_opt_1(V_range):
    return (np.sqrt((-C * C_h * a**2 + (-C * V_range + C * P + 3 * C * C_h) * a + 2 * C * V_range - 2 * C * P - 2 * C * C_h) * u) + (-C_h * a - V_range + P + C_h) * u) / (C_h * a**2 + (V_range - P - 3 * C_h) * a - 2 * V_range + 2 * P + 2 * C_h)

Lambda_opt_1_values = Lambda_opt_1(V_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u-((1-a)*C)/(a*C_h))
constraint_3_t1 = u/(2-a)-C/(V_range-P-(1-a)*C_h)


Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 

#create a plot
plt.plot(V_range,Lambda_opt_1_bound,color="red")
plt.xlabel('V')
plt.ylabel(r'$\Lambda^s_{opt}$')
plt.grid(True)
plt.show()

#%%

V=6
C=2
C_h=1.3
a=0.7
u=28

#Market size for optimal consumer surplus
P_range = np.linspace(0, 10, 400)


def Lambda_opt_1(P_range):
    return (np.sqrt((-C * C_h * a**2 + (-C * V + C * P_range + 3 * C * C_h) * a + 2 * C * V - 2 * C * P_range - 2 * C * C_h) * u) + (-C_h * a - V + P_range + C_h) * u) / (C_h * a**2 + (V - P_range - 3 * C_h) * a - 2 * V + 2 * P_range + 2 * C_h)

Lambda_opt_1_values = Lambda_opt_1(P_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u-((1-a)*C)/(a*C_h))
constraint_3_t1 = u/(2-a)-C/(V-P_range-(1-a)*C_h)


Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 

#create a plot
plt.plot(P_range,Lambda_opt_1_bound,color="red")
plt.xlabel('P')
plt.ylabel(r'$\Lambda^s_{opt}$')
plt.grid(True)
plt.show()

#%%
P=1
V=6
C_h=1.3
a=0.7
u=28

#Market size for optimal consumer surplus
C_range = np.linspace(0, 100, 400)


def Lambda_opt_1(C_range):
    return (np.sqrt((-C_range * C_h * a**2 + (-C_range * V + C_range * P + 3 * C_range * C_h) * a + 2 * C_range * V - 2 * C_range * P - 2 * C_range * C_h) * u) + (-C_h * a - V + P + C_h) * u) / (C_h * a**2 + (V - P - 3 * C_h) * a - 2 * V + 2 * P + 2 * C_h)

Lambda_opt_1_values = Lambda_opt_1(C_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u-((1-a)*C_range)/(a*C_h))
constraint_3_t1 = u/(2-a)-C_range/(V-P-(1-a)*C_h)


Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 

#create a plot
plt.plot(C_range,Lambda_opt_1_bound,color="red")
plt.xlabel('C')
plt.ylabel(r'$\Lambda^s_{opt}$')
plt.grid(True)
plt.show()

#%%
P=1
V=6
C=2
a=0.7
u=28

#Market size for optimal consumer surplus
C_h_range = np.linspace(1, 17, 400)


def Lambda_opt_1(C_h_range):
    return (np.sqrt((-C * C_h_range * a**2 + (-C * V + C * P + 3 * C * C_h_range) * a + 2 * C * V - 2 * C * P - 2 * C * C_h_range) * u) + (-C_h_range * a - V + P + C_h_range) * u) / (C_h_range * a**2 + (V - P - 3 * C_h_range) * a - 2 * V + 2 * P + 2 * C_h_range)

Lambda_opt_1_values = Lambda_opt_1(C_h_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u-((1-a)*C)/(a*C_h_range))
constraint_3_t1 = u/(2-a)-C/(V-P-(1-a)*C_h_range)


Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 

#create a plot
plt.plot(C_h_range,Lambda_opt_1_bound,color="red")
plt.xlabel(r'$C_h$')
plt.ylabel(r'$\Lambda^s_{opt}$')
plt.grid(True)
plt.show()