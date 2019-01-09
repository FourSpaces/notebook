# 编写你的第一个Django应用程序，第3部分[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#writing-your-first-django-app-part-3)

本教程从[教程2](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)停止的地方开始。我们正在继续进行Web轮询应用程序，并将重点放在创建公共接口 - “视图”上。

## 概述[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#overview)

视图是Django应用程序中网页的“类型”，通常用于特定功能并具有特定模板。例如，在博客应用程序中，您可能有以下观点：

- 博客主页 - 显示最新的几个条目。
- 输入“详细信息”页面 - 永久链接页面用于单个条目。
- 基于年份的存档页面 - 显示给定年份中所有条目的月份。
- 基于月份的存档页面 - 显示给定月份中所有日期的条目。
- 基于日期的归档页面 - 显示给定日期的所有条目。
- 评论操作 - 处理对给定条目的发布评论。

在我们的投票应用程序中，我们将拥有以下四个视图：

- 问题“索引”页面 - 显示最新的几个问题。
- 问题“详细信息”页面 - 显示问题文本，没有结果，但有投票表格。
- 问题“结果”页面 - 显示特定问题的结果。
- 投票行动 - 在特定问题中处理针对特定选择的投票。

在Django中，网页和其他内容由视图传递。每个视图都由一个简单的Python函数（或基于类的视图的方法）表示。Django将通过检查请求的URL（准确地说，域名后的URL部分）来选择一个视图。

现在，在网络上，您可能会遇到诸如“ME2 / Sites / dirmod.asp？sid =＆type = gen＆mod = Core + Pages＆gid = A6CD4967199A42D9B65B1B”等美女。你会很高兴知道Django允许我们使用比这更优雅的 *URL模式*。

URL模式只是URL的一般形式 - 例如： `/newsarchive/<year>/<month>/`。

为了从URL获得视图，Django使用了所谓的'URLconf'。URLconf将URL模式映射到视图。

本教程提供了有关使用URLconf的基本说明，您可以参考[URL调度程序](https://docs.djangoproject.com/en/2.0/topics/http/urls/)以获取更多信息。

## 写更多的意见[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#writing-more-views)

现在让我们再添加一些视图`polls/views.py`。这些观点略有不同，因为他们有一个论点：

polls/views.py

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)）
```

`polls.urls`通过添加以下[`path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)调用将这些新视图连接到模块中 ：

polls/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

看看你的浏览器，在“/ polls / 34 /”。它会运行该`detail()` 方法并显示您在URL中提供的任何ID。尝试“/ polls / 34 / results /”和“/ polls / 34 / vote /” - 这些将显示占位符结果和投票页面。

