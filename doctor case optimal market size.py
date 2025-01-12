# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:36:33 2024

@author: Nienke Keuning
"""

import numpy as np
import matplotlib.pyplot as plt

V=6
P=1
C=2
H=1.3
a=0.7
u=28
Lambda = np.linspace(0, 21.03, 400)


L = (np.sqrt((-C * H * a**2 + (-C * V + C * P + 3 * C * H) * a + 2 * C * V - 2 * C * P - 2 * C * H) * u) + (-H * a - V + P + H) * u) / (H * a**2 + (V - P - 3 * H) * a - 2 * V + 2 * P + 2 * H)
beta=5.2/365

total= L/beta
total_2 = 21.03/beta

CS = Lambda*(V-P-(1-a)*H-(2-a)*C*(1/(u-Lambda*(2-a))))
CS_nonnegative = np.maximum(CS,0)

plt.plot(Lambda,CS_nonnegative,color="red")
plt.xlabel(r'$\Lambda$ (per day)')
plt.ylabel('CS')
plt.legend()
plt.grid(True)
plt.show()







































































