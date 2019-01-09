# 编写你的第一个Django应用程序，第4部分[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial04/#writing-your-first-django-app-part-4)

本教程从[教程3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)停止的地方开始。我们正在继续Web轮询应用程序，并将重点放在简单的表单处理和削减我们的代码。

## 写一个简单的表单[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial04/#write-a-simple-form)

让我们从上一篇教程更新我们的投票细节模板（“polls / detail.html”），以便模板包含一个HTML `<form>`元素：

polls/templates/polls/detail.html

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```

简要说明：

- 上面的模板为每个问题选项显示一个单选按钮。的 `value`每个单选按钮的是相关联的问题的选择的ID。的 `name`每个单选按钮的是`"choice"`。这意味着，当有人选择其中一个单选按钮并提交表单时，它将发送POST数据`choice=#`，其中＃是所选选项的ID。这是HTML表单的基本概念。
- 我们设置窗体的`action`到，我们设置。使用（而不是 ）非常重要，因为提交此表单的行为将会改变数据服务器端。无论何时创建一个可以改变数据服务器端的表单，都可以使用。这个提示并不是针对Django的; 这只是一个很好的Web开发实践。`{% url'polls:vote' question.id%}``method="post"``method="post"``method="get"``method="post"`
- `forloop.counter`表示[`for`](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-for)标签经过其循环的次数
- 由于我们正在创建POST表单（可能会影响修改数据），因此我们需要担心跨站点请求伪造。值得庆幸的是，您不必太担心，因为Django带有一个非常易用的系统来保护它。简而言之，所有以内部URL为目标的POST表单都应使用 模板标记。[`{%csrf_token %}`](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-csrf_token)

现在，让我们创建一个处理提交数据的Django视图，并对其进行处理。请记住，在[教程3中](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)，我们为包含以下行的民意调查应用程序创建了一个URLconf：

polls/urls.py

```python
path('<int:question_id>/vote/', views.vote, name='vote'),
```

我们还创建了该`vote()`函数的虚拟实现。我们来创建一个真正的版本。将以下内容添加到`polls/views.py`：

polls/views.py

```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

这段代码包含了本教程中尚未涉及的一些内容：

- [`request.POST`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.POST)是一个类似字典的对象，可让您通过键名访问提交的数据。在这种情况下， `request.POST['choice']`以字符串形式返回所选选项的ID。[`request.POST`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.POST)值总是字符串。

  请注意，Django还提供[`request.GET`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.GET)了以相同的方式访问GET数据 - 但我们明确地[`request.POST`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.POST)在我们的代码中使用，以确保数据仅通过POST调用进行更改。

- `request.POST['choice']`[`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError)如果 `choice`在POST数据中没有提供，将会引发。[`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError)如果`choice`没有给出，上面的代码会检查 并重新显示问题表单并显示错误消息。

- 增加选择计数后，代码将返回一个 [`HttpResponseRedirect`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponseRedirect)而不是一个正常值[`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse)。 [`HttpResponseRedirect`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponseRedirect)只有一个参数：用户将被重定向到的URL（关于这种情况下我们如何构建URL，请参阅以下几点）。

  正如上面的Python注释所指出的，您应该总是[`HttpResponseRedirect`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponseRedirect)在成功处理POST数据之后返回一个 。这个提示并不是针对Django的; 这只是一个很好的Web开发实践。

