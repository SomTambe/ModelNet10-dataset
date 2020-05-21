import binvox_rw
import numpy as np
import os

entries = os.listdir('./monitor_binvox')
train_voxels=np.zeros((1,32,32,32))
i=0
for entry in entries:
    print('i=',i,' ./monitor_binvox/'+entry)
    i+=1
    f=open('./monitor_binvox/'+entry,'rb')
    model=binvox_rw.read_as_3d_array(f)
    dat=np.expand_dims(model.data,axis=0)
    # print(dat.shape)
    train_voxels=np.concatenate((train_voxels,dat),axis=0)
    del dat
    del model
    del f
train_voxels=np.expand_dims(train_voxels,axis=1) # outputs a 5-vector (N,C,H,W,D), as in the official Pytorch documentation
np.save('monitor.npy',train_voxels)
