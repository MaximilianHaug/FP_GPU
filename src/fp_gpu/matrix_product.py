import numpy as np
#from typing import List

def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    if not matrices:
        raise ValueError("The list of matrices cannot be empty.")
    
    result = matrices[0]
    for mat in matrices[1:]:
        result = result @ mat
    return result

product = matrix_product([np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])])
print(product)