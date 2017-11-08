#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2274503
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 7
import my_functions
import numpy as np
import taylor_approx
import nose
import math

#Testing f(x)=sin(x) at x[50] and x[40] with up to 5 order approximations
def test_taylor_0():
    """test_taylor_0()
    Tests for the accuracy of the Taylor formula approximation at point x[50] by calling sin(x) and taylor; zero order derivative approximation
    """
    a=-5
    b=5
    numberOfPoints=101
    x=np.linspace(a,b,numberOfPoints)
    f=my_functions.sin(x)
    i=50
    out_X,out_fapprox=taylor_approx.taylor(x,f,i-10,n=0) #approximating x[50] at x[40], described as i-10
    desired = -.841
    np.testing.assert_almost_equal(out_fapprox[i],desired,1)

def test_taylor_1():
    """test_taylor_1()
    Tests for the accuracy of the Taylor formula approximation at point x[50] by calling sin(x) and taylor; first order derivative approximation
    """
    a=-5
    b=5
    numberOfPoints=101
    x=np.linspace(a,b,numberOfPoints)
    f=my_functions.sin(x)
    i=50
    out_X,out_fapprox=taylor_approx.taylor(x,f,i-10,n=1) #approximating x[50] at x[40], described as i-10
    desired = -.301
    np.testing.assert_almost_equal(out_fapprox[i],desired,1)

def test_taylor_2():
    """test_taylor_2()
    Tests for the accuracy of the Taylor formula approximation at point x[50] by calling sin(x) and taylor; second order derivative approximation
    """
    a=-5
    b=5
    numberOfPoints=101
    x=np.linspace(a,b,numberOfPoints)
    f=my_functions.sin(x)
    i=50
    out_X,out_fapprox=taylor_approx.taylor(x,f,i-10,n=2) #approximating x[50] at x[40], described as i-10
    desired = .12
    np.testing.assert_almost_equal(out_fapprox[i],desired,1)

def test_taylor_3():
    """test_taylor_3()
    Tests for the accuracy of the Taylor formula approximation at point x[50] by calling sin(x) and taylor; third order derivative approximation
    """
    a=-5
    b=5
    numberOfPoints=101
    x=np.linspace(a,b,numberOfPoints)
    f=my_functions.sin(x)
    i=50
    out_X,out_fapprox=taylor_approx.taylor(x,f,i-10,n=3) #approximating x[50] at x[40], described as i-10
    desired = .03
    np.testing.assert_almost_equal(out_fapprox[i],desired,1)

def test_taylor_4():
    """test_taylor_4()
    Tests for the accuracy of the Taylor formula approximation at point x[50] by calling sin(x) and taylor; fourth order derivative approximation
    """
    a=-5
    b=5
    numberOfPoints=101
    x=np.linspace(a,b,numberOfPoints)
    f=my_functions.sin(x)
    i=50
    out_X,out_fapprox=taylor_approx.taylor(x,f,i-10,n=4) #approximating x[50] at x[40], described as i-10
    desired = -0.005
    np.testing.assert_almost_equal(out_fapprox[i],desired,1)

def test_taylor_5():
    """test_taylor_5()
    Tests for the accuracy of the Taylor formula approximation at point x[50] by calling sin(x) and taylor; fifth order derivative approximation
    """
    a=-5
    b=5
    numberOfPoints=101
    x=np.linspace(a,b,numberOfPoints)
    f=my_functions.sin(x)
    i=50
    out_X,out_fapprox=taylor_approx.taylor(x,f,i-10,n=5) #approximating x[50] at x[40], described as i-10
    desired = -0.0005
    np.testing.assert_almost_equal(out_fapprox[i],desired,1)