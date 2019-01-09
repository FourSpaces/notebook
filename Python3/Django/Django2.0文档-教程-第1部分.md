# 编写你的第一个Django应用，第1部分 [¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#writing-your-first-django-app-part-1)

让我们通过例子学习。

在本教程中，我们将引导您完成基本投票应用程序的创建。

它将由两部分组成：

- 一个让人们查看投票结果并投票的公共网站。
- 允许您添加，更改和删除选票的后台管理网站。

我们假设你已经[安装](https://docs.djangoproject.com/en/2.0/intro/install/)了[Django](https://docs.djangoproject.com/en/2.0/intro/install/)。您可以通过在shell提示符下运行以下命令（$为前缀shell 的前缀表示）来告诉Django已安装以及哪个版本：

```
$ python -m django --version
```

如果安装了Django，您应该会看到您的安装版本。如果不是，你会得到一个错误，告诉“没有名为django的模块”。

本教程是为支持Python 3.4及更高版本的Django 2.0而编写的。如果Django版本不匹配，可以使用此页面右下角的版本切换器来引用您的Django版本的教程，或将Django更新为最新版本。如果您使用的是旧版本的Python，请检查[我可以在Django中使用哪些Python版本？](https://docs.djangoproject.com/en/2.0/faq/install/#faq-python-version-support)找到兼容版本的Django。

请参阅[如何安装Django](https://docs.djangoproject.com/en/2.0/topics/install/)以获取有关如何移除较旧版本Django并安装较新版本的建议。

从哪里获得帮助：

如果您在阅读本教程时遇到困难，请发送消息给[django用户](https://docs.djangoproject.com/en/2.0/internals/mailing-lists/#django-users-mailing-list)或[在irc.freenode.net](irc://irc.freenode.net/django)上通过[#django](irc://irc.freenode.net/django)发送消息，以便与可能帮助的其他Django用户聊天。

## 创建一个项目[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-a-project)

如果这是您第一次使用Django，那么您必须照顾一些初始设置。也就是说，您需要自动生成一些代码来建立一个Django [项目](https://docs.djangoproject.com/en/2.0/glossary/#term-project) - 一个Django实例的设置集合，包括数据库配置，Django特定的选项和特定于应用程序的设置。

从命令行，`cd`到您想要存储代码的目录，然后运行以下命令：

```
$ django-admin startproject mysite
```

这将`mysite`在您当前的目录中创建一个目录。如果它不起作用，请参阅[运行django-admin的问题](https://docs.djangoproject.com/en/2.0/faq/troubleshooting/#troubleshooting-django-admin)。

注意

您需要避免在内置Python或Django组件之后命名项目。特别是，这意味着你应该避免使用像`django`（这将与Django本身冲突）或`test`（与内置Python包冲突）的名称。

这个代码应该在哪里生活？

如果你的背景是普通的旧式PHP（没有使用现代框架），那么你可能习惯于把代码放在Web服务器的文档根目录下（在诸如此类的地方`/var/www`）。用Django，你不这样做。将任何Python代码放入Web服务器的文档根目录中并不是一个好主意，因为它有可能让人们能够通过Web查看您的代码。这对安全性不好。

将您的代码放在文档根目录**以外**的某个目录中，例如 `/home/mycode`。

我们来看看[`startproject`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-startproject)创建的内容：

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

这些文件是：

- 外部`mysite/`根目录只是您的项目的容器。它的名字与Django无关; 你可以将它重命名为任何你喜欢的东西。
- `manage.py`：一个命令行实用程序，可让您以各种方式与此Django项目进行交互。你可以阅读所有的细节`manage.py`在[Django的管理和manage.py](https://docs.djangoproject.com/en/2.0/ref/django-admin/)。
- 内部`mysite/`目录是您的项目的实际Python包。它的名字是你需要用来导入任何内容的Python包名（例如`mysite.urls`）。
- `mysite/__init__.py`：一个空文件，告诉Python这个目录应该被视为一个Python包。如果您是Python初学者，请阅读官方Python文档中[有关软件包的更多信息](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- `mysite/settings.py`：这个Django项目的设置/配置。 [Django设置](https://docs.djangoproject.com/en/2.0/topics/settings/)会告诉你所有关于设置的工作方式。
- `mysite/urls.py`：这个Django项目的URL声明; 您的Django支持的网站的“目录”。您可以在[URL调度](https://docs.djangoproject.com/en/2.0/topics/http/urls/)器中阅读更多关于URL的内容。
- `mysite/wsgi.py`：WSGI兼容的Web服务器为您的项目提供服务的入口点。有关更多详细信息，请参阅[如何使用WSGI](https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/)进行[部署](https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/)。

## 开发服务器[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#the-development-server)

让我们验证你的Django项目的作品。`mysite`如果尚未更改到外部目录，请运行以下命令：

```
$ python manage.py runserver
```

您将在命令行上看到以下输出：

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

April 24, 2018 - 15:50:53
Django version 2.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

>  注意

暂时忽略有关未应用数据库迁移的警告; 我们很快就会处理数据库。

你已经开始使用Django开发服务器，这是一个纯粹用Python编写的轻量级Web服务器。我们在Django中包含了这个功能，所以您可以快速开发，而无需处理配置生产服务器（如Apache），直到您准备好生产。

现在是值得注意的时候了：**不要**在类似于生产环境的任何情况下使用此服务器。它仅用于开发时使用。（我们的业务是制作Web框架，而不是Web服务器。）

现在服务器正在运行，请使用Web浏览器访问<http://127.0.0.1:8000/>。你会看到一个“恭喜！”页面，火箭起飞。有效！

>  更改端口

默认情况下，该[`runserver`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-runserver)命令在内部IP的端口8000上启动开发服务器。

如果您想更改服务器的端口，请将其作为命令行参数传递。例如，该命令在端口8080上启动服务器：

```
$ python manage.py runserver 8080
```

如果您想更改服务器的IP，请将其与端口一起传递。例如，要收听所有可用的公共IP（如果您正在运行Vagrant或想要在网络上的其他计算机上展示您的工作，这很有用），请使用：

```
$ python manage.py runserver 0:8000
```

**0**是**0.0.0.0**的快捷方式。有关开发服务器的完整文档可以在[`runserver`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-runserver)参考文献中找到。

自动重新加载 [`runserver`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-runserver)

开发服务器根据需要自动为每个请求重新加载Python代码。您无需重新启动服务器以使代码更改生效。但是，某些操作（如添加文件）不会触发重新启动，因此在这种情况下您必须重新启动服务器。



## 创建投票应用程序[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-the-polls-app)

既然你的环境 - 一个“项目” - 已经建立起来了，你就开始工作了。

您在Django中编写的每个应用程序都包含遵循特定约定的Python包。Django带有一个实用程序，可以自动生成应用程序的基本目录结构，因此您可以专注于编写代码而不是创建目录。

项目与应用程序

项目和应用程序有什么区别？应用程序是一种Web应用程序，它可以执行某些操作，例如Weblog系统，公共记录数据库或简单的轮询应用程序。项目是特定网站的配置和应用程序的集合。项目可以包含多个应用程序。一个应用程序可以在多个项目中。

您的应用程序可以在您的任何地方居住[Python的路径](https://docs.python.org/3/tutorial/modules.html#tut-searchpath)。在本教程中，我们将在您的`manage.py` 文件旁边创建我们的轮询应用程序，以便它可以作为其自己的顶级模块而不是子模块导入`mysite`。

要创建您的应用程序，请确保您位于相同的目录中`manage.py` 并键入此命令：

```
$ python manage.py startapp polls
```

这将创建一个目录`polls`，其布局如下所示：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

该目录结构将容纳轮询应用程序。

## 编写你的第一个视图[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#write-your-first-view)

我们来写第一个视图。打开文件`polls/views.py` 并将下面的Python代码放入其中：

polls/views.py

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

这是Django中最简单的视图。要调用视图，我们需要将它映射到一个URL - 为此，我们需要一个URLconf。

要在polls目录中创建URLconf，请创建一个名为的文件`urls.py`。你的app目录现在应该如下所示：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

在该`polls/urls.py`文件中包含以下代码：

polls/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

下一步是将URL URL指向`polls.urls`模块。在中 `mysite/urls.py`，添加一个导入`django.urls.include`并[`include()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.include)在`urlpatterns`列表中插入一个 ，这样你就可以：

mysite/urls.py

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

该[`include()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.include)函数允许引用其他URLconf。每当Django遇到时[`include()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.include)，它会截断与该点匹配的URL的任何部分，并将剩余的字符串发送到包含的URLconf以供进一步处理。

背后的想法[`include()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.include)是使插入和播放网址变得容易。由于民意测验是在他们自己的URLconf（`polls/urls.py`）中，他们可以放在“/ polls /”下，或者放在“/ fun_polls /”下，或放在“/ content / polls /”下，或者任何其他路径根下，工作。

何时使用 [`include()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.include)

`include()`包含其他网址格式时，请务必使用。 `admin.site.urls`这是唯一的例外。

您现在已将`index`视图连接到URLconf。让我们验证它的工作，运行以下命令：

```
$ python manage.py runserver
```

在您的浏览器中转到[http：// localhost：8000 / polls /](http://localhost:8000/polls/)，您应该看到“ *Hello，world* ”文本*。**你在投票指数。*“，你在`index`视图中定义的 。

该[`path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)函数传递四个参数，其中两个是必需的： `route`和`view`，以及两个可选的：`kwargs`，和`name`。在这一点上，值得回顾一下这些论据是什么。

### [path()](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)参数：route[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#path-argument-route)

`route`是一个包含URL模式的字符串。在处理请求时，Django从第一个模式开始`urlpatterns`并在列表中向下，将所请求的URL与每个模式进行比较，直到找到匹配的模式。

模式不搜索GET和POST参数或域名。例如，在请求中`https://www.example.com/myapp/`，URLconf将查找`myapp/`。在请求中`https://www.example.com/myapp/?page=3`，URLconf也将查找`myapp/`。

### [path()](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)参数：view[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#path-argument-view)

当Django找到一个匹配的模式时，它会以一个[`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest)对象作为第一个参数以及路由中的任何“捕获”值作为关键字参数来调用指定的视图函数。我们将稍微举一个例子。

### [path()](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)参数：kwargs[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#path-argument-kwargs)

任意关键字参数可以在字典中传递给目标视图。我们不打算在教程中使用Django的这个特性。

### [path()](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)参数：name[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#path-argument-name)

命名您的URL可以让您从Django其他地方明确地引用它，特别是在模板中。这个强大的功能允许您在只触摸单个文件的情况下对项目的URL模式进行全局更改。

如果您对基本请求和响应流程感到满意，请阅读 [本教程的第2部分](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)以开始使用数据库。

