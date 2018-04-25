## Django 手册



### Django 常用命令

```
# 创建一个项目，cd（例如cd exam)到你想要用来保存代码的目录
$ django-admin startproject mysite

# 在数据库中创建数据表
$ python manage.py migrate

# 运行服务器
$ python manage.py runserver 
$ python manage.py runserver 8080			# 更改端口
$ python manage.py runserver 0.0.0.0:8000	# 允许外网访问

# 创建应用
$ python manage.py startapp polls

# 更新模型修改，将这些更改记录为迁移文件
$ python manage.py makemigrations polls

# 接收迁移文件的名字，并返回它们的SQL语句
$ python manage.py sqlmigrate polls 0001

# 检查你的项目中的模型是否存在问题，而不用执行迁移或者接触数据库。
$ python manage.py check

# python manage.py createsuperuser
$
```

- migrate

  根据INSTALLED_APPS中的应用，并在mysite/settings.py 文件中的的数据库中设置必要的数据表。


----------



项目和应用之间有什么不同？ 应用是一个Web应用程序，它完成具体的事项 —— 比如一个博客系统、一个存储公共档案的数据库或者一个简单的投票应用。 项目是一个特定网站中相关配置和应用的集合。一个项目可以包含多个应用。一个应用可以运用到多个项目中去。

### 开发



#### 1、创建应用模型：

​	本质上，就是定义该模型所对应的数据库设计及其附带的元数据。

​	模型指出了数据的唯一、明确的真实来源。 它包含了正在存储的数据的基本字段和行为。 Django遵循[*DRY (Don't repeat yourself)原则*](https://yiyibooks.cn/__trs__/xx/django_182/misc/design-philosophies.html#dry)。这个原则的目标是在一个地方定义你的数据模型，并自动从它获得需要的信息.

`polls/models.py`文件如下：

```python
from django.db import models
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # 定义了一个关联，Django支持所有常见的数据库关联：多对一、多对多和一对一
    question = models.ForeignKey(Question)          
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

上面那段简短的模型代码给了Django很多信息。 有了这些代码，Django就能够自动完成以下两个功能：

- 为该应用创建数据库表（`CREATE TABLE` 语句）。
- 为`Question`对象和`Choice`对象创建一个访问数据库的python API。



#### 2、激活模型

我们首先得告诉项目：`polls`应用已经安装。 

原理:

Django 应用是可以“热插拔”的，即可以在多个项目中使用同一个应用，也可以分发这些应用， 因为它们不需要与某个特定的Django安装绑定。

再次编辑`mysite/settings.py`文件，并修改[`INSTALLED_APPS`](https://yiyibooks.cn/__trs__/xx/django_182/ref/settings.html#std:setting-INSTALLED_APPS)设置以包含字符串`'polls'`。所以它现在是这样的：

mysite/settings.py 文件

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)
```

现在Django知道要包含`polls`应用。 让我们运行另外一个命令：

```
$ python manage.py makemigrations polls
```

通过运行`makemigrations`告诉Django，已经对模型做了一些更改（在这个例子中，你创建了一个新的模型）并且会将这些更改记录为*迁移文件*。



迁移行为将会执行哪些SQL语句。[`sqlmigrate`](https://yiyibooks.cn/__trs__/xx/django_182/ref/django-admin.html#django-admin-sqlmigrate)命令接收迁移文件的名字并返回它们的SQL语句：

```
$ python manage.py sqlmigrate polls 0001
```

迁移功能非常强大，可以让你在开发过程中不断修改你的模型而不用删除数据库或者表然后再重新生成一个新的 —— 它专注于升级你的数据库且不丢失数据。

请记住实现模型变更的三个步骤：

- 修改你的模型（在`models.py`文件中）。
- 运行[`python manage.py makemigrations`](https://yiyibooks.cn/__trs__/xx/django_182/ref/django-admin.html#django-admin-makemigrations) ，为这些修改创建迁移文件
- 运行[`python manage.py migrate`](https://yiyibooks.cn/__trs__/xx/django_182/ref/django-admin.html#django-admin-migrate) ，将这些改变更新到数据库中。

将生成和应用迁移文件的命令分成几个命令来执行，是因为你可能需要将迁移文件提交到你的版本控制系统中并跟随你的应用一起变化； 这样做不仅可以使开发变得更加简单，而且对其他开发者以及上线生产非常有用。



-------



### 编写拥有实际功能的视图

每个视图函数只负责处理两件事中的一件：返回一个包含所请求页面内容的 [`HttpResponse`](https://yiyibooks.cn/__trs__/xx/django_182/ref/request-response.html#django.http.HttpResponse)对象，或抛出一个诸如[`Http404`](https://yiyibooks.cn/__trs__/xx/django_182/topics/http/views.html#django.http.Http404)异常。