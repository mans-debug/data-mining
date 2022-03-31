import numpy as np


def pagerank(M, num_iterations: int = 20, d: float = 0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v
#

# M = np.array([[0    , 1 / 2, 1,     0],
#               [1 / 3, 0, 0, 1 / 2],
#               [1 / 3, 0, 0, 1 / 2],
#               [1 / 3, 1 / 2, 0, 0]])
# for x in M:
#     for y in x:
#         print(y, end=" ")
#     print()