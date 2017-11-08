#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2267883
# Email: schwa218@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 6

import numpy as np
import matplotlib.pyplot as plt #Used to plot in python

#First Derivative code
def derivative(a,b,n):
    '''derivative(a,b,n)
    Creating the first-order derivative matrix operator
    Args:
        a (int) : first endpoint
        b (int) : last endpoing
        n (int) : number of intervals from a to b
    Returns:
        D1 : The first derivative matrix operator'''
    dx = (b-a)/(n-1)
    D1 = np.eye(n,n,1)-np.eye(n,n,-1)
    D1[0][0] = -2
    D1[0][1] = 2
    D1[-1][-1] = 2
    D1[-1][-2] = -2
    D1 = D1/(2*dx)
    return D1

#Second Derivative Code
def second_derivative(a,b,n):
    '''derivative(a,b,n)
    Creating the second-order derivative matrix operator
    Args:
        a (int) : first endpoint
        b (int) : last endpoing
        n (int) : number of intervals from a to b
    Returns:
        D2 : The second derivative matrix operator'''
    dx = ((b-a)/(n-1))
    D2 = np.eye(n,n,2)+np.eye(n,n,-2)-2*np.eye(n)
    D2[0][0] = 2
    D2[0][1] = -4
    D2[0][2] = 2
    D2[1][0] = 2
    D2[1][1] = -3
    D2[-1][-1] = 2
    D2[-1][-2] = -4
    D2[-1][-3] = 2
    D2[-2][-1] = 2
    D2[-2][-2] = -3
    D2 = (D2/(4*dx**2))
    return D2

#Plotting xSquared(f):
def make_plots_for_xSquared(x, functionResults, myDerivative, mySecondDerivative):
    #plots the normal function, derivative function, and second derivative function of x^2.
    plt.ylabel('Y') #labels the y axis
    plt.xlabel('X') #labels the x axis
    font = {'size': 16} #adjusts size of font
    title="Normal, First Derivative, and Second Derivative of x^2" #title of graph
    plt.title(title)
    plt.plot(x,functionResults,label="Function Results",color="green")
    plt.plot(x,myDerivative,label="First Derivative Results",color="blue")
    plt.plot(x,mySecondDerivative,label="Second Derivative Results", color="red")
    plt.legend(loc='upper left', frameon=False) #graph's legend
    plt.show()

#Plotting sinX(f)
def make_plots_for_sinX(x, functionResults, myDerivative, mySecondDerivative):
    #plots the normal function, derivative function, and second derivative function of sin(x).
    plt.ylabel('Y') #labels the y axis
    plt.xlabel('X') #labels the x axis
    font = {'size': 16} #adjusts size of font
    title="Normal, First Derivative, and Second Derivative of sin(x)" #title of graph
    plt.title(title)
    plt.plot(x,functionResults,label="Function Results",color="green")
    plt.plot(x,myDerivative,label="First Derivative Results",color="blue")
    plt.plot(x,mySecondDerivative,label="Second Derivative Results", color="red")
    plt.legend(loc='lower right', frameon=False) #graph's legend
    plt.show()

#Plotting expX(f)
def make_plots_for_expX(x, functionResults, myDerivative, mySecondDerivative):
    #plots the normal function, derivative function, and second derivative function of e^((-x^2/2)/(2pi)^(1/2).
    plt.ylabel('Y') #labels the y axis
    plt.xlabel('X') #labels the x axis
    font = {'size': 16} #adjusts size of font
    title="Normal, First Derivative, and Second Derivative of e^((-x^2/2)/(2pi)^(1/2)" #title of graph
    plt.title(title)
    plt.plot(x,functionResults,label="Function Results",color="green")
    plt.plot(x,myDerivative,label="First Derivative Results",color="blue")
    plt.plot(x,mySecondDerivative,label="Second Derivative Results", color="red")
    plt.legend(loc='upper right', frameon=False) #graph's legend
    plt.show()