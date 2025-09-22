import numpy as np

data=np.array([10,20,30,40,50])

print("first 3 elements:", data[:3])
print("reversed:", data[::-1])
print("sum:", np.sum(data))
print("standard deviation:", np.std(data))