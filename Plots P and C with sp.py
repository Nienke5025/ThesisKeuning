# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:15:12 2024

@author: Nienke Keuning
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#%%
#In this first example we will optimize the market size (Lambda) wrt P 
#initialize parameters according to figure 4 in main paper
V = 6
C = 2
a = 0.7
u = 0.9
t_1 = 0
t_2 = 0.2
H = 1.3
P = sp.symbols('P')

#Calculate zero point for P
Lambda_opt_S1 = (sp.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_1 + (C * P - C * V) * a + 2 * C * V - 2 * C * P) * u) + ((2 * C - C * a) * t_1 - V + P) * u) / ((C * a**2 - 4 * C * a + 4 * C) * t_1 + (V - P) * a - 2 * V + 2 * P)
Lambda_opt_S2 = (sp.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_2 + (C * P - C * V) * a + 2 * C * V - 2 * C * P) * u) + ((2 * C - C * a) * t_2 - V + P) * u) / ((C * a**2 - 4 * C * a + 4 * C) * t_2 + (V - P) * a - 2 * V + 2 * P)
print(sp.solve(Lambda_opt_S1,P))
print(sp.solve(Lambda_opt_S2,P))

#Market size for optimal consumer surplus
P_range = np.linspace(0, 3.12, 400)


def Lambda_opt_1(P_range):
    return (np.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_1 + (C * P_range - C * V) * a + 2 * C * V - 2 * C * P_range) * u) + ((2 * C - C * a) * t_1 - V + P_range) * u) / ((C * a**2 - 4 * C * a + 4 * C) * t_1 + (V - P_range) * a - 2 * V + 2 * P_range)

def Lambda_opt_2(P_range):
    return (np.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_2 + (C * P_range - C * V) * a + 2 * C * V - 2 * C * P_range) * u) + ((2 * C - C * a) * t_2 - V + P_range) * u) / ((C * a**2 - 4 * C * a + 4 * C) * t_2 + (V - P_range) * a - 2 * V + 2 * P_range)


Lambda_opt_1_values = Lambda_opt_1(P_range)
Lambda_opt_2_values = Lambda_opt_2(P_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u-((1-a)*C)/(H-(2-a)*t_1*C))
constraint_3_t1 = u/(2-a)-C/(V-P_range-(2-a)*t_1*C)
constraint_2_t2 = (1/(2-a))*(u-((1-a)*C)/(H-(2-a)*t_2*C))
constraint_3_t2 = u/(2-a)-C/(V-P_range-(2-a)*t_2*C)

Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)
Lambda_opt_2_bound = np.minimum(constraint_2_t2,constraint_3_t2)
Lambda_opt_2_bound = np.minimum(Lambda_opt_2_bound,Lambda_opt_2_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 
Lambda_opt_2_bound[Lambda_opt_2_bound<0] = np.nan

#create a plot
plt.plot(P_range,Lambda_opt_1_bound,label=r"$\tau$ = 0",color="red")
plt.plot(P_range,Lambda_opt_2_bound,label=r"$\tau$ = 0.2",color="blue")
plt.xlabel('P')
plt.ylabel(r'$\Lambda^o_{opt}$')
plt.legend()
plt.grid(True)
plt.show()

#%%
#In this second example we will optimize the market size (Lambda) wrt C
#initialize parameters according to figure 4 in main paper
V = 6
P = 1
a = 0.7
u = 0.9
t_1 = 0
t_2 = 0.2
C = sp.symbols('C')

#Calculate zero point for P
Lambda_opt_S1 = (sp.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_1 + (C * P - C * V) * a + 2 * C * V - 2 * C * P) * u) + ((2 * C - C * a) * t_1 - V + P) * u) / ((C * a**2 - 4 * C * a + 4 * C) * t_1 + (V - P) * a - 2 * V + 2 * P)
Lambda_opt_S2 = (sp.sqrt(((-C**2 * a**2 + 4 * C**2 * a - 4 * C**2) * t_2 + (C * P - C * V) * a + 2 * C * V - 2 * C * P) * u) + ((2 * C - C * a) * t_2 - V + P) * u) / ((C * a**2 - 4 * C * a + 4 * C) * t_2 + (V - P) * a - 2 * V + 2 * P)
print(sp.solve(Lambda_opt_S1,C))
print(sp.solve(Lambda_opt_S2,C))

#variable C
C_range = np.linspace(0, 3.47, 400)

#Market size for optimal consumer surplus

def Lambda_opt_1(C_range):
    return (np.sqrt(((-C_range**2 * a**2 + 4 * C_range**2 * a - 4 * C_range**2) * t_1 + (C_range * P - C_range * V) * a + 2 * C_range * V - 2 * C_range * P) * u) + ((2 * C_range - C_range * a) * t_1 - V + P) * u) / ((C_range * a**2 - 4 * C_range * a + 4 * C_range) * t_1 + (V - P) * a - 2 * V + 2 * P)

def Lambda_opt_2(C_range):
    return (np.sqrt(((-C_range**2 * a**2 + 4 * C_range**2 * a - 4 * C_range**2) * t_2 + (C_range * P - C_range * V) * a + 2 * C_range * V - 2 * C_range * P) * u) + ((2 * C_range - C_range * a) * t_2 - V + P) * u) / ((C_range * a**2 - 4 * C_range * a + 4 * C_range) * t_2 + (V - P) * a - 2 * V + 2 * P)

Lambda_opt_1_values = Lambda_opt_1(C_range)
Lambda_opt_2_values = Lambda_opt_2(C_range)

#market size is bounded
constraint_2_t1 = (1/(2-a))*(u-((1-a)*C_range)/(H-(2-a)*t_1*C_range))
constraint_3_t1 = u/(2-a)-C_range/(V-P-(2-a)*t_1*C_range)
constraint_2_t2 = (1/(2-a))*(u-((1-a)*C_range)/(H-(2-a)*t_2*C_range))
constraint_3_t2 = u/(2-a)-C_range/(V-P-(2-a)*t_2*C_range)

Lambda_opt_1_bound = np.minimum(constraint_2_t1,constraint_3_t1)
Lambda_opt_1_bound = np.minimum(Lambda_opt_1_bound,Lambda_opt_1_values)
Lambda_opt_2_bound = np.minimum(constraint_2_t2,constraint_3_t2)
Lambda_opt_2_bound = np.minimum(Lambda_opt_2_bound,Lambda_opt_2_values)

#market size is nonnegative
Lambda_opt_1_bound[Lambda_opt_1_bound<0] = np.nan 
Lambda_opt_2_bound[Lambda_opt_2_bound<0] = np.nan

#create a plot
plt.plot(C_range,Lambda_opt_1_bound, label=r"$\tau$ = 0",color="red")
plt.plot(C_range,Lambda_opt_2_bound, label=r"$\tau$ = 0.2",color="blue")
plt.xlabel('C')
plt.ylabel(r'$\Lambda^o_{opt}$')
plt.legend()
plt.grid(True)
plt.show()
