# ModelNet10-dataset
Compressed really aesthetic handling of the humongous ModelNet10 3D Vision dataset

This contains the numpy array file of the huge ModelNet10 dataset.

Original dataset size ~ 2.2 Gigabytes

Numpy file size ~ 8 Gigabytes

Compressed file size ~ 32 Megabytes

This can all be seen due to the very bad handling of binvox files, and on the top of that numpy arrays.

Please star this repo if you find this useful :grin:

## Usage example -

```python
import gzip
import numpy as np
with gzip.open('modelnet10.npy.gz','rb') as f:
    arr=np.load(f)
    print(type(arr),arr.shape)
```
Output -
```python
<class 'numpy.ndarray'> (3992, 1, 64, 64, 64)
```
Let's check is it works -
```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(arr[78][0],facecolors='red')
plt.show()
```
Output -

![image](/assets/chair.png)
