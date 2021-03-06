"""
    Calculates G(r, r^, z-z^)
    
"""
import scipy.special as scsp
import math
import numpy as np
def G_int(x,t_cap,f,t):
    g = G(x,t_cap,f,t)
    return x*g
def G(x, t_cap, f, t):
    r = 1. + f*math.cos(t)
    rcap = 1 + x*math.cos(t_cap)
    zmzcap = f*math.sin(t) - x*math.sin(t_cap)
    k = 4*r*rcap/((r+rcap)**2 + zmzcap**2)
    term1 = np.sqrt((r+rcap)**2 + zmzcap**2)
    term1 = term1*rcap
    term2 = (1.e0 - (k)*0.5e0)*scsp.ellipk(k)
    term2 = term2 - scsp.ellipe(k)
    return term1*term2
    
