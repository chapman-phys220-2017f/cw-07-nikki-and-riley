#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2274503
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 7
import array_calculus
import numpy as np
import math

#Taylor Theorem Code
def taylor(x, f, i, n):
    '''taylor(x,f,i,n=10)
    Takes the taylor series approximation around a specific point at position i.
    Args:
        x (array) : x-coordinates
        f (array) : y-coordinates
        i (index int) : position of point between 0 and the domain
        n (int) : number of terms to keep in Taylor expansion sum
    Returns:
        (x, fapprox) : Pair of numpy arrays
            x  : x-coordinates domain
            fapprox  : new approximate function y-coordinates obtained by Taylor formula at x[i]
'''
    fapprox = np.zeros(len(x))
    for xValue in range(0,len(x)):
        answer = 0
        for term in range(0,n+1):
            D = array_calculus.derivative(x[0],x[len(x)-1],len(x))
            D_operator=np.linalg.matrix_power(D,term)
            myDerivative=D_operator@f
            answer = answer+(myDerivative[i]*(((x[xValue]-x[i])**term)/math.factorial(term)))
        fapprox[xValue] = answer
    return (x,fapprox)