#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2274503
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 7
import array_calculus
import numpy as np

#sin(x) function
def sin(x):
    '''sin(x)
    Takes the x-coordinate domain and determines corresponding y-coordinates
    Args:
        x (array) : x-coordinates
    Returns:
        out2 (array) : y-coordinates, described as "f" in taylor_approx file
'''
    out1 = list()
    yValues = ()
    for k in range(0,len(x)):
        yValues = np.sin(x[k])
        out1.insert(k,yValues)
    out2 = np.array(out1)
    return out2

#cos(x) function
def cos(x):
    '''cos(x)
    Takes the x-coordinate domain and determines corresponding y-coordinates
    Args:
        x (array) : x-coordinates
    Returns:
        out2 (array) : y-coordinates, described as "f" in taylor_approx file
'''
    out1 = list()
    yValues = ()
    for k in range(0,len(x)):
        yValues = np.cos(x[k])
        out1.insert(k,yValues)
    out2 = np.array(out1)
    return out2

#tanh(x) function
def tanh(x):
    '''tanh(x)
    Takes the x-coordinate domain and determines corresponding y-coordinates
    Args:
        x (array) : x-coordinates
    Returns:
        out2 (array) : y-coordinates, described as "f" in taylor_approx file
'''
    out1 = list()
    yValues = ()
    for k in range(0,len(x)):
        yValues = np.tanh(x[k])
        out1.insert(k,yValues)
    out2 = np.array(out1)
    return out2

#poly(x) function
def poly(x):
    '''poly(x)
    Takes the x-coordinate domain and determines corresponding y-coordinates
    Args:
        x (array) : x-coordinates
    Returns:
        out2 (array) : y-coordinates, described as "f" in taylor_approx file
'''
    out1 = list()
    yValues = ()
    for k in range(0,len(x)):
        yValues = ((x[k]**2)/10)+(np.sin(2*x[k]))/2
        #np.tanh(x[k])
        out1.insert(k,yValues)
    out2 = np.array(out1)
    return out2

#denom(x) function
def denom(x):
    '''denom(x)
    Takes the x-coordinate domain and determines corresponding y-coordinates
    Args:
        x (array) : x-coordinates
    Returns:
        out2 (array) : y-coordinates, described as "f" in taylor_approx file
'''
    out1 = list()
    yValues = ()
    for k in range(0,len(x)):
        if x[k] == 0:
            yValues = np.nan
        else:
            yValues = 1/(x[k])
        out1.insert(k,yValues)
    out2 = np.array(out1)
    return out2

#theta(x) function
def theta(x):
    '''theta(x)
    Takes the x-coordinate domain and determines corresponding y-coordinates
    Args:
        x (array) : x-coordinates
    Returns:
        out2 (array) : y-coordinates, described as "f" in taylor_approx file
'''
    out1 = list()
    yValues = ()
    for k in range(0,len(x)):
        yValues = (x[k])
        if (x[k]) < 0:
            yValues = 0
        if (x[k]) == 0:
            yValues = (1/2)
        if (x[k]) > 0:
            yValues = 1
        out1.insert(k,yValues)
    out2 = np.array(out1)
    return out2
