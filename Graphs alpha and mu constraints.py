# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:06:38 2024

@author: Nienke Keuning
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#%% constraints with respect to the service rate online case
#initialize variables
V = 6
C = 2
alpha = 0.7
tau_1 = 0.2
tau_2 = 0
P=1
H=1.3
mu = np.linspace(0, 2, 400)

#functions for the 3 bounds on the market size
constraint_2 = (1/(2-alpha))*(mu-(((1-alpha)*C)/(H-(2-alpha)*tau_1*C)))
constraint_3 = mu/(2-alpha)-C/(V-P-(2-alpha)*tau_1*C)

#Market size is always larger than zero
constraint_2[constraint_2<0]=np.nan
constraint_3[constraint_3<0]=np.nan

#create a plot
plt.plot(mu,constraint_2, label=r"$\Lambda< \frac{1}{q_J(2-\alpha)}(\mu-\frac{(1-\alpha)C}{C_h-(2-\alpha)\tau C})$",color="green")
plt.plot(mu,constraint_3, label=r"$\Lambda\leq\frac{\mu}{2-\alpha}-\frac{C}{V-P-(2-\alpha)\tau C}$",color="purple")
plt.fill_between(mu,constraint_2,color='lightblue')
plt.xlabel(r'$\mu$')
plt.ylabel(r'$\Lambda$')
plt.legend()
plt.grid(True)
plt.show()

#%% constraints with respect to the satisfaction rate online case
#initialize variables
V = 6
C = 2
mu = 0.9
tau_1 = 0.2
tau_2 = 0
P=1
H=1.3
alpha = np.linspace(0, 1, 400)

#functions for the 3 bounds on the market size
constraint_2 = (1/(2-alpha))*(mu-(((1-alpha)*C)/(H-(2-alpha)*tau_1*C)))
constraint_3 = mu/(2-alpha)-C/(V-P-(2-alpha)*tau_1*C)

#Market size is always larger than zero
constraint_2[constraint_2<0]=np.nan
constraint_3[constraint_3<0]=np.nan

# Function to find intersection
def find_intersection(alpha_val):
    return (1/(2-alpha_val))*(mu-(((1-alpha_val)*C)/(H-(2-alpha_val)*tau_1*C))) - \
           (mu/(2-alpha_val)-C/(V-P-(2-alpha_val)*tau_1*C))

# Solve for intersection alpha
alpha_intersection = fsolve(find_intersection, 0.5)[0]
lambda_intersection = (1/(2-alpha_intersection))*(mu-(((1-alpha_intersection)*C)/(H-(2-alpha_intersection)*tau_1*C)))

#create a plot
plt.plot(alpha,constraint_2, label=r"$\Lambda< \frac{1}{q_J(2-\alpha)}(\mu-\frac{(1-\alpha)C}{C_h-(2-\alpha)\tau C})$",color="green")
plt.plot(alpha,constraint_3, label=r"$\Lambda\leq\frac{\mu}{2-\alpha}-\frac{C}{V-P-(2-\alpha)\tau C}$",color="purple")
plt.fill_between(alpha,constraint_2,where=(constraint_2<constraint_3), color='lightblue')
plt.fill_between(alpha,constraint_3,where=(constraint_2>constraint_3),color='lightblue')
plt.scatter(alpha_intersection, lambda_intersection, color='blue', label=f'Intersection ({alpha_intersection:.2f}, {lambda_intersection:.2f})')
plt.xlim(0,1)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\Lambda$')
plt.legend()
plt.grid(True)
plt.show()

#%% constraints with respect to the service rate onsite case
#initialize variables
V = 6
C = 2
alpha = 0.7
P=1
H=1.3
mu = np.linspace(0, 2, 400)

#functions for the 3 bounds on the market size
constraint_2 = (1/(2-alpha))*(mu-(((1-alpha)*C)/(alpha*H)))
constraint_3 = mu/(2-alpha)-C/(V-P-(1-alpha)*H)

#Market size is always larger than zero
constraint_2[constraint_2<0]=np.nan
constraint_3[constraint_3<0]=np.nan

#create a plot
plt.plot(mu,constraint_2, label=r"$\Lambda< \frac{1}{q_J(2-\alpha)}(\mu-\frac{(1-\alpha)C}{\alpha C_h}$) ",color="green")
plt.plot(mu,constraint_3, label=r"$\Lambda\leq\frac{\mu}{2-\alpha}-\frac{C}{V-P-(1-\alpha)C_h}$",color="purple")
plt.fill_between(mu,constraint_2,color='lightblue')
plt.xlabel(r'$\mu$')
plt.ylabel(r'$\Lambda$')
plt.legend()
plt.grid(True)
plt.show()

#%% constraints with respect to the satisfaction rate onsite case
#initialize variables
V = 6
C = 2
mu = 0.9
P=1
H=1.3
alpha = np.linspace(0, 1, 400)

#functions for the 3 bounds on the market size
constraint_2 = (1/(2-alpha))*(mu-(((1-alpha)*C)/(alpha*H)))
constraint_3 = mu/(2-alpha)-C/(V-P-(1-alpha)*H)

#Market size is always larger than zero
constraint_2[constraint_2<0]=np.nan
constraint_3[constraint_3<0]=np.nan

# Function to find intersection
def find_intersection(alpha_val):
    return (1 / (2 - alpha_val)) * (mu - (((1 - alpha_val) * C) / (alpha_val * H))) - \
           (mu / (2 - alpha_val) - C / (V - P - (1 - alpha_val) * H))

# Solve for intersection alpha
alpha_intersection = fsolve(find_intersection, 0.5)[0]
lambda_intersection = (1 / (2 - alpha_intersection)) * (mu - (((1 - alpha_intersection) * C) / (alpha_intersection * H)))

#create a plot
plt.plot(alpha,constraint_2, label=r"$\Lambda< \frac{1}{q_J(2-\alpha)}(\mu-\frac{(1-\alpha)C}{\alpha C_h}$) ",color="green")
plt.plot(alpha,constraint_3, label=r"$\Lambda\leq\frac{\mu}{2-\alpha}-\frac{C}{V-P-(1-\alpha)C_h}$",color="purple")
plt.fill_between(alpha,constraint_2,where=(constraint_2<constraint_3), color='lightblue')
plt.fill_between(alpha,constraint_3,where=(constraint_2>constraint_3),color='lightblue')
plt.scatter(alpha_intersection, lambda_intersection, color='blue', label=f'Intersection ({alpha_intersection:.2f}, {lambda_intersection:.2f})')
plt.xlim(0,1)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\Lambda$')
plt.legend()
plt.grid(True)
plt.show()