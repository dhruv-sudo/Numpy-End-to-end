#This explains about how to identify the type of the array used.

import numpy as np

arr_1=np.array([1,2,3])
arr_2=np.array([[1,2,3],
                [4,5,6]])


print("This shows that the given arr_2 is a",arr_2.ndim,"array.")
