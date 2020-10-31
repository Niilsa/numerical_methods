import numpy as np


def solve(A, f):
    n = A.shape[0]
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    for i in range(n):
        b[i] = -A[i][i]
        if (i > 0):
            a[i] = A[i][i - 1]
        if (i < n - 1):
            c[i] = A[i][i + 1]
    p = np.zeros(n)
    q = np.zeros(n)
    p[0] = c[0]/b[0]
    q[0] = -f[0]/b[0]
    for i in range(1, n):
        p[i] = c[i]/(b[i] - a[i] * p[i - 1])
        q[i] = (a[i] * q[i - 1] - f[i])/(b[i] - a[i] * p[i - 1])
    x = np.zeros(n)
    x[-1] = (a[-1] * q[-2] - f[-1])/(b[-1] - a[-1] * p[-2])
    for i in range(n - 2, -1, -1):
        x[i] = p[i] * x[i + 1] + q[i]
    return x

def main():
    A = np.array([[5, 3, 0, 0],
                  [3, 6, 1, 0],
                  [0, 1, 4, -2],
                  [0, 0, 1, -3]])
    f = np.array([8, 10, 3, -2])
    print(A @ solve(A, f))
    

main()
