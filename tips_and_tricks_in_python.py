import numpy as np
import PS1.fixed_income_derivatives_E2025 as fid    
import matplotlib.pyplot as plt
from scipy.optimize import minimize, Bounds

R = 0.06
K =100
pv_original = 98.74
T_N =10
# semi-annual coupons 
alpha = 0.5

# function definitions 
def pv(y,T,C):
    N =len(T)
    pv = 0 
    for i in range(0,N):
        pv += C[i]/(1+y)**T[i]
    return pv    

def ytm_obj(y, pv,T,C):
    pv_hat = pv_fct(y,T,C)
    se = (pv - pv_hat)**2
    return se 


# Where we have included the 0 period. 
N = int(10/alpha) + 1
# før: T = np.array([i*alpha for i in range(0,21)])
T = np.array([i*alpha for i in range(N)])
C = np.zeros(N, dtype=float)
print(T, T.shape)
for i in range(1,N):
    C[i] = alpha*R*K
C[-1] += K

#Problem 1
print(pv(0.08,T,C))

print(ytm_obj(0.07, pv_original,T,C))

y_init = 0,07
args = (pv_original,T,C)
results = minimize(ytm_obj,y_init,args = args, method = "nelder-mead")
print(results)