- 在这个例子[`reverse()`](https://docs.djangoproject.com/en/2.0/ref/urlresolvers/#django.urls.reverse)中，我们在[`HttpResponseRedirect`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponseRedirect)构造函数中使用了这个函数 。此功能有助于避免在视图功能中硬编码URL。它给出了我们想要传递控制权的视图的名称以及指向该视图的URL模式的可变部分。在这种情况下，使用我们在[教程3中](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)设置的URLconf ，这个[`reverse()`](https://docs.djangoproject.com/en/2.0/ref/urlresolvers/#django.urls.reverse)调用将返回一个类似的字符串

  ```
  '/polls/3/results/'
  ```

  那里的`3`价值是`question.id`。这个重定向的URL会调用`'results'`视图来显示最终页面。

如[教程3所述](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)，`request`是一个 [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest)对象。有关[`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest)对象的更多信息 ，请参阅[请求和响应文档](https://docs.djangoproject.com/en/2.0/ref/request-response/)。

有人在问题中投票后，该`vote()`视图会重定向到问题的结果页面。我们来写下这个观点：

polls/views.py

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

这`detail()`与[教程3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)的视图几乎完全相同。唯一的区别是模板名称。我们稍后将修复此冗余。

现在，创建一个`polls/results.html`模板：

polls/templates/polls/results.html

```html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

现在，请`/polls/1/`在您的浏览器中进行投票。您应该会看到每次投票时都会更新的结果页面。如果您在未选择选项的情况下提交表单，则应该看到错误消息。

注意

我们`vote()`观点的代码确实有一个小问题。它首先`selected_choice`从数据库获取对象，然后计算新值`votes`，然后将其保存回数据库。如果您的网站的两个用户*在同一时间*尝试投票，这可能会出错：相同的值，比方说42，将被检索`votes`。然后，为两个用户计算并保存43的新值，但44将是预期值。

这被称为*竞赛条件*。如果你有兴趣，你可以阅读 [使用F（）](https://docs.djangoproject.com/en/2.0/ref/models/expressions/#avoiding-race-conditions-using-f)来[避免竞争条件，](https://docs.djangoproject.com/en/2.0/ref/models/expressions/#avoiding-race-conditions-using-f)以了解如何解决这个问题。

## 使用通用视图：代码越少越好[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial04/#use-generic-views-less-code-is-better)

在`detail()`（从[教程3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)）和`results()` 意见是非常简单的-并且如上面提到的，冗余的。`index()` 显示民意调查列表的视图与此类似。

这些视图代表了基本Web开发的常见情况：根据URL中传递的参数从数据库获取数据，加载模板并返回呈现的模板。由于这很常见，Django提供了一个称为“通用视图”系统的快捷方式。

泛型视图将常见模式抽象到您甚至不需要编写Python代码来编写应用程序的地步。

我们将我们的投票应用程序转换为使用通用视图系统，以便我们可以删除一大堆我们自己的代码。我们只需采取几个步骤即可完成转换。我们会：

1. 转换URLconf。
2. 删除一些旧的不需要的视图。
3. 基于Django的通用视图引入新的视图。

详情请阅读。

为什么代码洗牌？

通常，在编写Django应用程序时，您会评估通用视图是否适合您的问题，并且从头开始使用它们，而不是在中途重构代码。但是，本教程故意将注意力集中在迄今为止“以艰难的方式编写视图”上，专注于核心概念。

在开始使用计算器之前，您应该了解基础数学。

### 修改URL配置[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial04/#amend-urlconf)

首先，打开`polls/urls.py`URLconf并像这样更改它：

polls/urls.py

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

请注意，第二个和第三个模式的路径字符串中的匹配模式的名称已从更改`<question_id>`为`<pk>`。

### 修改视图[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial04/#amend-views)

接下来，我们将删除我们的老`index`，`detail`和`results` 视图，并使用Django的通用视图代替。为此，请打开 `polls/views.py`文件并像下面这样更改它：

polls/views.py

```
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

我们在这里使用两个通用视图： [`ListView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView)和 [`DetailView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView)。这两个视图分别抽象出“显示对象列表”和“显示特定类型对象的详细页面”的概念。

- 每个通用视图都需要知道它将采取何种模式。这是使用`model`属性提供的。
- 该[`DetailView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView)通用视图预计从URL中捕获的主键值被调用 `"pk"`，所以我们已经改变`question_id`，以`pk`用于通用视图。

默认情况下，[`DetailView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView)通用视图使用名为的模板。在我们的例子中，它会使用模板。该 属性用于告诉Django使用特定的模板名称而不是自动生成的默认模板名称。我们还指定了列表视图-这确保了渲染时，结果视图和详细视图具有不同的外观，虽然他们都是一个 幕后。`<app name>/<modelname>_detail.html``"polls/question_detail.html"``template_name``template_name``results`[`DetailView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView)

同样，[`ListView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView)通用视图使用名为的默认模板; 我们使用告诉 使用我们现有的 模板。`<app name>/<modelname>_list.html``template_name`[`ListView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView)`"polls/index.html"`

在本教程的前几部分中，模板已经提供了一个包含`question`和`latest_question_list` 上下文变量的上下文。对于`DetailView`该`question`自动提供的变量-因为我们使用的Django模型（`Question`），Django的是能够确定一个适当的名称为上下文变量。但是，对于ListView，自动生成的上下文变量是`question_list`。为了覆盖这个，我们提供了这个`context_object_name` 属性，指定我们想要使用它`latest_question_list`。作为一种替代方法，您可以更改模板以匹配新的默认上下文变量 - 但只要告诉Django使用您想要的变量就容易多了。

运行服务器，并根据通用视图使用新的轮询应用程序。

有关通用视图的完整详细信息，请参阅[通用视图文档](https://docs.djangoproject.com/en/2.0/topics/class-based-views/)。

当您熟悉表单和通用视图时，请阅读[本教程的第5部分](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)以了解如何测试我们的民意调查应用程序。