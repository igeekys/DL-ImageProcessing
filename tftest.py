# import tensorflow as tf
# import keras
# print(tf.__version__,tf.test.is_gpu_available())


import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
import numpy as np
import time
# 产生用于计算测试的数据
value = np.random.randn(5000,1000)
a = tf.constant(value)
# 计算方式
# gpu
tic = time.time()
for i in range(30000): #进行10000次运算
    tf.multiply(a,a)
toc = time.time()
t_cost = toc - tic
print('耗时:',t_cost)