# TensorFlow入门

本文档介绍了TensorFlow编程环境，并向您展示了如何解决TensorFlow中的Iris分类问题。

## 先决条件

在本文档中使用示例代码之前，您需要执行以下操作：

- [安装TensorFlow](https://www.tensorflow.org/install/index?hl=zh-cn)。

- 如果您使用virtualenv或Anaconda安装了TensorFlow，请激活您的TensorFlow环境。

- 通过发出以下命令来安装或升级熊猫：

  ```
  pip install pandas
  ```

## 获取示例代码

按照以下步骤获取我们将要经历的示例代码：

1. 通过输入以下命令从GitHub克隆TensorFlow Models存储库：

   ```
   git clone https://github.com/tensorflow/models
   ```

2. 将该分支内的目录更改为包含本文档中使用的示例的位置：

   ```
   cd models/samples/core/get_started/
   ```

本文档中描述的程序是 [`premade_estimator.py`](https://github.com/tensorflow/models/blob/master/samples/core/get_started/premade_estimator.py)。该程序用于 [`iris_data.py`](https://github.com/tensorflow/models/blob/master/samples/core/get_started/iris_data.py) 获取其培训数据。

### 运行程序

您可以像运行任何Python程序一样运行TensorFlow程序。例如：

```
python premade_estimator.py
```

该程序应该输出训练日志，然后对测试集进行一些预测。例如，以下输出中的第一行显示该模型认为测试集中的第一个示例是Setosa的可能性为99.6％。由于测试集预计Setosa，这似乎是一个很好的预测。

```
...
Prediction is "Setosa" (99.6%), expected "Setosa"

Prediction is "Versicolor" (99.8%), expected "Versicolor"

Prediction is "Virginica" (97.9%), expected "Virginica"

```

如果程序显示错误而不是答案，请检查以下问题：

- 您是否正确安装了TensorFlow？
- 你使用的是正确版本的TensorFlow吗？
- 您是否激活了安装TensorFlow的环境？（这只与某些安装机制有关。）

## 编程堆栈

在深入了解程序本身的细节之前，让我们来看看编程环境。如下图所示，TensorFlow提供了一个由多个API层组成的编程堆栈：

![img](https://www.tensorflow.org/images/tensorflow_programming_environment.png?hl=zh-cn)

我们强烈建议使用以下API编写TensorFlow程序：

- [估算器](https://www.tensorflow.org/programmers_guide/estimators?hl=zh-cn) ([Estimators](https://www.tensorflow.org/programmers_guide/estimators?hl=zh-cn))： 代表一个完整的模型。Estimator API提供方法来训练模型，判断模型的准确性并生成预测。
- [数据集](https://www.tensorflow.org/get_started/datasets_quickstart?hl=zh-cn) ([Datasets](https://www.tensorflow.org/get_started/datasets_quickstart?hl=zh-cn))：构建数据输入管道。Datasets API具有加载和操作数据的方法，并将其提供给您的模型。Datasets API与Estimators API良好地协作。

## 分类irises：概述

本文档中的示例程序构建并测试了一个模型，该模型根据[萼片](https://en.wikipedia.org/wiki/Sepal)和 [花瓣](https://en.wikipedia.org/wiki/Petal)的大小将鸢尾花分为三种不同的物种 。

![比较三种鸢尾属的花瓣几何：Iris setosa，Iris virginica和Iris versicolor](https://www.tensorflow.org/images/iris_three_species.jpg?hl=zh-cn)

**从左到右， Iris setosa（由 Radomil，CC BY-SA 3.0）， 鸢尾花（ Dlanglois，CC BY-SA 3.0）和Iris virginica （by Frank Mayfield，CC BY-SA 2.0）。**

### 数据集

虹膜数据集包含四个特征和一个 [标签](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#label)。这四个特征确定了单个鸢尾花的以下植物学特征：

- 萼片长度
- 萼片宽度
- 花瓣长度
- 花瓣宽度

我们的模型将把这些特征表示为`float32`数字数据。

该标签标识鸢尾属物种，其必须是以下之一：

- Iris setosa（0）
- 杂色鸢尾花（1）
- 虹膜virginica（2）

我们的模型将标签作为`int32`分类数据。

下表显示了数据集中的三个示例：

| 萼片长度 | 萼片宽度 | 花瓣长度 | 花瓣宽度 | 物种（标签）       |
| ---- | ---- | ---- | ---- | ------------ |
| 5.1  | 3.3  | 1.7  | 0.5  | 0（Setosa）    |
| 5    | 2.3  | 3.3  | 1.0  | 1（杂色）        |
| 6.4  | 2.8  | 5.6  | 2.2  | 2（virginica） |

### 算法

该程序训练具有以下拓扑的深度神经网络分类器模型：

- 2个隐藏层。
- 每个隐藏层包含10个节点。

下图说明了特征，隐藏层和预测（并未显示隐藏层中的所有节点）：

![网络架构图：输入，2个隐藏层和输出](https://www.tensorflow.org/images/custom_estimators/full_network.png?hl=zh-cn)

### 推理

在未标记的例子上运行训练模型会得出三个预测结果，即这朵花是给定虹膜种类的可能性。这些输出预测的总和将是1.0。例如，对未标记示例的预测可能如下所示：

- 0.03为Iris Setosa
- 0.95 for Iris Versicolor
- 0.02为鸢尾Virginica

前面的预测表明给定的未标记示例是虹膜彩色的概率为95％。

## 用估计器编程的概述

Estimator是TensorFlow对完整模型的高级表示。它处理初始化，记录，保存和恢复以及许多其他功能的细节，以便您可以专注于您的模型。欲了解更多详情，请参阅 [估算人员](https://www.tensorflow.org/programmers_guide/estimators?hl=zh-cn)。

Estimator是派生自任何类[`tf.estimator.Estimator`](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator?hl=zh-cn)。TensorFlow提供了一系列 (预定义好的) [预制的Estimators](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#pre-made_Estimator) （例如`LinearRegressor`）来实现常见的ML算法。除此之外，您可以编写自己的 [定制估算器](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#custom_Estimator)。我们建议在刚开始使用TensorFlow时使用预制的估算器。在获得预先制定的估算器的专业知识后，我们建议通过创建您自己的定制估算器来优化您的模型。

要根据预先制作的估算器编写TensorFlow程序，您必须执行以下任务：

- 创建一个或多个输入功能。
- 定义模型的特征列。
- 实例化Estimator，指定特征列和各种超参数。
- 在Estimator对象上调用一个或多个方法，传递相应的输入函数作为数据源。

让我们看看这些任务是如何实施虹膜分类的。

## 创建输入功能

您必须创建输入函数来为培训，评估和预测提供数据。

一个**输入功能**是返回的函数[`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset?hl=zh-cn)，输出以下两个元素的元组对象：

- `features`

   - 一个Python字典，其中：

  - 每个键都是特征的名称。
  - 每个值都是包含所有该功能值的数组。

- `label`- 包含每个示例的[标签](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#label)值的数组 。

为了演示输入函数的格式，下面是一个简单的实现：

```
def input_evaluation_set():
    features = {'SepalLength': np.array([6.4, 5.0]),
                'SepalWidth':  np.array([2.8, 2.3]),
                'PetalLength': np.array([5.6, 3.3]),
                'PetalWidth':  np.array([2.2, 1.0])}
    labels = np.array([2, 1])
    return features, labels

```

您的输入功能可能会生成`features`字典并`label`以您喜欢的方式列出。不过，我们建议使用TensorFlow的数据集API，它可以解析各种数据。在高层次上，数据集API由以下类组成：

instantiates : 实例化， Subclass : 子类，text line: 文本行, TF record: TF记录, 

Fixed length: 固定长度, iterator: 迭代器

![显示数据集类的子类的图表](https://www.tensorflow.org/images/dataset_classes.png?hl=zh-cn)

个人会员如下：

- `Dataset` - 包含创建和转换数据集的方法的基类。还允许您从内存中的数据或Python生成器中初始化数据集。
- `TextLineDataset` - 从文本文件中读取行。
- `TFRecordDataset` - 从TFRecord文件中读取记录。
- `FixedLengthRecordDataset` - 从二进制文件中读取固定大小的记录。
- `Iterator` - 提供一次访问一个数据集元素的方法。

数据集API可以为您处理很多常见情况。例如，使用数据集API，您可以轻松地从大量文件集中并行读入记录，并将它们合并到一个流中。

为了让这个例子简单些，我们将使用[熊猫](https://pandas.pydata.org/)来加载数据 ，并从这些内存数据构建输入管道。

以下是该程序中用于培训的输入功能，可在[`iris_data.py`](https://github.com/tensorflow/models/blob/master/samples/core/get_started/iris_data.py)以下位置获得：

tensor: 张量,  slices: 片,  shuffle: 拖曳,  reoeat: 重复,  batch: 批量

```
def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    return dataset.shuffle(1000).repeat().batch(batch_size)

```

## 定义特征列

甲[**特征柱**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#feature_columns) 是描述如何模型应该从特征字典使用原始输入数据的对象。在构建Estimator模型时，您会传递一个功能列列表来描述您希望模型使用的每个功能。该[`tf.feature_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column?hl=zh-cn)模块提供了很多用于向模型表示数据的选项。

对于Iris，4个原始特征是数值，因此我们将构建一个特征列列表，以告诉Estimator模型将四个特征中的每一个都表示为32位浮点值。因此，创建功能列的代码是：

```
# Feature columns describe how to use the input.
my_feature_columns = []
for key in train_x.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

```

特征列可能比我们在这里展示的要复杂得多。我们将在“入门指南”中[稍后](https://www.tensorflow.org/get_started/feature_columns?hl=zh-cn)详细介绍功能列。

现在我们已经描述了我们希望模型如何表示原始特征，我们可以构建估计器。

## 实例化一个估计器

虹膜问题是一个经典的分类问题。幸运的是，TensorFlow提供了几个预先制作的分类器Estimators，其中包括：

- [`tf.estimator.DNNClassifier`](https://www.tensorflow.org/api_docs/python/tf/estimator/DNNClassifier?hl=zh-cn) 适用于执行多级分类的深层模型。
- [`tf.estimator.DNNLinearCombinedClassifier`](https://www.tensorflow.org/api_docs/python/tf/estimator/DNNLinearCombinedClassifier?hl=zh-cn) 广泛和深刻的模型。
- [`tf.estimator.LinearClassifier`](https://www.tensorflow.org/api_docs/python/tf/estimator/LinearClassifier?hl=zh-cn) 用于基于线性模型的分类器。

对于虹膜问题，`tf.estimator.DNNClassifier`看起来是最好的选择。以下是我们如何实例化此Estimator的方法：

```python
# Build a DNN with 2 hidden layers and 10 nodes in each hidden layer.
# 构建一个拥有两个隐藏层的DNN，每个隐藏层有10个节点
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    # Two hidden layers of 10 nodes each.两个隐藏层，每层10个节点。
    hidden_units=[10, 10],
    # The model must choose between 3 classes.该模型必须在3个类之间进行选择。
    n_classes=3)

```

## 培训，评估和预测

现在我们有一个Estimator对象，我们可以调用方法来执行以下操作：

- 训练模型。
- 评估训练的模型。
- 使用训练好的模型进行预测。

### 训练模型

通过调用Estimator的`train`方法来训练模型如下：

```
# Train the Model.
classifier.train(
    input_fn=lambda:iris_data.train_input_fn(train_x, train_y, args.batch_size),
    steps=args.train_steps)

```

在这里，我们用`input_fn`a [`lambda`](https://docs.python.org/3/tutorial/controlflow.html) 来包装我们的调用 来捕获参数，同时提供一个不带参数的输入函数，正如Estimator预期的那样。该`steps`论点告诉方法在多次训练步骤后停止训练。

### 评估训练的模型

现在模型已经过训练，我们可以获得一些关于其性能的统计数据。以下代码块评估测试数据上训练模型的准确性：

```
# Evaluate the model.
eval_result = classifier.evaluate(
    input_fn=lambda:iris_data.eval_input_fn(test_x, test_y, args.batch_size))

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

```

与我们对该`train`方法的调用不同，我们没有通过`steps` 参数来评估。我们`eval_input_fn`只会产生一个单一 的数据[时代](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#epoch)。

运行此代码会生成以下输出（或类似内容）：

```
Test set accuracy: 0.967

```

### 从训练的模型中进行预测（推断）

我们现在有一个训练有素的模型，可以产生良好的评估结果 我们现在可以使用训练好的模型根据一些未标记的测量结果来预测鸢尾花的种类。与培训和评估一样，我们使用单个函数调用进行预测：

```
# Generate predictions from the model
expected = ['Setosa', 'Versicolor', 'Virginica']
predict_x = {
    'SepalLength': [5.1, 5.9, 6.9],
    'SepalWidth': [3.3, 3.0, 3.1],
    'PetalLength': [1.7, 4.2, 5.4],
    'PetalWidth': [0.5, 1.5, 2.1],
}

predictions = classifier.predict(
    input_fn=lambda:iris_data.eval_input_fn(predict_x,
                                            batch_size=args.batch_size))

```

该`predict`方法返回一个Python迭代器，为每个示例生成一个预测结果字典。以下代码打印了一些预测及其概率：

```
for pred_dict, expec in zip(predictions, expected):
    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    class_id = pred_dict['class_ids'][0]
    probability = pred_dict['probabilities'][class_id]

    print(template.format(iris_data.SPECIES[class_id],
                          100 * probability, expec))

```

运行上面的代码将生成以下输出：

```
...
Prediction is "Setosa" (99.6%), expected "Setosa"

Prediction is "Versicolor" (99.8%), expected "Versicolor"

Prediction is "Virginica" (97.9%), expected "Virginica"

```

## 概要

预制估算器是快速创建标准模型的有效方法。

现在您已经开始编写TensorFlow程序，请考虑以下材料：

- 了解如何保存和恢复模型的[检查点](https://www.tensorflow.org/get_started/checkpoints?hl=zh-cn)。
- [数据集](https://www.tensorflow.org/get_started/datasets_quickstart?hl=zh-cn)了解有关将数据导入模型的更多信息。
- [创建自定义估算器](https://www.tensorflow.org/get_started/custom_estimators?hl=zh-cn)以了解如何编写自己的估算器，并根据特定问题进行定制。





-----------------------

# ML初学者入门

本文档解释了如何使用机器学习按物种对鸢尾花进行分类（分类）。本文深入介绍了TensorFlow代码，以此来解释ML的基本原理。

如果以下列表描述了你，那么你是在正确的地方：

- 你对机器学习一无所知。
- 你想学习如何编写TensorFlow程序。
- 你可以用Python编写（至少一点）。

如果您已经熟悉基本的机器学习概念，但对TensorFlow来说是新手，请阅读TensorFlow [入门：针对ML专家](https://www.tensorflow.org/get_started/premade_estimators?hl=zh-cn)。

## 虹膜分类问题

想象一下，你是一位植物学家，寻找一种自动化的方法来对你发现的每个鸢尾花进行分类。机器学习提供了许多方法来分类花卉。例如，一个复杂的机器学习程序可以根据照片对花进行分类。我们的野心比较温和 - 我们将根据[萼片](https://en.wikipedia.org/wiki/Sepal)和 [花瓣](https://en.wikipedia.org/wiki/Petal)的长度和宽度对鸢尾花进行分类 。

虹膜属约300种，但我们的计划将只分类以下三种：

- Iris setosa
- 虹膜virginica
- 杂色鸢尾花

![比较三种鸢尾属的花瓣几何：Iris setosa，Iris virginica和Iris versicolor](https://www.tensorflow.org/images/iris_three_species.jpg?hl=zh-cn)

**从左到右， Iris setosa（由 Radomil，CC BY-SA 3.0）， 鸢尾花（ Dlanglois，CC BY-SA 3.0）和Iris virginica （by Frank Mayfield，CC BY-SA 2.0）。**

 

幸运的是，有人已经创建[了一个](https://en.wikipedia.org/wiki/Iris_flower_data_set) 由萼片和花瓣测量结果组成[的120个鸢尾花数据集](https://en.wikipedia.org/wiki/Iris_flower_data_set)。该数据集已成为机器学习分类问题的标准介绍之一。（包含手写数字的[MNIST数据库](https://en.wikipedia.org/wiki/MNIST_database)是另一个流行的分类问题。）Iris数据集的前5个条目如下所示：

| 萼片长度 | 萼片宽度 | 花瓣长度 | 花瓣宽度 | 种类   |
| ---- | ---- | ---- | ---- | ---- |
| 6.4  | 2.8  | 5.6  | 2.2  | 2    |
| 5    | 2.3  | 3.3  | 1.0  | 1    |
| 4.9  | 2.5  | 4.5  | 1.7  | 2    |
| 4.9  | 3.1  | 1.5  | 0.1  | 0    |
| 5.7  | 3.8  | 1.7  | 0.3  | 0    |

我们来介绍一些条款：

- 最后一列（物种）被称为 [**标签**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#label) ; 前四列称为 [**功能**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#feature)。特征是一个例子的特征，而标签是我们试图预测的。
- 一个[**示例**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#example) 由一组样本和一个样本花的标签组成。上表显示了来自120个示例的数据集的5个示例。

每个标签自然是一个字符串（例如，“setosa”），但机器学习通常依赖于数字值。因此，有人将每个字符串映射到一个数字。这是表示方案：

- 0代表setosa
- 1代表杂色
- 2代表维吉尼卡

## 模型和培训

一个**模型**是功能和标签之间的关系。对于虹膜问题，该模型定义了萼片和花瓣测量值与虹膜种类之间的关系。一些简单的模型可以用几行代数来描述; 更复杂的机器学习模型包含如此大量的交错数学函数和参数，以至于难以在数学上进行总结。

你可以在*不*使用机器学习的*情况下*确定四种特征和虹膜种类之间的关系吗？也就是说，您是否可以使用传统编程技术（例如，大量条件语句）来创建模型？也许。您可以使用足够长的数据集来确定花瓣和萼片测量与特定物种的正确关系。然而，一个好的机器学习方法*为你确定了模型*。也就是说，如果您将足够多的代表性示例用于正确的机器学习模型类型，程序将确定萼片，花瓣和物种之间的关系。

**培训**是机器学习的阶段，其中模型逐渐优化（学习）。虹膜问题是[**监督机器学习的**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#supervised_machine_learning)一个例子， 其中模型是从包含标签的示例中进行训练的。（在 [**无监督机器学习中**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#unsupervised_machine_learning)，示例不包含标签，而是典型地在模型中找到模式。）

## 获取示例程序

在使用本文档中的示例代码之前，请执行以下操作：

1. [安装TensorFlow](https://www.tensorflow.org/install/index?hl=zh-cn)。

2. 如果您使用virtualenv或Anaconda安装了TensorFlow，请激活您的TensorFlow环境。

3. 通过发出以下命令来安装或升级熊猫：

   `pip install pandas`

采取以下步骤获取示例程序：

1. 通过输入以下命令从github克隆TensorFlow Models存储库：

   `git clone https://github.com/tensorflow/models`

2. 将该分支内的目录更改为包含本文档中使用的示例的位置：

   `cd models/samples/core/get_started/`

在该`get_started`目录中，您会找到一个名为的程序`premade_estimator.py`。

## 运行示例程序

您可以像运行任何Python程序一样运行TensorFlow程序。因此，从命令行执行以下命令即可运行`premade_estimators.py`：

```
python premade_estimator.py

```

运行程序应输出一大堆以三条预测线结束的信息，如下所示：

```
...
Prediction is "Setosa" (99.6%), expected "Setosa"

Prediction is "Versicolor" (99.8%), expected "Versicolor"

Prediction is "Virginica" (97.9%), expected "Virginica"

```

如果程序生成错误而不是预测，请问自己以下问题：

- 您是否正确安装了TensorFlow？
- 你使用的是正确版本的TensorFlow吗？该`premade_estimators.py` 程序至少需要TensorFlow v1.4。
- 如果您使用virtualenv或Anaconda安装了TensorFlow，您是否激活了环境？

## TensorFlow编程堆栈

如下图所示，TensorFlow提供了一个由多个API层组成的编程堆栈：

![img](https://www.tensorflow.org/images/tensorflow_programming_environment.png?hl=zh-cn)

**TensorFlow编程环境。**

 

在您开始编写TensorFlow程序时，我们强烈建议您关注以下两个高级API：

- 估计
- 数据集

虽然我们会从其他API中获取偶尔的便利功能，但本文档重点关注前两个API。

## 程序本身

谢谢你的耐心; 让我们深入代码。以及`premade_estimator.py`许多其他TensorFlow程序的总体概述如下：

- 导入和解析数据集。
- 创建要素列以描述数据。
- 选择模型的类型
- 训练模型。
- 评估模型的有效性。
- 让训练好的模型进行预测。

以下小节详细说明每个部分。

### 导入和解析数据集

Iris程序需要以下两个.csv文件中的数据：

- `http://download.tensorflow.org/data/iris_training.csv`，其中包含训练集。
- `http://download.tensorflow.org/data/iris_test.csv`，其中包含测试集。

该**训练集**包含了我们将用它来训练模型的例子; 该**测试集**包含了我们将用它来评估训练模型的有效性的例子。

训练集和测试集作为单个数据集开始。然后，有人将这些例子分解，大多数人进入训练集，剩下的人进入测试集。在训练集中添加示例通常会构建一个更好的模型; 然而，在测试集中添加更多示例使我们能够更好地评估模型的有效性。无论分割如何，测试集中的示例都必须与训练集中的示例分开。否则，您无法准确确定模型的有效性。

该`premade_estimators.py`程序依赖于`load_data`相邻[`iris_data.py`](https://github.com/tensorflow/models/blob/master/samples/core/get_started/iris_data.py) 文件中的功能来读入和解析训练集和测试集。这里是一个重要的评论版本的功能：

```
TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth',
                    'PetalLength', 'PetalWidth', 'Species']

...

def load_data(label_name='Species'):
    """Parses the csv file in TRAIN_URL and TEST_URL."""

    # Create a local copy of the training set.
    train_path = tf.keras.utils.get_file(fname=TRAIN_URL.split('/')[-1],
                                         origin=TRAIN_URL)
    # train_path now holds the pathname: ~/.keras/datasets/iris_training.csv

    # Parse the local CSV file.
    train = pd.read_csv(filepath_or_buffer=train_path,
                        names=CSV_COLUMN_NAMES,  # list of column names
                        header=0  # ignore the first row of the CSV file.
                       )
    # train now holds a pandas DataFrame, which is data structure
    # analogous to a table.

    # 1. Assign the DataFrame's labels (the right-most column) to train_label.
    # 2. Delete (pop) the labels from the DataFrame.
    # 3. Assign the remainder of the DataFrame to train_features
    train_features, train_label = train, train.pop(label_name)

    # Apply the preceding logic to the test set.
    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)
    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_features, test_label = test, test.pop(label_name)

    # Return four DataFrames.
    return (train_features, train_label), (test_features, test_label)

```

Keras是一个开源的机器学习库，`tf.keras`是Keras的TensorFlow实现。该`premade_estimator.py`程序只能访问一个`tf.keras`函数; 即`tf.keras.utils.get_file`便利功能，它将远程CSV文件复制到本地文件系统。

呼叫`load_data`返回两`(feature,label)`对，分别为训练和测试集：

```
    # Call load_data() to parse the CSV file.
    (train_feature, train_label), (test_feature, test_label) = load_data()

```

Pandas是由几个TensorFlow函数利用的开源Python库。熊猫 [**DataFrame**](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) 是一个具有命名列标题和编号行的表。返回的功能`load_data`被打包`DataFrames`。例如，`test_feature`DataFrame如下所示：

```
    SepalLength  SepalWidth  PetalLength  PetalWidth
0           5.9         3.0          4.2         1.5
1           6.9         3.1          5.4         2.1
2           5.1         3.3          1.7         0.5
...
27          6.7         3.1          4.7         1.5
28          6.7         3.3          5.7         2.5
29          6.4         2.9          4.3         1.3

```

### 描述数据

一个**功能柱**是一种数据结构，它告诉你的模型如何解释每个功能的数据。在虹膜问题中，我们希望模型将每个特征中的数据解释为它的文字浮点值; 也就是说，我们希望模型将5.4的输入值解释为5.4。但是，在其他机器学习问题中，通常希望不太字面解释数据。使用功能列来解释数据是一个非常丰富的主题，我们将整个 [文档](https://www.tensorflow.org/get_started/feature_columns?hl=zh-cn)用于它。

从代码角度来看，您可以`feature_column`通过调用[`tf.feature_column`](https://www.tensorflow.org/api_docs/python/tf/feature_column?hl=zh-cn)模块中的函数来构建对象列表。每个对象都描述了模型的输入。要告诉模型将数据解释为浮点值，请调用@ {tf.feature_column.numeric_column）。在中`premade_estimator.py`，所有四个特征应该被解释为文字浮点值，所以创建特征列的代码如下所示：

```
# Create feature columns for all features.
my_feature_columns = []
for key in train_x.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

```

这是一个不太优雅的，但可能更清晰的替代方法来编码前面的块：

```
my_feature_columns = [
    tf.feature_column.numeric_column(key='SepalLength'),
    tf.feature_column.numeric_column(key='SepalWidth'),
    tf.feature_column.numeric_column(key='PetalLength'),
    tf.feature_column.numeric_column(key='PetalWidth')
]

```

### 选择模型的类型

我们需要选择将要训练的那种模型。存在许多模型类型; 选择理想的类型需要经验。我们选择了一个神经网络来解决虹膜问题。 [**神经网络**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#neural_network) 可以找到特征和标签之间的复杂关系。神经网络是一个高度结构化的图，组织成一个或多个 [**隐藏层**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#hidden_layer)。每个隐藏层由一个或多个 [**神经元组成**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#neuron)。有几类神经网络。我们将使用[**完全连接的神经网络**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#fully_connected_layer)，这意味着一层中的神经元从上一层中的*每个*神经元获取输入。例如，下图说明了由三个隐藏层组成的完全连接的神经网络：

- 第一个隐藏层包含四个神经元。
- 第二个隐藏层包含三个神经元。
- 第三个隐藏层包含两个神经元。

![img](https://www.tensorflow.org/images/simple_dnn.svg?hl=zh-cn)

**具有三个隐藏层的神经网络。**

 

要指定模型类型，请实例化一个 [**Estimator**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#Estimators) 类。TensorFlow提供了两类估算器：

- [**预先制作的估算器**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#pre-made_Estimator)，其他人已经为您编写。
- [**自定义估算器**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#custom_estimator)，您必须至少部分编码自己。

为了实现神经网络，该`premade_estimators.py`程序使用预先制作的估算器命名[`tf.estimator.DNNClassifier`](https://www.tensorflow.org/api_docs/python/tf/estimator/DNNClassifier?hl=zh-cn)。这个Estimator构建了一个分类示例的神经网络。以下调用实例化`DNNClassifier`：

```
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[10, 10],
        n_classes=3)

```

使用该`hidden_units`参数来定义神经网络每个隐藏层中的神经元数量。为此参数分配一个列表。例如：

```
        hidden_units=[10, 10],

```

分配给列表的长度`hidden_units`标识隐藏层的数量（在本例中为2）。列表中的每个值表示特定隐藏层中的神经元数（第一个隐藏层中的10个，第二个隐藏层中的10个）。要更改隐藏层或神经元的数量，只需将不同的列表分配给`hidden_units`参数。

隐藏层和神经元的理想数量取决于问题和数据集。像机器学习的许多方面一样，选择神经网络的理想形状需要知识和实验的混合。作为一个经验法则，增加隐藏层和神经元的数量 *通常*会创建一个更强大的模型，这需要更多的数据进行有效训练。

该`n_classes`参数指定了神经网络可以预测的可能值的数量。由于虹膜问题将3种虹膜种类分类，我们设定`n_classes`为3。

构造函数`tf.Estimator.DNNClassifier`接受一个名为的可选参数`optimizer`，我们的示例代码选择不指定。该 [**优化**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#optimizer) 控制模型如何训练。随着您在机器学习方面开发更多专业知识，优化器和 [**学习速度**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#learning_rate) 将变得非常重要。

### 训练模型

实例化`tf.Estimator.DNNClassifier`创建了一个学习模型的框架。基本上，我们已经连线了一个网络，但还没有让数据流过它。要训练神经网络，请调用Estimator对象的`train` 方法。例如：

```
    classifier.train(
        input_fn=lambda:train_input_fn(train_feature, train_label, args.batch_size),
        steps=args.train_steps)

```

该`steps`参数告诉`train`在指定次数的迭代后停止训练。增加会`steps`增加模型训练的时间。相反，直观地说，长时间训练模型并不能保证更好的模型。默认值`args.train_steps` 是1000.要训练的步数是一个 可以调整的 [**超参数**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#hyperparameter)。选择正确的步骤数通常需要经验和实验。

该`input_fn`参数标识提供训练数据的功能。对该`train`方法的调用表明该 `train_input_fn`功能将提供训练数据。这是该方法的签名：

```
def train_input_fn(features, labels, batch_size):

```

我们将以下参数传递给`train_input_fn`：

- ```
  train_feature
  ```

   是一个Python字典，其中：

  - 每个键都是特征的名称。
  - 每个值都是包含训练集中每个示例值的数组。

- `train_label` 是包含训练集中每个示例的标签值的数组。

- `args.batch_size`是一个定义[**批量大小**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#batch_size)的整数。

该`train_input_fn`函数依赖于**数据集API**。这是一个高级TensorFlow API，用于读取数据并将其转换为该`train`方法所需的形式。以下调用将输入要素和标签转换为一个`tf.data.Dataset`对象，该对象是Dataset API的基类：

```
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

```

该`tf.dataset`课程提供了许多有用的功能来准备培训示例。以下行称这些函数中的三个：

```
    dataset = dataset.shuffle(buffer_size=1000).repeat(count=None).batch(batch_size)

```

如果训练示例是随机排列的，则训练效果最好。要随机化示例，请致电 `tf.data.Dataset.shuffle`。将该`buffer_size`值设置为大于示例数（120）的值可以确保数据将被彻底清理。

在培训期间，该`train`方法通常会多次处理这些示例。在`tf.data.Dataset.repeat`没有任何参数的情况下调用该 方法可以确保该`train`方法拥有无限量的（现在是混洗的）训练集示例。

该`train`方法一次处理 [**一批**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#batch) 示例。该`tf.data.Dataset.batch`方法通过连接多个示例来创建批处理。该程序将默认[**批量大小设置**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#batch_size) 为100，表示该`batch`方法将连接100个示例组。理想的批量大小取决于问题。作为一个经验法则，较小的批量通常可以使该`train`方法以更高的精度（有时）更快地训练模型。

以下`return`语句将一批示例传回给调用方（`train`方法）。

```
   return dataset.make_one_shot_iterator().get_next()

```

### 评估模型

**评估**意味着确定模型如何有效地进行预测。要确定虹膜分类模型的有效性，请将一些萼片和花瓣测量结果传递给模型，并要求模型预测它们代表的虹膜种类。然后将模型的预测与实际标签进行比较。例如，在一半输入示例中挑选正确种类的模型将具有 0.5 的 [准确度](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#accuracy)。以下建议一个更有效的模型：

| 测试集  |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 特征   | 标签   | 预测   |      |      |      |
| 5.9  | 3.0  | 4.3  | 1.5  | 1    | 1    |
| 6.9  | 3.1  | 5.4  | 2.1  | 2    | 2    |
| 5.1  | 3.3  | 1.7  | 0.5  | 0    | 0    |
| 6    | 3.4  | 4.5  | 1.6  | 1    | 2    |
| 5.5  | 2.5  | 4    | 1.3  | 1    | 1    |

**一个80％准确的模型。**

 

为了评估模型的有效性，每个估算器都提供了一种`evaluate` 方法。该`premade_estimator.py`程序调用`evaluate`如下：

```
# Evaluate the model.
eval_result = classifier.evaluate(
    input_fn=lambda:eval_input_fn(test_x, test_y, args.batch_size))

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

```

呼叫`classifier.evaluate`类似于呼叫`classifier.train`。最大的区别是`classifier.evaluate`必须从测试集而不是训练集中得到它的例子。换句话说，为了公平评估模型的有效性，用于 *评估*模型的示例必须与用于*训练* 模型的示例不同。该`eval_input_fn`函数提供了一组来自测试集的示例。这里的`eval_input_fn`方法：

```
def eval_input_fn(features, labels=None, batch_size=None):
    """An input function for evaluation or prediction"""
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert inputs to a tf.dataset object.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the read end of the pipeline.
    return dataset.make_one_shot_iterator().get_next()

```

简而言之，`eval_input_fn`通过以下方式进行呼叫时 `classifier.evaluate`：

1. 将要素和标签从测试集转换为`tf.dataset` 对象。
2. 创建一批测试集示例。（没有必要洗牌或重复测试集示例。）
3. 将该批测试集示例返回给`classifier.evaluate`。

运行此代码会生成以下输出（或与之相近的东西）：

```
Test set accuracy: 0.967

```

准确度为0.967意味着我们的训练模型在测试集中的30种虹膜种类中正确分类了29种。

### 预测

我们现在已经训练了一个模型并“证明”它在分类鸢尾属物种方面是好的 - 但并不完美。现在让我们使用训练好的模型对[**未标记的示例**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#unlabeled_example)进行一些预测; 即包含功能但不包含标签的示例。

在现实生活中，未标记的示例可能来自许多不同的来源，包括应用程序，CSV文件和数据馈送。现在，我们只需手动提供以下三个未标记的示例：

```
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }

```

每个Estimator都提供了一个`predict`方法，其`premade_estimator.py` 调用如下：

```
predictions = classifier.predict(
    input_fn=lambda:eval_input_fn(predict_x, batch_size=args.batch_size))

```

与该`evaluate`方法一样，我们的`predict`方法也收集该`eval_input_fn`方法的示例。

在做预测时，我们*不会*传递标签`eval_input_fn`。因此，`eval_input_fn`做到以下几点：

1. 从我们刚创建的3元素手册集转换特征。
2. 从该手册集创建一批3个示例。
3. 将该批示例返回给`classifier.predict`。

该`predict`方法返回一个python iterable，为每个示例生成一个预测结果字典。这本字典包含几个键。该`probabilities`键包含三个浮点值的列表，每个浮点值表示输入示例是特定虹膜种类的概率。例如，请考虑以下`probabilities`列表：

```
'probabilities': array([  1.19127117e-08,   3.97069454e-02,   9.60292995e-01])

```

上面的列表表明：

- 虹膜是Setosa的可能性微乎其微。
- 虹膜变色的几率为3.97％。
- Iris成为Virginica的几率为96.0％。

的`class_ids`关键认为识别最可能的种类的一元件阵列。例如：

```
'class_ids': array([2])

```

该数字`2`对应于Virginica。以下代码遍历返回的`predictions`每个预测报告：

```
for pred_dict, expec in zip(predictions, expected):
    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    class_id = pred_dict['class_ids'][0]
    probability = pred_dict['probabilities'][class_id]
    print(template.format(SPECIES[class_id], 100 * probability, expec))

```

运行该程序会产生以下输出：

```
...
Prediction is "Setosa" (99.6%), expected "Setosa"

Prediction is "Versicolor" (99.8%), expected "Versicolor"

Prediction is "Virginica" (97.9%), expected "Virginica"

```

## 概要

本文档简要介绍了机器学习。

因为`premade_estimators.py`依赖于高级API，所以机器学习中的大部分数学复杂性都是隐藏的。如果你打算更加精通机器学习，我们建议最终学习更多关于[**梯度下降**](https://developers.google.com/machine-learning/glossary/?hl=zh-cn#gradient_descent)，批处理和神经网络的知识。

我们建议阅读下面的[Feature Columns](https://www.tensorflow.org/get_started/feature_columns?hl=zh-cn)文档，它解释了如何在机器学习中表示不同类型的数据。



