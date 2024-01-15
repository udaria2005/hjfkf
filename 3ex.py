import numpy as np
n = int(input())
a = []
for k in range(n**2):
    b = int(input())
    a.append(b)
a = np.array(a)
a = a.reshape(n,n)
c = np.linalg.inv(a)
q = c.dot(c)
v = q.dot(c)
print(v)