#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2274503
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 7
import my_functions
import numpy as np
import taylor_approx
import math
import matplotlib.pyplot as plt

#Codes for each function's 0-5th ordered plots demonstrated in taylor.ipynb
def make_plots(x,i):
    for f,s in ((np.sin(x), "sin(x)"), (np.tanh(x), "tanh(x)"), (my_functions.poly(x), "poly(x)"), (my_functions.denom(x), "denom(x)"), (my_functions.theta(x), "theta(x)")): #ensures all functions are being plotted, including the sin(x) test function.
        for n in range(0,6): #range enables 0-5th order approximations to be plotted
            out_X,out_fapprox=taylor_approx.taylor(x,f,i,n) #plots approximations
            plt.figure(figsize=(3,3))
            plt.ylabel('y') #y-axis label
            plt.xlabel('x') #x-axis label
            font = {'size': 16} #font size
            title= n #enables the title to be each function's name
            plt.title(title)
            plt.plot(out_X,out_fapprox,label=s+"approx",color="green") #green plot demonstrates the ordered approximation
            plt.plot(x,f,label=s,color="blue") #blue plot demonstrates the actual function
            plt.legend(loc='upper left', frameon=False)
            plt.plot(x[500], f[500], 'r*') #marks the specific point which function is being approximated around
            plt.show()

