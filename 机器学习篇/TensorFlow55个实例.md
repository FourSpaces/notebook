# 干货 | TensorFlow的55个经典案例

[![BigQuant](https://pic2.zhimg.com/v2-cad751296cc3efc068695708fcbf380a_xs.jpg)](https://www.zhihu.com/people/bigquant)

[BigQuant](https://www.zhihu.com/people/bigquant)

人工智能助力宽客玩转量化投资，高效开发AI量化策略。微信公众号:BigQuant

1,043 人赞了该文章

> **导语:** 本文是TensorFlow实现流行机器学习算法的教程汇集，目标是让读者可以轻松通过清晰简明的案例深入了解 TensorFlow。这些案例适合那些想要实现一些 TensorFlow 案例的初学者。本教程包含还包含笔记和带有注解的代码。

## 第一步：给TF新手的教程指南

### 1：tf初学者需要明白的入门准备

- 机器学习入门笔记：

aymericdamien/TensorFlow-Examples

- MNIST 数据集入门笔记

aymericdamien/TensorFlow-Examples

### 2：tf初学者需要了解的入门基础

- Hello World

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/1_Introduction/helloworld.py

- 基本操作

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/1_Introduction/basic_operations.py

### 3：tf初学者需要掌握的基本模型

- 最近邻：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/2_BasicModels/nearest_neighbor.py

- 线性回归：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/2_BasicModels/linear_regression.py

- Logistic 回归：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/2_BasicModels/logistic_regression.py

### 4：tf初学者需要尝试的神经网络

- 多层感知器：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/multilayer_perceptron.py

- 卷积神经网络：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/convolutional_network.py

- 循环神经网络（LSTM）：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/recurrent_network.py

- 双向循环神经网络（LSTM）：

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/bidirectional_rnn.py

- 动态循环神经网络（LSTM）

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/dynamic_rnn.py

- 自编码器

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/autoencoder.py

### 5：tf初学者需要精通的实用技术

- 保存和恢复模型

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/4_Utils/save_restore_model.py

- 图和损失可视化

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/4_Utils/tensorboard_basic.py

- Tensorboard——高级可视化

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/4_Utils/tensorboard_advanced.py

### 6：tf初学者需要的懂得的多GPU基本操作

- 多 GPU 上的基本操作

aymericdamien/TensorFlow-Examples

https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/5_MultiGPU/multigpu_basics.py

### 7：案例需要的数据集

有一些案例需要 MNIST 数据集进行训练和测试。运行这些案例时，该数据集会被自动下载下来（使用 input_data.py）。

> **MNIST数据集笔记**：[aymericdamien/TensorFlow-Examples](https://link.zhihu.com/?target=https%3A//github.com/aymericdamien/TensorFlow-Examples/blob/master/notebooks/0_Prerequisite/mnist_dataset_intro.ipynb)
>
> **官方网站：** [MNIST handwritten digit database, Yann LeCun, Corinna Cortes and Chris Burges](https://link.zhihu.com/?target=http%3A//yann.lecun.com/exdb/mnist/)

## 第二步：为TF新手准备的各个类型的案例、模型和数据集

**初步了解：TFLearn TensorFlow**

接下来的示例来自TFLearn，这是一个为 TensorFlow 提供了简化的接口的库。里面有很多示例和预构建的运算和层。

### 使用教程：

TFLearn 快速入门。通过一个具体的机器学习任务学习 TFLearn 基础。开发和训练一个深度神经网络分类器。

> TFLearn地址：[tflearn/tflearn](https://link.zhihu.com/?target=https%3A//github.com/tflearn/tflearn)
>
> 示例：[tflearn/tflearn](https://link.zhihu.com/?target=https%3A//github.com/tflearn/tflearn/tree/master/examples)
>
> 预构建的运算和层：[Index - TFLearn](https://link.zhihu.com/?target=http%3A//tflearn.org/doc_index/%23api)
>
> 
>
> 笔记：[tflearn/tflearn](https://link.zhihu.com/?target=https%3A//github.com/tflearn/tflearn/blob/master/tutorials/intro/quickstart.md)

### 基础模型以及数据集

- 线性回归，使用 TFLearn 实现线性回归

https://github.com/tflearn/tflearn/blob/master/examples/basics/linear_regression.py

- 逻辑运算符。使用 TFLearn 实现逻辑运算符

https://github.com/tflearn/tflearn/blob/master/examples/basics/logical.py

- 权重保持。保存和还原一个模型

https://github.com/tflearn/tflearn/blob/master/examples/basics/weights_persistence.py

- 微调。在一个新任务上微调一个预训练的模型

https://github.com/tflearn/tflearn/blob/master/examples/basics/finetuning.py

- 使用 HDF5。使用 HDF5 处理大型数据集

https://github.com/tflearn/tflearn/blob/master/examples/basics/use_hdf5.py

- 使用 DASK。使用 DASK 处理大型数据集

https://github.com/tflearn/tflearn/blob/master/examples/basics/use_dask.py

### 计算机视觉模型及数据集

- 多层感知器。一种用于 MNIST 分类任务的多层感知实现

https://github.com/tflearn/tflearn/blob/master/examples/images/dnn.py

- 卷积网络（MNIST）。用于分类 MNIST 数据集的一种卷积神经网络实现

https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_mnist.py

- 卷积网络（CIFAR-10）。用于分类 CIFAR-10 数据集的一种卷积神经网络实现

https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py

- 网络中的网络。用于分类 CIFAR-10 数据集的 Network in Network 实现

https://github.com/tflearn/tflearn/blob/master/examples/images/network_in_network.py

- Alexnet。将 Alexnet 应用于 Oxford Flowers 17 分类任务

https://github.com/tflearn/tflearn/blob/master/examples/images/alexnet.py

- VGGNet。将 VGGNet 应用于 Oxford Flowers 17 分类任务

https://github.com/tflearn/tflearn/blob/master/examples/images/vgg_network.py

- VGGNet Finetuning (Fast Training)。使用一个预训练的 VGG 网络并将其约束到你自己的数据上，以便实现快速训练

https://github.com/tflearn/tflearn/blob/master/examples/images/vgg_network_finetuning.py

- RNN Pixels。使用 RNN（在像素的序列上）分类图像

https://github.com/tflearn/tflearn/blob/master/examples/images/rnn_pixels.py

- Highway Network。用于分类 MNIST 数据集的 Highway Network 实现

https://github.com/tflearn/tflearn/blob/master/examples/images/highway_dnn.py

- Highway Convolutional Network。用于分类 MNIST 数据集的 Highway Convolutional Network 实现

https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_highway_mnist.py

- Residual Network (MNIST) 。应用于 MNIST 分类任务的一种瓶颈残差网络（bottleneck residual network）

https://github.com/tflearn/tflearn/blob/master/examples/images/residual_network_mnist.py

- Residual Network (CIFAR-10)。应用于 CIFAR-10 分类任务的一种残差网络

https://github.com/tflearn/tflearn/blob/master/examples/images/residual_network_cifar10.py

- Google Inception（v3）。应用于 Oxford Flowers 17 分类任务的谷歌 Inception v3 网络

https://github.com/tflearn/tflearn/blob/master/examples/images/googlenet.py

- 自编码器。用于 MNIST 手写数字的自编码器

https://github.com/tflearn/tflearn/blob/master/examples/images/autoencoder.py

### 自然语言处理模型及数据集

- 循环神经网络（LSTM），应用 LSTM 到 IMDB 情感数据集分类任

https://github.com/tflearn/tflearn/blob/master/examples/nlp/lstm.py

- 双向 RNN（LSTM），将一个双向 LSTM 应用到 IMDB 情感数据集分类任务：

https://github.com/tflearn/tflearn/blob/master/examples/nlp/bidirectional_lstm.py

- 动态 RNN（LSTM），利用动态 LSTM 从 IMDB 数据集分类可变长度文本：

https://github.com/tflearn/tflearn/blob/master/examples/nlp/dynamic_lstm.py

- 城市名称生成，使用 LSTM 网络生成新的美国城市名：

https://github.com/tflearn/tflearn/blob/master/examples/nlp/lstm_generator_cityname.py

- 莎士比亚手稿生成，使用 LSTM 网络生成新的莎士比亚手稿：

https://github.com/tflearn/tflearn/blob/master/examples/nlp/lstm_generator_shakespeare.py

- Seq2seq，seq2seq 循环网络的教学示例：

https://github.com/tflearn/tflearn/blob/master/examples/nlp/seq2seq_****example.py

- CNN Seq，应用一个 1-D 卷积网络从 IMDB 情感数据集中分类词序列

https://github.com/tflearn/tflearn/blob/master/examples/nlp/cnn_sentence_classification.py

### 强化学习案例

- Atari Pacman 1-step Q-Learning，使用 1-step Q-learning 教一台机器玩 Atari 游戏：

https://github.com/tflearn/tflearn/blob/master/examples/reinforcement_learning/atari_1step_qlearning.py

## 第三步：为TF新手准备的其他方面内容

- Recommender-Wide&Deep Network，推荐系统中 wide & deep 网络的教学示例：

https://github.com/tflearn/tflearn/blob/master/examples/others/recommender_wide_and_deep.py

- Spiral Classification Problem，对斯坦福 CS231n spiral 分类难题的 TFLearn 实现：

tflearn/tflearn

- 与 TensorFlow 一起使用 TFLearn 层：

https://github.com/tflearn/tflearn/blob/master/examples/extending_tensorflow/layers.py

- 训练器，使用 TFLearn 训练器类训练任何 TensorFlow 图：

https://github.com/tflearn/tflearn/blob/master/examples/extending_tensorflow/layers.py

- Bulit-in Ops，连同 TensorFlow 使用 TFLearn built-in 操作：

https://github.com/tflearn/tflearn/blob/master/examples/extending_tensorflow/builtin_ops.py

- Summaries，连同 TensorFlow 使用 TFLearn summarizers：

https://github.com/tflearn/tflearn/blob/master/examples/extending_tensorflow/summaries.py

- Variables，连同 TensorFlow 使用 TFLearn Variables：

https://github.com/tflearn/tflearn/blob/master/examples/extending_tensorflow/variables.py

转载自：[干货 | TensorFlow的55个经典案例](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/Qdo1vks94tbGkzXEiuQV7w)

文中提供的网页链接，均来自于网络，如有问题，请站内告知。

*转载请先获得作者  BigQuant 同意！*