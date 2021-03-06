import numpy as np
import numpy.linalg as la

def gsBasis(A) :
    B = np.array(A, dtype=np.float_)
    for i in range(B.shape[1]) :
        for j in range(i) :
            B[:, i] -= B[:, i] @ B[:, j] * B[:, j]
        if la.norm(B[:, i]) > 1e-14:
            B[:, i] = B[:, i] / la.norm(B[:, i])
        else :
            B[:, i] = np.zeros_like(B[:, i])
    return B

def dimensions(A) :
    return np.sum(la.norm(gsBasis(A), axis=0))
