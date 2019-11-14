#enconding:utf-8
'''
    @Author:	b0ring
    @MySite:	https://unnamebao.github.io/
    @Date:		2019-11-13 21:16:15
    @Version:	1.0.0
'''

import random

with open("data.txt","a") as f:
    for i in range(20000):
        a = int(random.random()*1000)/100
        b = int(random.random()*1000)/100
        lambda_ = 0.0001 
        y = 3 + 4*a + 5*b + lambda_*random.randint(0,1000)
        y = int(y*100)/100
        f.write(str(a)+"\t"+str(b)+"\t"+str(y)+'\n')

        