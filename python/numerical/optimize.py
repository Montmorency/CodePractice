import numpy as np
from scipy.optimize import minimize

def f_xy(x,a,b):
  return (x[0]-a)**2+(x[1]-b)**2

args = (-4,2)
print 'Minimum', args
res = minimize(f_xy,np.array([0,3]),args,method='nelder-mead')
print 'Found Minimum', res.x
print 'Rounded Minimum', tuple(map(lambda x: int(round(x)), res.x))
