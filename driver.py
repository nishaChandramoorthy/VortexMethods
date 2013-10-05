
"""
    Driver module.
"""
import math
import numpy as np
from numpy.linalg import solve
from P import P_alph
from rhs import pop_b
alpha = 3.e-01
#X1 is X in the first iteration.
k = 0.2967
W = 0.7402
t = 0.e0 
delt = 0.008
X1 = np.array([ k, W, 0.2997, \
     -0.0020, -0.0188, 0.0022, 0.0007,  -0.0002,  -0.000,  0.000,  0.000,  -0.00, \
     0.0,  0.0,  -0.,  0.0,  0.,  -0.])
#Number of fourier coefficients + 2 

N = np.size(X1)     
M = 10
A = np.zeros((N,N))
b = np.zeros(N)

st_time = 0
en_time = math.pi
dt = (en_time-st_time)/(N-1)

#Populating LHS and RHS once
print "populating N*N matrix..."
for j in range(0,N):
    print "************ t = ", j , "******************"
    tj = t + j*dt
    #Tweak X for P's sake
    X = np.copy(X1)
    X = np.insert(X1,[2,2],[alpha,tj])
    P_2 = P_alph(X)
    for i in range(0,N):
        print "j : ", i
        X = np.copy(X1)
        X[i] = X[i] + delt
        X = np.insert(X,[2,2],[alpha,tj])
        P_1 = P_alph(X)
        Pxj = (P_1-P_2)/delt
        A[j][i] = Pxj
    
    b[j] = -P_2 
    
b = np.transpose(b)
print "Solving to get better approximations..."
for i in range(0,M):
    print "n = ", i
    d = solve(A,b)
    X1 = X1 + np.transpose(d)
    X2 = np.insert(X1, [2,2], [alpha,t])
    b = pop_b(X2)
    

    