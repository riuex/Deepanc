import os
import numpy as np
import matplotlib.pyplot as plt
from chainer.datasets import mnist


train_val,test = mnist.get_mnist(withlabel=True,ndim=1)

#You can use this function for sepalating source dataset to each number of datas in random.
#split_dataset_random(data,number of data of training,randomseed)
from chainer.datasets import split_dataset_random
train,valid = split_dataset_random(train_val,5000,seed=0)

#Iterator is most important function to return minibatch
from chainer import iterators
batchsize = 12
train_iter = iterators.SerialIterator(train,batchsize)
valid_iter = iterators.SerialIterator(valid,batchsize,repeat=False,shuffle=False)
test_iter = iterators.SerialIterator(test,batchsize,repeat=False,shuffle=False)

minibatch = train_iter.next()

#if you want to create more over images. you can create this pathway
