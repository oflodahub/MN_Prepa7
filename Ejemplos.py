import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import lagrange

'''
# hace una partición regular de n-1 intervalos
xs=np.linspace (0,10,21)

print(type(xs))

for x in xs:
    print(x)
    
    

n = 10
for i in range(0, n, 2):
    print(i)

xx = np.array([0, 1, 10])
print(xx)

# Buena explicacion en https://aprendeconalf.es/docencia/python/manual/numpy/
 
# This is a 1d array:
a = np.array([1,2,3])
print("1d array: ",a)

# This is a 2d array:
b = np.array([[1,2,3],[3,4,5]])
print("2d array:")
print(b)

# This is a 3d array:
c = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[21,22,23],[24,25,26],
[27,28,29],[30,31,32]]])
print("3d array:")
print(c)

# ejemplo en https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter17.04-Lagrange-Polynomial-Interpolation.html
xx = np.array([-2, 0, 2])
yy = np.array([4, 0, 4])
pol = lagrange(xx, yy)

print(pol)

x = np.arange(0, 5, 0.1)
print(x)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

'''




def regla_simpson13 (f,a,b,n):
    h = (b - a) / n
    xs=np.linspace (a,b,n+1)
    #pasa toda la particion como argumento
    ys=f(xs)
    suma = 0
    for j in range(1, int(n/2)+1, 1):
        suma+= (ys[2*j-2] + 4*ys[2*j-1] + ys[2*j])
    suma = (h/3)*suma
    #print(f'suma: {suma}')
    return suma

# funcion a integrar
def f(x):
    # return np.exp(-(x**2))
    return x**2

area = regla_simpson13(f, -2, 2, 2)

print(area)






