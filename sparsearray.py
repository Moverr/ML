import numpy as np 
from  scipy import sparse 

 
dataset = [[1,2,3],[3,4,5],[6,7,8],[11,12,34]]
#convert dataset to numpy aarrya ndArray 
ndArray = np.array(dataset)


eye = np.eye(23)
sparse = sparse.csr_matrix(dataset)

print("Sci Array X:\n{}".format(dataset))
print("Sci Array X:\n{}".format(sparse))
