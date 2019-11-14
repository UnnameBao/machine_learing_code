#enconding:utf-8
'''
    @Author:	b0ring
    @MySite:	https://unnamebao.github.io/
    @Date:		2019-11-13 15:47:04
    @Version:	1.0.0
'''

import numpy as np
import random

class linear():
    def __init__(self):
        self.theta = np.random.randn(3, 1)
        self.eta = 0.0000001

    def train(self,train_data,mini_batch_size,epochs=1000):
        for i in range(epochs):
            random.shuffle(train_data)
            mini_batches = [
                train_data[k:k+mini_batch_size]
                for k in range(0, len(train_data), mini_batch_size)]
            for mini_batche in mini_batches:
                self.update_mini_batch(np.array(mini_batche),self.eta)
    def predict(self,x):
        return np.dot(x,self.theta)

    def update_mini_batch(self,mini_batch,eta):
        y = mini_batch[:,2:]
        new_col = np.array([[1]]*mini_batch.shape[0])
        x = np.c_[new_col,mini_batch[:,:2]]
        y_hat = self.predict(x)
        part_one = y - y_hat
        # print("[*] ",part_one)
        self.theta = self.theta + (1/len(mini_batch))*np.sum((eta*part_one*x).T,axis=1).reshape((-1,1))

 
def correlation(x, y):
    return (((x-x.mean())/(x.std(ddof=0)))*((y-y.mean())/(y.std(ddof=0)))).mean() 


linear_ = linear()
f = open("house.txt","r")
lines = f.readlines()
data = [[float(one) for one in line.strip().split(" ")] for line in lines]
train_data = data[:1000]
test_data = data[1000:]
linear_.train(train_data,100)
input_ = np.array(data)[:,:2]
y = np.array(data)[:,2:]
new_col = np.array([[1]]*input_.shape[0])
input_ = np.c_[new_col,input_]
y_hat = linear_.predict(input_)
print(np.corrcoef(y_hat.T, y.T))
