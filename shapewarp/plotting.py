# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 13:57:26 2014

@author: schackv
"""

import matplotlib.pyplot as plt
        
def plot_shape(P,clr,**plotargs):
    """Plot the shape with coordinates in the numpy array P 
    as [x1,x2,x3,..,xp,y1,y2,...,yp].
    Keyword arguments are passed directly to plot command.
    """

    if P.ndim == 2:
        P = P.T.flatten()

    N = len(P)
    k = int(N/2)
    
    x = P[:k]
    y = P[k:]
    for i in range(k):
        if i<(k-1):
            plt.plot((x[i],x[i+1]),(y[i],y[i+1]),'-',color=clr,**plotargs) #,'color',clr,*plotargs)
        else:
            plt.plot((x[i],x[0]),(y[i],y[0]),'-',color=clr,**plotargs) #,'color',clr,*plotargs)


def plot_mode(mu,pc, nstd):
    """Plot the mean shape +/- nstd times the principal component
    """
    plot_shape(mu,'k',linewidth=2.0)
    plot_shape(mu + nstd*pc,'b')
    plot_shape(mu - nstd*pc,'b')
    
    