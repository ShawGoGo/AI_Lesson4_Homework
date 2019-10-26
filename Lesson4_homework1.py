# 随机打乱数据集
import random

def shuffle_xy(x, y):
    index = [i for i in range(len(x))]
    random.shuffle(index)
    rand_x = [x[i] for i in index]
    rand_y = [y[i] for i in index]
    for i, j in zip(rand_x,rand_y):
        print(i, ':', j)


x = ['快递太慢了！', '不好吃', '特别难吃', '要齁死我了', '很划算', '下次还来', '味道很不错！', '香']
y = ['差评', '差评', '差评', '差评', '好评', '好评', '好评', '好评']
shuffle_xy(x, y)