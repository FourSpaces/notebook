# TensorFlow

一个通过计算图的形式来表述计算的编程系统。TensorFlow中的每一个计算都是计算图上的一个节点，

而节点之间的边描述了计算之间的依赖关系。

### 计算图 (tf.Graph) , 计算模型

计算图是 TensorFlow 中的最基本的一个概念， TensorFlow 中的所有计算都会被转化为计算图上的节点

### 张量 (tf.Tensor) , 数据模型

简单的理解为多维数组，但实现并不是直接采用数组的形式。 表现了TensorFlow 的数据结构。

零阶张量表示标量(scalar), 也就是一个数。

第一阶张量为向量(vector), 也就是一维数组。

第n阶张量可以理解为一个n阶数组。

在张量中并没有真正保存数字，只保存了如何得到这些数字的计算过程。

- 张量的结构：
  - 名字(name)：是张量的唯一标识，张量名和计算图上节点
  - 维度(shape)：描述了一个张量的维度信息
  - 类型(type)：每个张量都会有一个唯一的类型。
- 张量的使用：
  - 对中间结果的引用，在包含多中间结果时，可提高代码的可读性。
  - 当计算图构造完成后，张量可以用来获得计算结果，使用会话 (session), 运算后得到具体的数字。



### 会话 (tf.Session) , 运算模型 

session 用来执行定义好的运算。拥有并管理TensorFlow程序运行时的所有资源，计算完成后需要关闭会话来帮助系统回收资源。



### Flow  流

表达了张量之间通过计算相互转化的构成，体现了TensorFlow 的计算模型

### 深度学习

通过增加神经元的个数和神经网络的隐藏层数，即使没有输入许多特征，神经 网络也能正确地分类

### 设计理念

TensorFlow 的设计理念主要体现在以下两个方面。

（1）将图的定义和图的运行完全分开。因此，TensorFlow 被认为是一个“符号主义”的库。

（2）TensorFlow 中涉及的运算都要放在图中，而图的运行只发生在会话(session)中。开 启会话后，就可以用数据去填充节点，进行运算;关闭会话后，就不能进行计算了。

### 符号式计算

符号式计算一般是先定义各种变量，然后建立一个数据流图，在数据流图中规定各个变量之间 的计算关系，最后需要对数据流图进行编译，但此时的数据流图还是一个空壳儿，里面没有任何实 际数据，只有把需要运算的输入放进去后，才能在整个模型中形成数据流，从而形成输出值。

### 编程模型

数据流图(也称为网络结构图)

它的计算过程是，首先从输入开始，经过塑形后，一层一层进行前向传播运算。Relu 层(隐 藏层)里会有两个参数，即Wh1和bh1，在输出前使用ReLu(Rectified Linear Units)激活函数 做非线性处理。

然后进入 Logit 层(输出层)，学习两个参数 Wsm 和 bsm。用 Softmax 来计算输出结果中各个类别的概率分布。

用交叉熵来度量两个概率分布(源样本的概率分布和输出结果 的概率分布)之间的相似性。然后开始计算梯度，这里是需要参数 Wh1、bh1、Wsm 和 bsm，以及 交叉熵后的结果。随后进入 SGD 训练，也就是反向传播的过程，从上往下计算每一层的参数， 依次进行更新。也就是说，计算和更新的顺序为 bsm、Wsm、bh1 和 Wh1。

### 边

TensorFlow 的边有两种连接关系: 数据依赖 和 控制依赖1

实线边表示数据依赖， 代表数据，即张量。

虚线边，称为控制依赖(control dependency)，可以用于控制操 作的运行

### 节点

节点又称为算子，代表一个操作(operation，OP)，一般用来表示施加的数学运 算

边和节点，TensorFlow 还涉及其他一些概念，如图、会话、设备、变量、内核等





# 神经网络

> 使用神经网络解决分类问题

1、提取问题中实体的特征向量作为神经网络的输入。不同的实体可以提取不同的特征向量

2、定义神经网络的结构，并定义如何从神经网络的输入得到输出。这个过程就是神经网络的前向传播算法。

3、通过训练数据来调整神经网络中参数的取值，这就是训练神经网络的过程。

4、使用训练好的神经网络来预测未知的数据。



>  训练神经网络的过程：

设置神经网络参数的过程就是神经网络的训练过程。

1、定义神经网络的结构和前向传播的输出结果。

2、定义损失函数以及选择反向传播优化的算法。

3、生成会话（tf.Session）并且在训练数据上反复运行反向传播优化算法。



> 监督学习

监督学习最重要的思想就是，在已知答案的标注数据集上，模型给出的预测结果要尽量接近真实的答案。通过调整神经网络中的参数对训练数据进行拟合，可以使得模型对未知的样本提供预测的能力。



> 神经网络前向传播算法





> 神经网络优化算法

- 反向传播算法( backpropagation )

  

![image-20180502163702844](/var/folders/zq/rjnjk4l905q7z92xqvh1g55w0000gn/T/abnerworks.Typora/image-20180502163702844.png)

反向传播算法实现了一个迭代的过程，每次迭代的开始，首先选一小部分训练数据，这一部分数据叫做一个batch.  这个batch 的样例会通过前向传播算法得到神经网络模型的预测结果。基于这预测值和真实值之间的差距，反向传播算法会想应更新神经网络参数的取值，使得在这个batch上神经网络模型的预测结果和真实的答案更加接近。



