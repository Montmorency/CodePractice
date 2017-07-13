#For some reason interview prep are always asking you to 
#to find the square root of a number using Newton's method.

N = 10
C = 20.0

def f(x):
  return x*x - C
    
def fprime(x):
  return 2.0*x

def newton(x_n):
#y = f'(x_n)(x-x_{n}) + f(x_{n})
#0 = f'(x_n)(x_(n+1)-x_{n}) + f(x_{n})
#x_{n+1}= x_{n} - f(x_{n})/f'(x_{n})
  return x_n - f(x_n)/fprime(x_n)

x_n = 1.0
for i in range(N):
  print 'Sqrt:', C
  x_n = newton(x_n)  
  print x_n, f(x_n)
