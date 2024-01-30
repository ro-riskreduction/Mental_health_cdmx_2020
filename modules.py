import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def central(x):
    x0     = np.mean( x )
    x1     = np.median( x )
    result = stats.mode( x ) # mode(s) and count(s)
    x2     = result.mode
    print("    Mean        = %.1f" %x0)
    print("    Median      = %.1f" %x1)
    print("    Mode        = %.1f" %x2)
    return x0, x1, x2


def dispersion(n):
    y0 = np.min( n )  # minimum
    y1 = np.max( n )  # maximum
    y2 = y1 - y0      # range
    y3 = np.percentile( n, 25 ) # 25th percentile (i.e., lower quartile)
    y4 = np.percentile( n, 75 ) # 75th percentile (i.e., upper quartile)
    y5 = y4 - y3 # inter-quartile range
    y6 = np.var( n ) # variance
    y7 = np.std( n ) # standard deviation

    print("    Minimum              = %.1f" %y0)
    print("    Maximum              = %.1f" %y1)
    print("    Range                = %.1f" %y2)
    print("    25th percentile      = %.1f" %y3)
    print("    75th percentile      = %.1f" %y4)
    print("    Inter-quartile range = %.1f" %y5)
    print("    Variance             = %.1f" %y6)
    print("    Standard deviation   = %.1f" %y7)

def skewkurto(x):
    n = 3
    z0 = stats.skew(x)
    z1 = stats.kurtosis(x)
    z0 = np.around(z0, n)
    z1 = np.around(z1, n)

    print("    Skewness     = ", z0)
    print("    Kurtosis     = ", z1)
    
def onettest(x, mu):
    j1 = stats.ttest_1samp(x, mu)
    
    print("This is the value of the One-sample t test =" , j1)

def twottest(x,y):
    x, y   = stats.ttest_ind(x, y)
    n = 3
    x = np.around( x, n )
    y = np.around( y, n )
    print("This is the value of the Two-sample t test =", x )
    print("This is the value of p for Two-sample t test =", y )
    
def anova(x,y):
    a = stats.f_oneway(x, y)
    a = np.around(a, 3)
    print("One way anova:", a)
    
def corr(x,y):
    co = np.corrcoef(x,y)[0,1]
    n = 3
    co = np.around(co, n)
    print("Correlation coeficient:", co)
    
def lr(x,y):
    results = stats.linregress(x,y)
    print(results)
    

def check_for_nan(x):
    x.isnull().values.any()
    print("check_for_nan", x)
    
    
def len_compare(x,y):
    o = len(x)
    o1 = len(y)
    b = ((o1 * 100)/o)-100
    b = np.around(b,3)
    print(o,o1,b)

def compare_mean_max(x,y):
    b = ((y * 100)/x)-100
    b = np.around(b,3)
    print(b)
    
def pre_post_ttest(x,y):
    t,p    = stats.ttest_rel(x, y)
    t = np.around(t,3)
    p = np.around(p, 3)
    print(t)
    print(p)