placeholder 机制用于提供输入数据，占位符



cross_entropy 定义了真实值和预测值之间的交叉墒，分类问题中常用的损失函数。



> TensorFlow 常用的优化方法

tf.train.GradientDescentOptimizer

tf.train.AdamOptimizer

tf.train.MomentumOptimizer



> 训练神经网络基于TensorFlow 的代码实现

```python
# -*- coding:utf-8 -*-
## 神经网络解决二分类问题

import tensorflow as tf
from numpy.random import RandomState

# 定义训练数据 batch 的大小
batch_size = 8

# 定义神经网络的参数，
w0 = tf.Variable(tf.random_normal([3, 3], stddev=1, seed=1))
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
# w1 = tf.Variable([[-0.8113182, 1.4845988, 0.06532937], [-2.4427042, 0.0992484, 0.5912243]])
# w2 = tf.Variable([[-0.8113182], [1.4845988], [0.06532937]])

# 在shape 的一个维度上使用None可以方便使用不大的batch大小。
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

# 定义神经网络前向传播过程
# a = tf.matmul(x, w1)
# b = tf.matmul(a, w0)
# y = tf.matmul(b, w2)

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播的算法
## 获取真实值与预测值之间的交叉墒
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
)
## 定义反向传播的优化方法
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)

# 定义规则来给出样本标签，在这里所有 x1+x2<1 的样例被认为是正样本，其他为负样本
# 用 0 表示 负样本， 用 1 表述正样本
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# 创建一个会话来运行TensorFlow 程序
with tf.Session() as sess:
    # 初始化变量
    init_op = tf.initialize_all_variables()
    sess.run(init_op)

    # 训练前输出神经网络参数的值
    print(sess.run(w1))
    print(sess.run(w2))

    # 设置训练轮数
    STEPS = 6000
    for i in range(STEPS):
        # 每次选择 batch_size 个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end],
                                        y_: Y[start:end]})

        if i % 1000 == 0:
            # 每隔一段时间计算在所有数据上的交叉墒并输出
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict={x: X, y_: Y}
            )
            print('After %d training step(s), cross entropy on all data is %g' %
                  (i, total_cross_entropy)
                  )

    print(sess.run(w1))
    print(sess.run(w2))
```











# 深度学习与深层神经网络

深度学习：一类通过多层非线性变换对高复杂性数据建模算法的合集

深度学习的特性：多层和非线性



## 线性模型的局限性

线性模型只能够解决线性问题。



## 激活函数实现去线性化

将每个神经元的输出通过一个非线性函数，那么整个神经网络的模型就不再是线性的了。这个非线性函数就是激活函数。

- 增加了一个偏置项(bias)
- 每个节点的取值不再是单纯的加权和，在加权和的基础上做了一个非线性变换

$$
A_1 = \begin{bmatrix} a_11 , a_12, a_13 \end{bmatrix} = f(xW^{(1)} + b)=f(\begin{bmatrix} x_1, x_2 \end{bmatrix}  \begin{bmatrix}W_{1,1}^{(1)}  & W_{1,2}^{(1)} & W_{1,3}^{(1)} \\ W_{2,1}^{(1)}  & W_{2,2}^{(1)} & W_{2,3}^{(1)} \end{bmatrix} +  \begin{bmatrix} b_1 & b_2 & b_3 \end{bmatrix})
$$

$$
= f(\begin{bmatrix} W_{1,1}^{(1)}x_1 +  W_{2,1}^{(1)}x_2 + b_1,   W_{1,2}^{(1)}x_1 +  W_{2,2}^{(1)}x_2 + b_2, W_{1,3}^{(1)}x_1 +  W_{2,3}^{(1)}x_2 + b_3\end{bmatrix})
$$

$$
= \begin{bmatrix} f(W_{1,1}^{(1)}x_1 +  W_{2,1}^{(1)}x_2 + b_1),   f(W_{1,2}^{(1)}x_1 +  W_{2,2}^{(1)}x_2 + b_2), f(W_{1,3}^{(1)}x_1 +  W_{2,3}^{(1)}x_2 + b_3)\end{bmatrix}
$$



## 损失函数定义

神经网络模型的效果以及优化的目标是通过损失函数(loss function) 来定义的。

通过神经网络解决多分类问题最常用的方法是设置 n 个输出节点，其中 n 为类别的个数。可以得到一个n 维数组作为输出结果。

> 判断一个输出向量和期望的向量接近程度。

- 交叉熵 ( cross entropy) : 刻画了两个概率分布之间的距离，是分类问题中使用较广的一种损失函数。

  - 解释

  给定两个概率分布 *p*  和 *q*, 通过 *q* 来表示 *p*  的交叉熵：
  $$
  H(p, q) = - \sum_{x}p(x) \log  q(x)
  $$
   交叉熵刻画的是两个概率分布之间的距离，概率分布刻画了不同事件发生的概率，当事件的总数是有限的情况下，概率分布函数 *P*(X = x) 满足：

  - Softmax 回归

  将神经网络的前向传播得到的结果变成概率分布。





```
tf.clio_by_value(y, 1e-10, 10)
```

