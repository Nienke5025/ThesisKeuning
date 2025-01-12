# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:09:25 2024

@author: Nienke Keuning
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, fsolve

#%%
#initiate values
V = 6
C = 2
alpha = 0.7
mu = 0.9
tau_1 = 0.2
tau_2 = 0
P=1
H=1.3
Lambda = np.linspace(0, 0.69, 400)

#Define the consumer surplus for two values of the delivery time
CS_1 = Lambda*(V-P-(2-alpha)*C*(1/(mu-Lambda*(2-alpha))+tau_1))
CS_2 = Lambda*(V-P-(2-alpha)*C*(1/(mu-Lambda*(2-alpha))+tau_2))

#maximize the consumer surplus
max_CS_1 = minimize_scalar(lambda x: -x * (V - P - (2 - alpha) * C * (1 / (mu - x * (2 - alpha)) + tau_1)),
                           bounds=(0, 0.69), method='bounded')
max_CS_2 = minimize_scalar(lambda x: -x * (V - P - (2 - alpha) * C * (1 / (mu - x * (2 - alpha)) + tau_2)),
                           bounds=(0, 0.69), method='bounded')

#Using the maximized value find x and y values
Lambda_max_1 = max_CS_1.x
CS_max_1 = -max_CS_1.fun
Lambda_max_2 = max_CS_2.x
CS_max_2 = -max_CS_2.fun

#Find root points of consumer surplus
#Define function to find root, such that root can be found for all values of lambda
def root_CS_1(Lambda_val):
    return Lambda_val * (V - P - (2 - alpha) * C * (1 / (mu - Lambda_val * (2 - alpha)) + tau_1))

#take initial guess 0.4, such that the second root is found
root_lambda_1 = fsolve(root_CS_1, 0.4)  

#repeat for the second function
def root_CS_2(Lambda_val):
    return Lambda_val * (V - P - (2 - alpha) * C * (1 / (mu - Lambda_val * (2 - alpha)) + tau_2))

root_lambda_2 = fsolve(root_CS_2, 0.4)  

#create a plot
plt.plot(Lambda,CS_1, label=r"$\tau=0.2$",color="blue")
plt.plot(Lambda,CS_2,label=r"$\tau=0$",color="red")
plt.scatter(Lambda_max_1, CS_max_1, color="blue", label=f"({Lambda_max_1:.2f}, {CS_max_1:.2f})")
plt.scatter(Lambda_max_2, CS_max_2, color="red", label=f"({Lambda_max_2:.2f}, {CS_max_2:.2f})")
plt.scatter(root_lambda_1[0], 0, color="green", label=f"({root_lambda_1[0]:.2f}, 0)")
plt.scatter(root_lambda_2[0], 0, color="orange", label=f"({root_lambda_2[0]:.2f}, 0)")
plt.ylim(0,0.21)
plt.xlim(0,0.5)
plt.xlabel(r'$\Lambda$')
plt.ylabel(r'CS')
plt.legend()
plt.grid(True)
plt.show()

#%%
V = 6
C = 2
alpha = 0.7
mu = 0.9
tau_1 = 0.2
tau_2 = 0
P=1
H=1.3
Lambda = np.linspace(0, 0.5, 400)

CS_1 = Lambda*(V-P-(2-alpha)*C*(1/(mu-Lambda*(2-alpha))+tau_1))

CS_2 = Lambda*(V-P-(2-alpha)*C*(1/(mu-Lambda*(2-alpha))+tau_2))

constraint_2 = (1/(2-alpha))*(mu-((1-alpha)*C)/(H-(2-alpha)*tau_2*C))
constraint_3 = mu/(2-alpha)-C/(V-P-(2-alpha)*tau_2*C)

#create a plot
plt.plot(Lambda,CS_2,label=r"$\tau=0$",color="red")
plt.axvline(constraint_2, color="green", linestyle="--", label=r"$\Lambda< \frac{1}{q_J(2-\alpha)}(\mu-\frac{(1-\alpha)C}{C_h-(2-\alpha)\tau C})$")
plt.axvline(constraint_3, color="purple", linestyle="--", label=r"$\Lambda\leq\frac{\mu}{2-\alpha}-\frac{C}{V-P-(2-\alpha)\tau C}$")
plt.xlim(0,0.5)
plt.ylim(0,0.21)
plt.xlabel(r'$\Lambda$')
plt.ylabel('CS')
plt.legend()
plt.grid(True)
plt.show()

#%%
V = 6
C = 2
alpha = 0.7
mu = 0.9
tau_1 = 0.2
tau_2 = 0
P=1
H=1.3
Lambda = np.linspace(0, 0.5, 400)

CS_1 = Lambda*(V-P-(2-alpha)*C*(1/(mu-Lambda*(2-alpha))+tau_1))

CS_2 = Lambda*(V-P-(2-alpha)*C*(1/(mu-Lambda*(2-alpha))+tau_2))

constraint_2 = (1/(2-alpha))*(mu-(((1-alpha)*C)/(H-(2-alpha)*tau_1*C)))
constraint_3 = mu/(2-alpha)-C/(V-P-(2-alpha)*tau_1*C)

#create a plot
plt.plot(Lambda,CS_1, label=r"$\tau=0.2$",color="blue")
plt.axvline(constraint_2, color="green", linestyle="--", label=r"$\Lambda< \frac{1}{q_J(2-\alpha)}(\mu-\frac{(1-\alpha)C}{C_h-(2-\alpha)\tau C})$")
plt.axvline(constraint_3, color="purple", linestyle="--", label=r"$\Lambda\leq\frac{\mu}{2-\alpha}-\frac{C}{V-P-(2-\alpha)\tau C}$")
plt.xlim(0,0.5)
plt.ylim(0,0.21)
plt.xlabel(r'$\Lambda$')
plt.ylabel('CS')
plt.legend()
plt.grid(True)
plt.show()

