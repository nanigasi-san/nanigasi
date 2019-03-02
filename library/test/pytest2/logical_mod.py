import numpy as np
def and_logical_easy(a,b):
    w1,w2,t = 0.5,0.5,0.7
    ans = a*w1+b*w2-t
    if ans > 0:
        return 1
    else:
        return 0

def and_logical(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(x*w)+b
    if tmp>0:
        return 1
    else:
        return 0

def nand_logical(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x*w)+b
    if tmp>0:
        return 1
    else:
        return 0

def or_logical(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.3
    tmp = np.sum(x*w)+b
    if tmp > 0:
        return 1
    else:
        return 0
