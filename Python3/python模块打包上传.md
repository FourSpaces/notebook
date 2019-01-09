http://www.10tiao.com/html/383/201704/2247484310/1.html

https://www.idaima.com/article/9354

http://blog.csdn.net/wdxin1322/article/details/56685094

http://peterdowns.com/posts/first-time-with-pypi.html

https://zhuanlan.zhihu.com/p/26159930

http://python.jobbole.com/86443/

https://my.oschina.net/letiantian/blog/788056



官方文档

https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi

# 打包和分发项目

本节将介绍如何配置，打包和分发自己的Python项目的基础知识。假定您已经熟悉[安装](https://pip.pypa.io/en/latest/installing/)页面的内容。

该条文并*没有*旨在涵盖Python项目开发为一体的最佳实践。例如，它不提供版本控制，文档或测试的指导或工具建议。

有关更多参考资料，请参阅[setuptools](https://packaging.python.org/key_projects/#setuptools)文档中的 [构建和分发软件包](https://setuptools.readthedocs.io/en/latest/setuptools.html)，但请注意，某些咨询内容可能已过时。如果发生冲突，请使用“Python打包用户指南”中的建议。

内容

- [包装和分发要求](https://packaging.python.org/tutorials/distributing-packages/#requirements-for-packaging-and-distributing)
- 配置您的项目
  - 初始文件
    - [setup.py](https://packaging.python.org/tutorials/distributing-packages/#setup-py)
    - [setup.cfg](https://packaging.python.org/tutorials/distributing-packages/#setup-cfg)
    - [README.rst](https://packaging.python.org/tutorials/distributing-packages/#readme-rst)
    - [MANIFEST.in](https://packaging.python.org/tutorials/distributing-packages/#manifest-in)
    - [LICENSE.TXT](https://packaging.python.org/tutorials/distributing-packages/#license-txt)
    - [<您的包裹>](https://packaging.python.org/tutorials/distributing-packages/#your-package)
  - setup（）参数
    - [名称](https://packaging.python.org/tutorials/distributing-packages/#name)
    - [版](https://packaging.python.org/tutorials/distributing-packages/#version)
    - [描述](https://packaging.python.org/tutorials/distributing-packages/#description)
    - [网址](https://packaging.python.org/tutorials/distributing-packages/#url)
    - [作者](https://packaging.python.org/tutorials/distributing-packages/#author)
    - [执照](https://packaging.python.org/tutorials/distributing-packages/#license)
    - [分类](https://packaging.python.org/tutorials/distributing-packages/#classifiers)
    - [关键字](https://packaging.python.org/tutorials/distributing-packages/#keywords)
    - [包](https://packaging.python.org/tutorials/distributing-packages/#packages)
    - [install_requires](https://packaging.python.org/tutorials/distributing-packages/#install-requires)
    - [python_requires](https://packaging.python.org/tutorials/distributing-packages/#python-requires)
    - [package_data](https://packaging.python.org/tutorials/distributing-packages/#package-data)
    - [data_files](https://packaging.python.org/tutorials/distributing-packages/#data-files)
    - [脚本](https://packaging.python.org/tutorials/distributing-packages/#scripts)
    - entry_points
      - [console_scripts](https://packaging.python.org/tutorials/distributing-packages/#console-scripts)
  - 选择版本控制方案
    - [符合互操作性的标准](https://packaging.python.org/tutorials/distributing-packages/#standards-compliance-for-interoperability)
    - 方案选择
      - [语义版本（首选）](https://packaging.python.org/tutorials/distributing-packages/#semantic-versioning-preferred)
      - [基于日期的版本控制](https://packaging.python.org/tutorials/distributing-packages/#date-based-versioning)
      - [串行版本控制](https://packaging.python.org/tutorials/distributing-packages/#serial-versioning)
      - [混合方案](https://packaging.python.org/tutorials/distributing-packages/#hybrid-schemes)
    - [预发行版本](https://packaging.python.org/tutorials/distributing-packages/#pre-release-versioning)
    - [本地版本标识符](https://packaging.python.org/tutorials/distributing-packages/#local-version-identifiers)
- [在“开发模式”下工作](https://packaging.python.org/tutorials/distributing-packages/#working-in-development-mode)
- 打包你的项目
  - [来源分布](https://packaging.python.org/tutorials/distributing-packages/#source-distributions)
  - 车轮
    - [通用车轮](https://packaging.python.org/tutorials/distributing-packages/#universal-wheels)
    - [纯蟒蛇车轮](https://packaging.python.org/tutorials/distributing-packages/#pure-python-wheels)
    - [平台车轮](https://packaging.python.org/tutorials/distributing-packages/#platform-wheels)
- 上传您的项目到PyPI
  - [创建一个帐户](https://packaging.python.org/tutorials/distributing-packages/#create-an-account)
  - [上传你的发行版](https://packaging.python.org/tutorials/distributing-packages/#upload-your-distributions)

## [包装和分发要求](https://packaging.python.org/tutorials/distributing-packages/#id32)

1. 首先，确保你已经达到了[安装软件包](https://packaging.python.org/tutorials/installing-packages/#installing-requirements)的[要求](https://packaging.python.org/tutorials/installing-packages/#installing-requirements)。

2. 安装“twine” [[1\]](https://packaging.python.org/tutorials/distributing-packages/#id30)：

   ```
   pip install twine

   ```

   你将需要这个上传你的项目[分配](https://packaging.python.org/glossary/#term-distribution-package)到[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)（见[下文](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)）。

## [配置您的项目](https://packaging.python.org/tutorials/distributing-packages/#id33)

### [初始文件](https://packaging.python.org/tutorials/distributing-packages/#id34)

#### [的setup.py ](https://packaging.python.org/tutorials/distributing-packages/#id35)

最重要的文件是“setup.py”，它存在于项目目录的根目录下。举一个例子，看到[setup.py](https://github.com/pypa/sampleproject/blob/master/setup.py)在[PyPA示例项目](https://github.com/pypa/sampleproject)。

“setup.py”有两个主要功能：

1. 这是您的项目的各个方面配置的文件。其主要特点`setup.py`是它包含一个全局`setup()` 函数。这个函数的关键字参数是如何定义项目的具体细节。最相关的论点将在[下面的部分](https://packaging.python.org/tutorials/distributing-packages/#setup-args)进行解释 。
2. 这是用于运行与打包任务相关的各种命令的命令行界面。要获取可用命令的列表，请运行 。`python setup.py --help-commands`

#### [setup.cfg ](https://packaging.python.org/tutorials/distributing-packages/#id36)

“setup.cfg”是一个包含`setup.py` 命令默认选项的ini文件。举一个例子，看到[setup.cfg](https://github.com/pypa/sampleproject/blob/master/setup.cfg)在[PyPA示例项目](https://github.com/pypa/sampleproject)。

#### [README.rst ](https://packaging.python.org/tutorials/distributing-packages/#id37)

所有项目都应该包含一个自述文件，涵盖项目的目标。最常见的格式是带有“rst”扩展名的[reStructuredText](http://docutils.sourceforge.net/rst.html)，尽管这不是必需的。

举一个例子，看到[README.rst](https://github.com/pypa/sampleproject/blob/master/README.rst)从[PyPA样本项目](https://github.com/pypa/sampleproject)。

#### [MANIFEST.in ](https://packaging.python.org/tutorials/distributing-packages/#id38)

一个`MANIFEST.in`需要在您需要打包未自动包含在源代码分发其他文件某些情况下。要查看默认包含内容的列表，请参阅[distutils](https://packaging.python.org/key_projects/#distutils)文档中的[指定要分发的文件](https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute) 部分。

举一个例子，看到[MANIFEST.in](https://github.com/pypa/sampleproject/blob/master/MANIFEST.in)从[PyPA样本项目](https://github.com/pypa/sampleproject)。

有关编写`MANIFEST.in`文件的详细信息，请参阅[distutils](https://packaging.python.org/key_projects/#distutils)文档中[的MANIFEST.in模板](https://docs.python.org/2/distutils/sourcedist.html#the-manifest-in-template) 部分。

注意

 

`MANIFEST.in` 不会影响车轮等二元分配。

#### [LICENSE.TXT ](https://packaging.python.org/tutorials/distributing-packages/#id39)

每个软件包应包括一个许可证文件，详细说明分配条款。在许多司法管辖区，没有明确许可的软件包不能由版权所有者以外的任何人合法使用或分发。如果您不确定要选择哪个许可证，则可以使用 [GitHub的“选择许可证”](https://choosealicense.com/)或咨询律师等资源。

举一个例子，看[LICENSE.TXT](https://github.com/pypa/sampleproject/blob/master/LICENSE.txt)从[PyPA样本项目](https://github.com/pypa/sampleproject)。

#### [<你的软件包> ](https://packaging.python.org/tutorials/distributing-packages/#id40)

尽管不是必需的，但最常见的做法是将Python模块和包包含在与您的项目[名称](https://packaging.python.org/tutorials/distributing-packages/#setup-name)相同的一个顶级包中 ，或者非常接近。

有关示例，请参阅[PyPA示例项目中](https://github.com/pypa/sampleproject)包含的[示例](https://github.com/pypa/sampleproject/tree/master/sample)包。

### [setup（）](https://packaging.python.org/tutorials/distributing-packages/#id41)

如上所述，其主要特点`setup.py`是它包含一个全局`setup()`函数。这个函数的关键字参数是如何定义项目的具体细节。

下面解释最相关的论点。给出的片段是取自[setup.py](https://github.com/pypa/sampleproject/blob/master/setup.py)包含在 [PyPA示例项目](https://github.com/pypa/sampleproject)。

#### [命名](https://packaging.python.org/tutorials/distributing-packages/#id42)

```
name = 'sample' ，

```

这是你的项目的名字，确定你的项目是如何在[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)上列出的 。每[**PEP 508**](https://www.python.org/dev/peps/pep-0508)，有效的项目名称必须：

- 仅包含ASCII字母，数字，下划线（`_`），连字符（`-`）和/或句号（`.`）和
- 以ASCII字母或数字开始和结束。

项目名称的比较是不区分大小写的，将任意长度的下划线，连字符和/或句号等同对待。例如，如果您注册了一个名为的项目`cool-stuff`，用户将能够使用以下任何拼写方式下载它或声明依赖关系：

```
Cool-Stuff
cool.stuff
COOL_STUFF
CoOl__-.-__sTuFF

```

#### [版本](https://packaging.python.org/tutorials/distributing-packages/#id43)

```
version = '1.2.0' ，

```

这是您的项目的当前版本，允许您的用户确定他们是否拥有最新版本，并指出他们针对自己的软件测试了哪些特定的版本。

如果您发布项目，则版本将显示在每个版本的[PyPI上](https://packaging.python.org/glossary/#term-python-package-index-pypi)。

有关如何使用版本向用户传递兼容性信息的更多信息，请参阅[选择版本方案](https://packaging.python.org/tutorials/distributing-packages/#choosing-a-versioning-scheme)。

如果项目代码本身需要对版本进行运行时访问，最简单的方法是将版本保存在`setup.py`代码中。如果你不想重复价值，有几种方法来管理这个。请参阅“ [单一软件包版本](https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version) ”高级主题部分。

#### [描述](https://packaging.python.org/tutorials/distributing-packages/#id44)

```
description='A sample Python project',
long_description=long_description,
```

给你的项目一个简短的描述。如果您发布项目，这些值将显示在[PyPI上](https://packaging.python.org/glossary/#term-python-package-index-pypi)。

#### [网址](https://packaging.python.org/tutorials/distributing-packages/#id45)

```
url = 'https://github.com/pypa/sampleproject' ，

```

为您的项目提供主页网址。

#### [作者](https://packaging.python.org/tutorials/distributing-packages/#id46)

```
author='The Python Packaging Authority',
author_email='pypa-dev@googlegroups.com', 

```

提供作者的详细信息。

#### [许可证](https://packaging.python.org/tutorials/distributing-packages/#id47)

```
license = 'MIT' ，

```

提供您正在使用的许可证的类型。

#### [分类](https://packaging.python.org/tutorials/distributing-packages/#id48)

```
classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
],
```

提供分类你的项目的分类列表。有关完整列表，请参阅<https://pypi.python.org/pypi?%3Aaction=list_classifiers>。

尽管分类器列表通常用于声明项目支持的Python版本，但这些信息仅用于在PyPI上搜索和浏览项目，而不用于安装项目。要真正限制可以安装项目的Python版本，请使用[python_requires](https://packaging.python.org/tutorials/distributing-packages/#python-requires) 参数。

#### [关键字](https://packaging.python.org/tutorials/distributing-packages/#id49)

```
keywords = 'sample setuptools development' ，

```

列出描述您的项目的关键字。

#### [包](https://packaging.python.org/tutorials/distributing-packages/#id50)

```
packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

```

需要列出要包含在项目中的[软件包](https://packaging.python.org/glossary/#term-import-package)。尽管可以手动列出，但可以 `setuptools.find_packages`自动找到它们。使用`exclude` 关键字参数来省略不打算发布和安装的软件包。

#### [install_requires ](https://packaging.python.org/tutorials/distributing-packages/#id51)

```
install_requires = [ 'peppercorn' ]，

```

应该使用“install_requires”来指定项目最低限度需要运行的依赖项。当项目通过[pip](https://packaging.python.org/key_projects/#pip)安装时，这是用于安装依赖关系的规范。

有关使用“install_requires”的更多信息，请参阅[install_requires vs要求文件](https://packaging.python.org/discussions/install-requires-vs-requirements/#install-requires-vs-requirements-files)。

#### [python_requires ](https://packaging.python.org/tutorials/distributing-packages/#id52)

如果您的项目只在某些Python版本上运行，请将`python_requires`参数设置 为适当的值[**PEP 440**](https://www.python.org/dev/peps/pep-0440)版本说明符字符串将阻止[ pip](https://packaging.python.org/key_projects/#pip)在其他Python版本上安装项目。例如，如果您的软件包仅适用于Python 3+，请写下：

```
python_requires = '> = 3' ，

```

如果你的软件包是用于Python 3.3或者更高版本，但是你不愿意提交Python 4的支持，那就写下：

```
python_requires = '〜= 3.3' ，

```

如果你的软件包是用于Python 2.6,2.7以及以3.3开头的所有版本的Python 3，写：

```
python_requires = '> = 2.6，！= 3.0。*，！= 3.1。*，！= 3.2。*，<4' ，

```

等等。

注意

 

对此功能的支持是相对较新的。您的项目的源代码分发和轮子（请参阅[打包您的项目](https://packaging.python.org/tutorials/distributing-packages/#packaging-your-project)）必须使用setuptools的至少版本24.2.0来[构建](https://packaging.python.org/key_projects/#setuptools)，以便 `python_requires`参数被识别并生成相应的元数据。

此外，只有9.0.0及更高版本的[pip](https://packaging.python.org/key_projects/#pip)才能识别 `python_requires`元数据。具有早期版本的pip的用户将能够在任何Python版本下载和安装项目，而不管项目的`python_requires`价值。

#### [package_data ](https://packaging.python.org/tutorials/distributing-packages/#id53)

```
package_data = { 
    'sample' ： [ 'package_data.dat' ]，
}，

```

通常需要将其他文件安装到[软件包中](https://packaging.python.org/glossary/#term-import-package)。这些文件通常是与包的实现密切相关的数据，或者是包含可能对使用该包的程序员感兴趣的文档的文本文件。这些文件被称为“包数据”。

该值必须是从软件包名称到应该复制到软件包中的相对路径名称列表的映射。路径被解释为相对于包含该包的目录。

欲了解更多信息，请参阅[包括数据文件](https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files) 从[setuptools的文档](https://setuptools.readthedocs.io/)。

#### [data_files ](https://packaging.python.org/tutorials/distributing-packages/#id54)

```
data_files = [（'my_data' ， [ 'data / data_file' ]）]，

```

虽然配置[package_data](https://packaging.python.org/tutorials/distributing-packages/#package-data)足以满足大多数需求，在某些情况下，你可能需要将数据文件*之外*你的[包](https://packaging.python.org/glossary/#term-import-package)。该`data_files`指令允许你这样做。

序列中的每个（目录，文件）对都指定安装目录和要安装的文件。如果目录是相对路径，则相对于安装前缀（Python的纯Python [发行版的](https://packaging.python.org/glossary/#term-distribution-package)sys.prefix，包含扩展模块的发行[版的](https://packaging.python.org/glossary/#term-distribution-package) sys.exec_prefix）进行解释。文件中的每个文件名都是相对于`setup.py`项目源分布顶部的脚本进行解释的。

有关更多信息，请参阅[安装其他文件](http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files)的distutils部分。

注意

 

[setuptools](https://packaging.python.org/key_projects/#setuptools)允许绝对的“data_files”路径，当从[ sdist](https://packaging.python.org/glossary/#term-source-distribution-or-sdist)安装时，pip将它们视为绝对路径。从[轮子](https://packaging.python.org/glossary/#term-wheel) 分配安装时，这是不正确的。车轮不支持绝对路径，最终被安装在相对于“站点包”的位置。有关讨论，请参阅[第92期问题轮](https://bitbucket.org/pypa/wheel/issue/92)。

#### [脚本](https://packaging.python.org/tutorials/distributing-packages/#id55)

尽管`setup()`支持[脚本](http://docs.python.org/3.4/distutils/setupscript.html#installing-scripts) 关键字来指向预先安装的脚本，但是为了实现跨平台兼容性，推荐使用[console_scripts](https://packaging.python.org/tutorials/distributing-packages/#console-scripts)入口点（见下文）。

#### [entry_points ](https://packaging.python.org/tutorials/distributing-packages/#id56)

```
entry_points = { 
  ... 
}，

```

使用这个关键字来指定你的项目提供的任何插件，这些插件可以被你的项目或者你所依赖的其他项目所定义。

欲了解更多信息，请参阅该部分[服务的动态发现和插件](https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins) 从[setuptools的](https://packaging.python.org/key_projects/#setuptools)文档。

最常用的入口点是“console_scripts”（见下文）。

##### [console_scripts ](https://packaging.python.org/tutorials/distributing-packages/#id57)

```
entry_points = { 
    'console_scripts' ： [ 
        'sample = sample：main' ，
    ]，
}，

```

使用“console_script” [入口点](https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins) 来注册脚本接口。然后，您可以让工具链处理将这些接口转换为实际脚本的工作[[2\]](https://packaging.python.org/tutorials/distributing-packages/#id31)。这些脚本将在安装[发行版时](https://packaging.python.org/glossary/#term-distribution-package)生成。

欲了解更多信息，请参阅[自动脚本创建](https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation) 从[setuptools的文档](https://setuptools.readthedocs.io/)。

### [选择版本控制方案](https://packaging.python.org/tutorials/distributing-packages/#id58)

#### [互操作性标准符合](https://packaging.python.org/tutorials/distributing-packages/#id59)

不同的Python项目可能会根据特定项目的需要使用不同的版本控制方案，但所有这些项目都需要遵守灵活性 [****](https://www.python.org/dev/peps/pep-0440#public-version-identifiers)在中指定的[**公共版本方案**](https://www.python.org/dev/peps/pep-0440#public-version-identifiers)[**PEP 440**](https://www.python.org/dev/peps/pep-0440)以在工具和类似图书馆的支持`pip` 和`setuptools`。

以下是一些符合版本号的示例：

```
1.2 。0 DEV1   ＃开发版本
1.2 。0 a1      ＃Alpha版本
1.2 。0b1      ＃Beta版本
1.2 。0 rc1     ＃发布候选版本
1.2 。0        ＃最终版本
1.2 。0. post1  ＃发布版本
15.10        ＃基于日期的版本
23           ＃序列版本

```

为了进一步适应版本编号方法的历史变化， [**PEP 440**](https://www.python.org/dev/peps/pep-0440)还定义了一个全面的技术[**版本规范化**](https://www.python.org/dev/peps/pep-0440#normalization)，将不同版本号的变体拼写映射到标准规范形式。

#### [方案选择](https://packaging.python.org/tutorials/distributing-packages/#id60)

##### [语义版本（首选）](https://packaging.python.org/tutorials/distributing-packages/#id61)

对于新项目，推荐的版本方案基于[语义版本控制](http://semver.org/)，但采用不同的方法来处理预发布版本和构建元数据。

语义版本化的实质是一个三部分MAJOR.MINOR.MAINTENANCE编号方案，其中项目作者增加：

1. MAJOR版本，当他们做不兼容的API更改，
2. MINOR版本，当他们以向后兼容的方式添加功能，和
3. MAINTENANCE版本，当他们做向后兼容的错误修复。

采用这种方法作为项目作者可以让用户使用 [**“兼容版本”**](https://www.python.org/dev/peps/pep-0440#compatible-release)说明符，其中 至少要求释放XY，但是也允许以后的版本与相匹配的MAJOR版本。`name ~=X.Y`

采用语义版本控制的Python项目应该遵守[Semantic Versioning 2.0.0规范的](http://semver.org/)第1-8条款 。

##### [基于日期的版本](https://packaging.python.org/tutorials/distributing-packages/#id62)

语义版本控制不适用于所有项目，例如那些具有常规基于时间的发布节奏的项目，以及在删除功能之前为多个版本提供警告的弃用过程。

基于日期的版本控制的一个主要优点是，可以直接告诉特定版本的基本特征集合的版本号是多少。

基于日期的项目的版本号通常采用YEAR.MONTH（例如 `12.04`，`15.10`）的形式。

##### [串行版本](https://packaging.python.org/tutorials/distributing-packages/#id63)

这是最简单的版本控制方案，由每个版本增加的单个数字组成。

虽然串行版本管理作为开发人员非常容易管理，但作为最终用户来说是最难追踪的，因为串行版本数字很少或没有关于API向后兼容性的信息。

##### [混合方案](https://packaging.python.org/tutorials/distributing-packages/#id64)

上述方案的组合是可能的。例如，一个项目可能会将基于日期的版本控制与串行版本控制相结合，以创建一个YEAR.SERIAL编号方案，该方案可以轻松传达版本的大致年龄，但不会在一年内承诺特定的版本节奏。

#### [预发行版本](https://packaging.python.org/tutorials/distributing-packages/#id65)

无论基本版本控制方案如何，给定最终版本的预发布版本可以发布为：

- 零个或多个dev版本（用“.devN”后缀表示）
- 零个或多个alpha版本（用“.aN”后缀表示）
- 零或多个beta版本（用“.bN”后缀表示）
- 零个或多个释放候选项（用“.rcN”后缀表示）

`pip` 而其他现代的Python软件包安装程序在决定安装哪个版本的依赖关系时会默认忽略预发行版本。

#### [本地版本标识符](https://packaging.python.org/tutorials/distributing-packages/#id66)

公共版本标识符旨在支持通过[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)进行分发 。Python的软件分发工具也支持a的概念[**本地版本标识符**](https://www.python.org/dev/peps/pep-0440#local-version-identifiers)，可用于标识不打算发布的本地开发版本，或者由再分发者维护的版本的修改版本。

本地版本标识符采用这种形式。例如：`<public version identifier>+<local version label>`

```
1.2 。0. dev1 + hg 。5. b11e5e6f0b0b   ＃第5个VCS自1.2.0.dev1版本
1.2 以后的通讯。1 + fedora 。4                 ＃软件包应用了下游的Fedora补丁

```

## [在“开发模式”下工作](https://packaging.python.org/tutorials/distributing-packages/#id67)

尽管不是必需的，但在您处理项目时，通常在“可编辑”或“开发”模式下将项目本地安装。这使得您的项目既可以以项目形式安装，也可以编辑。

假设你在你的项目目录的根目录，然后运行：

```
pip  安装 - e  。

```

虽然有点神秘，但是`-e`简短`--editable`，并且`.`指的是当前的工作目录，所以在一起，就意味着在可编辑模式下安装当前目录（即你的项目）。这也将安装用“install_requires”声明的任何依赖和用“console_scripts”声明的任何脚本。依赖性将以通常的不可编辑模式进行安装。

同样也希望在可编辑模式下安装一些依赖项。例如，假设您的项目需要“foo”和“bar”，但是您希望从VCS以可编辑模式安装“bar”，那么您可以构建一个需求文件，如下所示：

```
- e  。
- e  git + https ：// somerepo / bar 。git ＃egg = bar

```

第一行说安装你的项目和任何依赖项。第二行覆盖“bar”依赖项，这样它就可以从VCS而不是PyPI实现。

但是，如果要在可编辑模式下从本地目录安装“bar”，则需求文件应如下所示，本地路径位于文件顶部：

```
- e  / path / to / project / bar 
- e  。

```

否则，由于需求文件的安装顺序，依赖项将由PyPI完成。有关需求文件的更多信息，请参阅pip文档中的[需求文件](https://pip.pypa.io/en/latest/user_guide/#requirements-files)部分。有关VCS安装的更多信息，请参阅pip文档的[VCS支持](https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support)部分。

最后，如果你不想安装任何依赖关系，你可以运行：

```
pip  安装 - e  。 - 无- DEPS

```

有关更多信息，请参阅[setuptools文档](https://setuptools.readthedocs.io/)的“ [开发模式”](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)部分。

## [包装你的项目](https://packaging.python.org/tutorials/distributing-packages/#id68)

为了让您的项目可以像[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)那样从[Package Index中](https://packaging.python.org/glossary/#term-package-index)安装，您需要为您的项目创建一个[Distribution](https://packaging.python.org/glossary/#term-distribution-package)（又名“ [Package](https://packaging.python.org/glossary/#term-distribution-package) ”）。

### [来源分布](https://packaging.python.org/tutorials/distributing-packages/#id69)

最起码你应该创建一个[Source Distribution](https://packaging.python.org/glossary/#term-source-distribution-or-sdist)：

```
python setup.py sdist

```

“源代码分发”是非[构建的](https://packaging.python.org/glossary/#term-built-distribution)（即，它不是“ [构建分发”](https://packaging.python.org/glossary/#term-built-distribution)），并且需要通过点安装的构建步骤。即使发行版是纯Python（即不包含扩展名），它仍然需要构建步骤来构建安装元数据`setup.py`。

### [车轮](https://packaging.python.org/tutorials/distributing-packages/#id70)

你也应该为你的项目创建一个轮子。轮子是一个可以安装而不需要经过“构建”过程的[构建包](https://packaging.python.org/glossary/#term-built-distribution)。对于最终用户来说，安装车轮比从源代码发行版安装要快得多。

如果你的项目是纯Python（即不包含编译的扩展），并且本地支持Python 2和Python 3，那么你将创建一个叫做 [* Universal Wheel *（见下面的部分）](https://packaging.python.org/tutorials/distributing-packages/#universal-wheels)。

如果您的项目是纯Python，但本身不支持Python 2和Python 3，那么您将创建一个[“Pure Python Wheel”（请参阅下面的部分）](https://packaging.python.org/tutorials/distributing-packages/#pure-python-wheels)。

如果您的项目包含已编译的扩展名，那么您将创建所谓的[*平台轮*（请参阅下面的部分）](https://packaging.python.org/tutorials/distributing-packages/#platform-wheels)。

在为项目构建轮子之前，您需要安装 `wheel`软件包：

```
点子安装轮子

```

#### [万向轮](https://packaging.python.org/tutorials/distributing-packages/#id71)

*万向轮*是轮子是纯Python（即不包含任何编译的扩展）和支持Python 2和3这是一个可以在任何地方通过安装一个轮[点子](https://packaging.python.org/key_projects/#pip)。

建立轮子：

```
python setup.py bdist_wheel --universal

```

您也可以`--universal`在“setup.cfg”中永久设置标志（例如，参见 [sampleproject / setup.cfg](https://github.com/pypa/sampleproject/blob/master/setup.cfg)）：

```
[bdist_wheel] 
universal = 1

```

只有使用`--universal`设置，如果：

1. 您的项目在Python 2和3上运行，没有任何变化（即它不需要2to3）。
2. 您的项目没有任何C扩展名。

请注意，`bdist_wheel`如果您不恰当地使用设置，目前没有任何检查来警告。

如果您的项目具有可选的C扩展名，建议不要发布万向轮，因为pip将优先选择源安装，并防止构建扩展的可能性。

#### [纯Python轮子](https://packaging.python.org/tutorials/distributing-packages/#id72)

*纯Python车轮*不属于“通用”是轮子是纯Python（即不包含编译的扩展），但本身不支持Python 2和3。

建立轮子：

```
python  设置。py  bdist_wheel

```

bdist_wheel将检测到代码是纯Python，并且构建一个名为的轮子，以便它可以在任何Python安装中使用，并且具有与用于构建轮子的版本相同的主版本（Python 2或Python 3）。有关车轮文件命名的详细信息，请参阅[**PEP 425**](https://www.python.org/dev/peps/pep-0425)。

如果您的代码同时支持Python 2和Python 3，但是使用不同的代码（例如，使用[“2to3”](https://docs.python.org/2/library/2to3.html)），则可以运行 两次，一次使用Python 2，一次使用Python 3.这将为每个版本生成轮子。`setup.py bdist_wheel`

#### [平台车轮](https://packaging.python.org/tutorials/distributing-packages/#id73)

*平台车轮*是特定于某个平台（如Linux，macOS或Windows）的车轮，通常是由于包含已编译的扩展。

建立轮子：

```
python  设置。py  bdist_wheel

```

bdist_wheel将检测到代码不是纯Python，并构建一个名为只能在构建它的平台上使用的轮子。有关车轮文件命名的详细信息，请参阅[**PEP 425**](https://www.python.org/dev/peps/pep-0425)。

注意

 

[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)目前支持Windows，macOS和多发行版`manylinux1`ABI的平台轮子的上传。后者的细节定义在[**PEP 513**](https://www.python.org/dev/peps/pep-0513)。

## [上传你的项目的PyPI ](https://packaging.python.org/tutorials/distributing-packages/#id74)

运行命令创建发行版时，会`dist/` 在项目的根目录下创建一个新目录。这就是你会发现你的分发文件上传的地方。

注意

 

在释放主要的PyPI回购之前，您可能更喜欢使用 半定期清理的[PyPI测试网站](https://testpypi.python.org/pypi)进行培训。请参阅[使用TestPyPI](https://packaging.python.org/guides/using-testpypi/#using-test-pypi) 以了解如何设置您的配置以便使用它。

警告

 

在其他资源中，您可能会遇到使用和的引用 。**强烈建议不要**使用这些注册和上传软件包的方法，因为它可能会在某些Python版本上使用明文HTTP或未经验证的HTTPS连接，从而允许在传输过程中拦截用户名和密码。`python setup.py register``python setup.py upload`****

小费

 

PyPI上使用的reStructuredText解析器**不是**狮身人面像！此外，为了确保所有用户的安全，某些类型的URL和指令被禁止或剥离（例如指令）。**在**尝试上传您的发行版**之前**，您应该检查您提供的简短/长描述是否有效。你可以按照[pypa / readme_renderer](https://github.com/pypa/readme_renderer)工具的说明来做到这一点 。`.. raw::`****`setup.py`

### [创建一个帐户](https://packaging.python.org/tutorials/distributing-packages/#id75)

首先，您需要一个[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)用户帐户。您可以[使用PyPI网站上的表单](https://pypi.python.org/pypi?%3Aaction=register_form)创建一个帐户 。

注意

 

如果您想要避免在上传时输入您的用户名和密码，您可以`~/.pypirc`使用您的用户名和密码创建一个文件：

```
[pypi] 
用户名= <用户名> 
密码= <密码>

```

**请注意，这将以明文形式存储您的密码。**

### [上传您的分布](https://packaging.python.org/tutorials/distributing-packages/#id76)

一旦你有一个帐户，你可以上传你的分配到 [PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)使用[麻线](https://packaging.python.org/key_projects/#twine)。如果这是您第一次上传一个新项目的分配，麻线将处理注册该项目。

```
twine upload dist/*

```

注意

 

Twine允许您使用gpg预先签署分发文件：

```
gpg --detach-sign -a dist / package-1.0.1.tar.gz

```

并将gpg创建的.asc文件传递到命令行调用中：

```
twine upload dist / package-1.0.1.tar.gz package-1.0.1.tar.gz.asc

```

这可以让你放心，你只有输入你的gpg口令到gpg本身，而不是别的，因为*你*将是一个直接执行`gpg`命令的人。

------

| [[1\]](https://packaging.python.org/tutorials/distributing-packages/#id1) | 根据您的平台，这可能需要root或管理员访问权限。目前，[pip](https://packaging.python.org/key_projects/#pip)正在考虑通过[让用户安装默认行为来](https://github.com/pypa/pip/issues/1668)改变这一点。 |
| ---------------------------------------- | ---------------------------------------- |
|                                          |                                          |

| [[2\]](https://packaging.python.org/tutorials/distributing-packages/#id21) | 具体来说，“console_script”方法`.exe`在Windows上生成文件，这是因为操作系统特殊情况`.exe`文件所必需的。脚本执行功能喜欢`PATHEXT`和[**Windows的Python启动器**](https://www.python.org/dev/peps/pep-0397)允许在很多情况下使用脚本，但不是全部。 |
| ---------------------------------------- | ---------------------------------------- |
|                                          |                                          |