当有人从你的网站请求一个页面 - 比如“/ polls / 34 /”时，Django会加载`mysite.urls`Python模块，因为它是由[`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-ROOT_URLCONF)设置指向的 。它找到名为的变量`urlpatterns` 并按顺序遍历模式。找到匹配后`'polls/'`，它会去掉匹配的文本（`"polls/"`），并将剩余的文本 - 发送 `"34/"`到“polls.urls”URLconf以供进一步处理。在那里匹配`'<int:question_id>/'`，导致对`detail()`视图的调用如此：

```
detail(request=<HttpRequest object>, question_id=34)
```

该`question_id=34`部分来自`<int:question_id>`。使用尖括号“捕获”部分URL并将其作为关键字参数发送到视图函数。`:question_id>`字符串的一部分定义了用于标识匹配模式的名称，该`<int:`部分是一个转换器，用于确定哪些模式应匹配这部分URL路径。

没有必要添加URL cruft，如`.html`- 除非你想，在这种情况下，你可以做这样的事情：

```
path('polls/latest.html', views.index),
```

但是，不要这样做。这很愚蠢。

## 编写实际执行某些操作的视图[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#write-views-that-actually-do-something)

每个视图负责执行以下两项操作之一：返回[`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse)包含所请求页面的内容的 对象，或引发异常，如[`Http404`](https://docs.djangoproject.com/en/2.0/topics/http/views/#django.http.Http404)。其余的由你决定。

您的视图可以从数据库中读取记录，或不是。它可以使用模板系统，例如Django或第三方Python模板系统，也可以不使用。它可以生成一个PDF文件，输出XML，随时创建一个ZIP文件，任何你想要的，使用任何你想要的Python库。

Django想要的就是这个[`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse)。或者是一个例外。

因为它很方便，所以我们使用Django自己的数据库API，我们在[教程2中介绍了它](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)。`index()` 根据出版日期，这是一个新视图的刺，它显示系统中最新的5个投票问题，用逗号分隔。

polls/views.py

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

但这里有一个问题：页面的设计在视图中被硬编码。如果你想改变页面的外观，你必须编辑这个Python代码。因此，让我们使用Django的模板系统通过创建视图可以使用的模板来将设计从Python中分离出来。

首先，`templates`在您的`polls`目录中创建一个目录。Django将在那里寻找模板。

您的项目[`TEMPLATES`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES)设置描述了Django如何加载和呈现模板。默认设置文件配置`DjangoTemplates` 其[`APP_DIRS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES-APP_DIRS)选项设置为 的后端`True`。按照约定`DjangoTemplates`在每个中寻找一个“templates”子目录[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)。

在`templates`刚刚创建的目录中，创建另一个名为的目录`polls`，并在其中创建一个名为的文件 `index.html`。换句话说，你的模板应该在`polls/templates/polls/index.html`。由于`app_directories` 模板加载器的工作方式如上所述，因此您可以在Django中简单地引用该模板`polls/index.html`。

模板命名空间

现在我们*可以避免*将模板直接放入 `polls/templates`（而不是创建另一个`polls`子目录），但这实际上是一个糟糕的主意。Django会选择它找到的名称匹配的第一个模板，并且如果在*不同的*应用程序中有同名的模板，Django将无法区分它们。我们需要能够将Django指向正确的位置，并且最简单的方法是通过对它们进行*命名*来确保它是正确的。也就是说，将这些模板放在为应用程序本身命名的*另一个*目录中。

将下面的代码放在该模板中：

polls/templates/polls/index.html

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

现在让我们更新我们的`index`视图`polls/views.py`以使用模板：

polls/views.py

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

该代码加载调用的模板 `polls/index.html`并将其传递给上下文。上下文是一个将模板变量名称映射到Python对象的字典。

通过将浏览器指向“/ polls /”来加载页面，并且您应该看到一个包含[教程2中](https://docs.djangoproject.com/en/2.0/intro/tutorial02/) “What's up”问题的项目符号列表。链接指向问题的详细信息页面。

### 捷径：[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#a-shortcut-render)[`render()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.render)

加载模板，填充上下文并返回[`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse)带有渲染模板结果的对象是一个非常常见的习惯用法 。Django提供了一个捷径。这是完整的`index()`观点，重写：

polls/views.py

```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

请注意，一旦我们在所有这些视图中完成了这些操作，我们就不再需要导入， [`loader`](https://docs.djangoproject.com/en/2.0/topics/templates/#module-django.template.loader)并且[`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse)（`HttpResponse`如果您仍然拥有，和的存根方法`detail`， 您将需要保留）。`results``vote`

该[`render()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.render)函数将请求对象作为其第一个参数，将模板名称作为其第二个参数，并将字典作为其可选的第三个参数。它返回[`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse) 给定模板呈现给定上下文的对象。

## 引发404错误[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#raising-a-404-error)

现在，让我们解决问题详情视图 - 显示给定投票的问题文本的页面。这是观点：

polls/views.py

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

这里的新概念：[`Http404`](https://docs.djangoproject.com/en/2.0/topics/http/views/#django.http.Http404)如果具有所请求的ID的问题不存在，则视图引发异常。

我们将在稍后讨论可以放在该`polls/detail.html`模板中的内容，但如果您想快速获得上述示例的工作方式，则只需包含以下内容的文件：

polls/templates/polls/detail.html

```html
{{  question  }}
```

会让你现在开始。

### 捷径：[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#a-shortcut-get-object-or-404)[`get_object_or_404()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404)

这是一个非常常见的成语使用[`get()`](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.get) 和提高[`Http404`](https://docs.djangoproject.com/en/2.0/topics/http/views/#django.http.Http404)，如果对象不存在。Django提供了一个捷径。这里的`detail()`观点改写为：

polls/views.py

```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

该[`get_object_or_404()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404)函数将Django模型作为其第一个参数和任意数量的关键字参数，并将其传递给[`get()`](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.get)模型管理器的函数。[`Http404`](https://docs.djangoproject.com/en/2.0/topics/http/views/#django.http.Http404)如果对象不存在，则引发。

> 哲学

为什么我们使用助手函数[`get_object_or_404()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404) 而不是自动捕获[`ObjectDoesNotExist`](https://docs.djangoproject.com/en/2.0/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist)更高级别的 异常，或者使用模型API [`Http404`](https://docs.djangoproject.com/en/2.0/topics/http/views/#django.http.Http404)而不是 [`ObjectDoesNotExist`](https://docs.djangoproject.com/en/2.0/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist)？

因为那会将模型图层耦合到视图图层。Django最重要的设计目标之一是保持松耦合。[`django.shortcuts`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#module-django.shortcuts)模块中引入了一些受控耦合。

还有一个[`get_list_or_404()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.get_list_or_404)功能，其功能就像[`get_object_or_404()`](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404)- 除了使用[`filter()`](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.filter)而不是 [`get()`](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.get)。[`Http404`](https://docs.djangoproject.com/en/2.0/topics/http/views/#django.http.Http404)如果列表为空，则会引发 此问题。

## 使用模板系统[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#use-the-template-system)

回到`detail()`我们的投票应用程序的视图。鉴于上下文变量`question`，以下是`polls/detail.html`模板的样子：

polls/templates/polls/detail.html

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

模板系统使用点查找语法来访问变量属性。在这个例子中，首先Django在对象上进行字典查找。如果失败了，它会尝试一个属性查找 - 在这种情况下可以工作。如果属性查找失败，它会尝试列表索引查找。`{{ question.question_text }}``question`

方法调用发生在循环中： 被解释为Python代码 ，它返回一系列对象并适合在标记中使用。[`{% for%}`](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-for)`question.choice_set.all``question.choice_set.all()``Choice`[`{% for%}`](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-for)

有关[模板](https://docs.djangoproject.com/en/2.0/topics/templates/)的更多信息，请参阅[模板指南](https://docs.djangoproject.com/en/2.0/topics/templates/)。

## 删除硬编码的网址模板[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#removing-hardcoded-urls-in-templates)

请记住，当我们在`polls/index.html` 模板中编写问题链接时，链接部分硬编码如下：

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

这种硬编码，紧密耦合的方法存在的问题是，在具有大量模板的项目上更改网址变得非常具有挑战性。但是，由于您[`path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path)在`polls.urls`模块中的函数中定义了name参数，因此可以使用模板标记删除对URL配置中定义的特定URL路径的依赖：`{% url %}`

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

它的工作方式是通过查找`polls.urls`模块中指定的URL定义 。你可以看到下面定义了'detail'的URL名称的确切位置：

```
...
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
...
```

如果您想将投票详细信息视图的URL更改为其他内容，可能`polls/specifics/12/`不是在模板（或模板）中进行，而是将其更改为`polls/urls.py`：

```python
...
# added the word 'specifics'
path('specifics/<int:question_id>/', views.detail, name='detail'),
...
```

## 命名空间URL名称[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names)

该教程项目只有一个应用程序，`polls`。在真正的Django项目中，可能会有五个，十个，二十个应用程序或更多。Django如何区分它们之间的URL名称？例如，该`polls`应用程序有一个`detail` 视图，同一个项目上的一个应用程序也可以用于博客。如何让Django知道在使用模板标签时要为URL创建哪个应用视图 ？`{% url %}`

答案是将命名空间添加到您的URLconf中。在该`polls/urls.py` 文件中，继续并添加一个`app_name`以设置应用程序名称空间：

polls/urls.py

```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

```

现在`polls/index.html`从以下位置更改模板：

polls/templates/polls/index.html

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

指向命名空间的细节视图：

polls/templates/polls/index.html

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

如果您愿意编写视图，请阅读[本教程的第4部分，](https://docs.djangoproject.com/en/2.0/intro/tutorial04/)以了解简单表单处理和通用视图。