# 2、深入了解机器学习 (Descending into ML)：线性回归

**预计用时**：6 分钟

人们[早就知晓](https://wikipedia.org/wiki/Dolbear's_law)，相比凉爽的天气，蟋蟀在较为炎热的天气里鸣叫更为频繁。数十年来，专业和业余昆虫学者已将每分钟的鸣叫声和温度方面的数据编入目录。Ruth 阿姨将她喜爱的蟋蟀数据库作为生日礼物送给您，并邀请您自己利用该数据库训练一个模型，从而预测鸣叫声与温度的关系。

首先建议您将数据绘制成图表，了解下数据的分布情况：

https://developers.google.com/machine-learning/crash-course/descending-into-ml/linear-regression

**图 1. 每分钟的鸣叫声与温度（摄氏度）的关系。**

毫无疑问，此曲线图表明温度随着鸣叫声次数的增加而上升。鸣叫声与温度之间的关系是线性关系吗？是的，您可以绘制一条直线来近似地表示这种关系，如下所示：

0255075100125150175每分钟虫鸣声5101520253035温度（单位：摄氏度）

**图 2. 线性关系。**

事实上，虽然该直线并未精确无误地经过每个点，但针对我们拥有的数据，清楚地显示了鸣叫声与温度之间的关系。只需运用一点代数知识，您就可以将这种关系写下来，如下所示：

y=mx+b

其中：

- y 指的是温度（以摄氏度表示），即我们试图预测的值。
- m 指的是直线的斜率。
- x 指的是每分钟的鸣叫声次数，即输入特征的值。
- b 指的是 y 轴截距。

按照机器学习的惯例，您需要写一个存在细微差别的模型方程式：

y′=b+w1x1

其中：

- y′ 指的是预测[标签](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology#labels)（理想输出值）。
- b 指的是偏差（y 轴截距）。而在一些机器学习文档中，它称为 w0。
- w1 指的是特征 1 的权重。权重与上文中用 m 表示的“斜率”的概念相同。
- x1 指的是[特征](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology#features)（已知输入项）。

要根据新的每分钟的鸣叫声值 x1 **推断**（预测）温度 y′，只需将 x1 值代入此模型即可。

下标（例如 w1 和 x1）预示着可以用多个**特征来表示更复杂的模型。例如，具有三个特征的模型可以采用以下方程式：

y′=b+w1x1+w2x2+w3x3

 

**关键字词**[偏差](https://developers.google.com/machine-learning/glossary#bias)[推断](https://developers.google.com/machine-learning/glossary#inference)[线性回归](https://developers.google.com/machine-learning/glossary#linear_regression)[权重](https://developers.google.com/machine-learning/glossary#weight)