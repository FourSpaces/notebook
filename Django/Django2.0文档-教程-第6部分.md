# 编写你的第一个Django应用，部分6 [¶](https://docs.djangoproject.com/en/2.0/intro/tutorial06/#writing-your-first-django-app-part-6)

本教程从[教程5](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)停止的地方开始。我们已经构建了一个经过测试的Web轮询应用程序，现在我们将添加样式表和图像。

除了服务器生成的HTML之外，Web应用程序通常还需要提供额外的文件（例如图像，JavaScript或CSS）来呈现整个网页。在Django中，我们将这些文件称为“静态文件”。

对于小型项目，这不是什么大问题，因为您可以将静态文件保存在Web服务器可以找到的地方。但是，在更大的项目中 - 尤其是那些由多个应用程序组成的项目 - 处理每个应用程序提供的多组静态文件开始变得棘手。

那`django.contrib.staticfiles`就是：它将每个应用程序（以及您指定的任何其他位置）的静态文件收集到一个可以轻松在生产环境中提供的位置。

## 自定义*应用的*外观和感觉[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial06/#customize-your-app-s-look-and-feel)

首先，`static`在您的`polls`目录中创建一个目录。Django将在那里寻找静态文件，类似于Django如何在其中找到模板`polls/templates/`。

Django的[`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-STATICFILES_FINDERS)设置包含一个发现者列表，他们知道如何从各种来源发现静态文件。其中一个默认值是`AppDirectoriesFinder`在每个目录中寻找一个“静态”子目录 [`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)，就像`polls`我们刚刚创建的目录一样。管理站点为其静态文件使用相同的目录结构。

在`static`刚刚创建的目录中，创建另一个名为的目录，`polls`并在其中创建一个名为的文件`style.css`。换句话说，你的样式表应该在`polls/static/polls/style.css`。由于`AppDirectoriesFinder`静态文件查找程序的工作原理，您可以在Django中引用此静态文件`polls/style.css`，就像您引用模板路径一样。

静态文件命名空间

就像模板一样，我们*也许*能够将我们的静态文件直接放入`polls/static`（而不是创建另一个`polls` 子目录），但实际上这不是一个好主意。Django会选择它找到的第一个静态文件名称匹配，如果在*不同的*应用程序中有一个同名的静态文件，Django将无法区分它们。我们需要能够将Django指向正确的位置，并且最简单的方法是通过对它们进行*命名*来确保它是正确的。也就是说，通过将这些静态文件放入为应用程序本身命名的*另一个*目录中。

将下面的代码放入该样式表（`polls/static/polls/style.css`）中：

polls/static/polls/style.css

```css
li a {
    color: green;
}
```

接下来，在顶部添加以下内容`polls/templates/polls/index.html`：

polls/templates/polls/index.html

```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

该模板标签生成静态文件的绝对路径。`{% static %}`

这就是你需要为开发做的一切。重新加载 `http://localhost:8000/polls/`，你应该看到问题链接是绿色的（Django风格！）这意味着你的样式表已被正确加载。

## 添加背景图片[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial06/#adding-a-background-image)

接下来，我们将为图像创建一个子目录。`images`在`polls/static/polls/`目录中创建一个子目录。在这个目录里面，放一个叫做的图像`background.gif`。换句话说，把你的形象 `polls/static/polls/images/background.gif`。

然后，添加到您的样式表（`polls/static/polls/style.css`）中：

polls/static/polls/style.css

```css
body {
    background: white url("images/background.gif") no-repeat;
}
```

重新加载`http://localhost:8000/polls/`，你应该看到在屏幕左上角加载的背景。

警告

当然，模板标签不可用于像您的样式表这样的静态文件，这些文件不是由Django生成的。你应该总是使用**相对路径**来相互链接你的静态文件，因为这样你就可以改变（由 模板标签用来生成它的URL），而不必修改静态文件中的一堆路径。`{% static %}`[`STATIC_URL`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-STATIC_URL)[`static`](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-static)

这些是**基础知识**。有关框架中包含的设置和其他位的更多详细信息，请参阅 [静态文件howto](https://docs.djangoproject.com/en/2.0/howto/static-files/)和 [staticfiles引用](https://docs.djangoproject.com/en/2.0/ref/contrib/staticfiles/)。[部署静态文件](https://docs.djangoproject.com/en/2.0/howto/static-files/deployment/)讨论如何在真实服务器上使用静态文件。

当你熟悉静态文件时，请阅读[本教程的第7部分，](https://docs.djangoproject.com/en/2.0/intro/tutorial07/)以了解如何自定义Django的自动生成的管理站点。



# 编写你的第一个Django应用程序，第7部分[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#writing-your-first-django-app-part-7)

本教程从[教程6](https://docs.djangoproject.com/en/2.0/intro/tutorial06/)停止的地方开始。我们正在继续Web轮询应用程序，并将重点定制Django的自动生成的管理站点，我们在[教程2中](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)首次探讨了该站点。

## 自定义管理表单[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#customize-the-admin-form)

通过注册`Question`模型`admin.site.register(Question)`，Django能够构造一个默认的表单表示。通常，您需要自定义管理表单的外观和工作方式。您将通过在注册对象时告诉Django您想要的选项来实现这一点。

让我们通过重新排序编辑表单上的字段来看看它是如何工作的。将该`admin.site.register(Question)`行替换为：

polls/admin.py

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

您将遵循此模式 - 创建模型管理员类，然后将其作为第二个参数传递给`admin.site.register()`- 任何时候需要更改模型的管理选项。

上面的这个特殊变化使“出版日期”出现在“问题”字段之前：

这只有两个领域并不令人印象深刻，但对于包含数十个领域的管理员表单，选择直观的订单是一个重要的可用性细节。

说到数十个领域的表格，您可能想要将表格分成几个字段：

polls/admin.py

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```

每个元组的第一个元素 [`fieldsets`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets)是字段集的标题。以下是我们的表单现在的样子：

## 添加相关对象[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#adding-related-objects)

好的，我们有我们的问题管理页面，但是a `Question`有多个 `Choice`s，并且管理页面不显示选择。

然而。

有两种方法可以解决这个问题。首先是`Choice` 像我们一样向管理员注册`Question`。这很容易：

polls/admin.py

```python
from django.contrib import admin

from .models import Choice, Question
# ...
admin.site.register(Choice)
```

现在“选择”是Django管理员的可用选项。“添加选项”窗体如下所示：

在这种形式下，“问题”字段是包含数据库中每个问题的选择框。Django知道a [`ForeignKey`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey)应该在管理员中表现为一个`<select>`框。在我们的案例中，目前只有一个问题存在。

还要注意“问题”旁边的“添加另一个”链接。每个与`ForeignKey`另一个人有关系的对象 都可以免费获得此内容。当你点击“添加另一个”时，你会看到一个带有“添加问题”表单的弹出窗口。如果您在该窗口中添加问题并单击“保存”，Django会将问题保存到数据库中，并将其动态添加为您正在查看的“添加选项”窗体上的选定选项。

但是，实际上，这是`Choice`向系统添加对象的低效方式。如果您可以在创建`Question`对象时直接添加一堆Choices，那会更好 。让我们做到这一点。

删除模型的`register()`呼叫`Choice`。然后，编辑`Question` 注册码以读取：

polls/admin.py

```python
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

这告诉Django：“ `Choice`在`Question`管理页面上编辑对象。默认情况下，为3个选择提供足够的字段。“

加载“添加问题”页面以查看它的外观：

它的工作原理如下：相关选择有三个插槽 - 按照指定的`extra`顺序 - 每当您返回已经创建的对象的“更改”页面时，您将获得另外三个额外的插槽。

在三个当前插槽的末尾，您会看到一个“添加另一个选择”链接。如果你点击它，一个新的插槽将被添加。如果你想删除添加的插槽，你可以点击添加插槽右上角的X. 请注意，您无法删除原来的三个插槽。此图显示了一个添加的插槽：

一个小问题，但。它需要大量的屏幕空间来显示输入相关`Choice`对象的所有字段。出于这个原因，Django提供了一种显示内联相关对象的表格方式; 你只需要将`ChoiceInline`声明改为：

polls/admin.py

```python
class ChoiceInline(admin.TabularInline):
    #...
```

用那个`TabularInline`（而不是`StackedInline`），相关对象以更紧凑的基于表格的格式显示：

请注意，还有一个额外的“删除？”列，允许使用“添加另一选项”按钮和已保存的行删除添加的行。

## 自定义管理员更改列表[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#customize-the-admin-change-list)

现在问题管理页面看起来不错，让我们对“更改列表”页面进行一些调整 - 显示系统中所有问题的页面。

这里是它在这一点上的样子：

默认情况下，Django显示`str()`每个对象。但有时如果我们能够显示单个字段，它会更有帮助。要做到这一点，请使用 [`list_display`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)admin选项作为字段名称的字段元素在对象的更改列表页面上显示为列：

polls/admin.py

```
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date')
```

为了更好的衡量，我们还要包含[教程2中](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)的`was_published_recently()` 方法：

polls/admin.py

```
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
```

现在问题更改列表页面如下所示：

您可以单击列标题按照这些值进行排序 - 除了`was_published_recently`标题外，因为不支持通过任意方法的输出进行排序。另请注意，`was_published_recently`缺省情况下，列标题 是方法的名称（下划线用空格替换），并且每行包含输出的字符串表示形式。

你可以通过给这个方法`polls/models.py`提供一些属性来改善它，如下所示：

polls/models.py

```python
class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
```

有关这些方法属性的更多信息，请参阅 [`list_display`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)。

`polls/admin.py`再次编辑您的文件，并向`Question`改变列表页面添加改进 ：使用[`list_filter`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter)。将以下行添加到 `QuestionAdmin`：

```python
list_filter = ['pub_date']
```

这增加了一个“过滤器”侧边栏，让人们可以通过`pub_date`字段过滤更改列表 ：

显示的过滤器类型取决于您要过滤的字段的类型。因为`pub_date`是a [`DateTimeField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateTimeField)，Django知道给出适当的过滤选项：“任何日期”，“今天”，“过去7天”，“本月”，“今年”。

这样做很好。让我们添加一些搜索功能：

```python
search_fields = ['question_text']
```

在更改列表的顶部添加了一个搜索框。当有人输入搜索条件时，Django将搜索该`question_text`字段。您可以根据需要使用尽可能多的字段 - 尽管由于它`LIKE`在后台使用查询，因此将搜索字段的数量限制为合理的数字可以使您的数据库更轻松地进行搜索。

现在也是注意变更列表给你免费分页的好时机。默认值是每页显示100个项目。，，，，和 所有的工作在一起，就像你认为他们应该。[`Change list pagination`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page)[`searchboxes`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)[`filters`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter)[`date-hierarchies`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy)[`column-header-ordering`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

## 自定义管理员的外观和感觉[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#customize-the-admin-look-and-feel)

显然，在每个管理页面的顶部添加“Django管理”是非常荒谬的。这只是占位符文本。

不过，使用Django的模板系统很容易改变。Django管理员由Django本身支持，其接口使用Django自己的模板系统。

### 定制您的*项目*模板[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#customizing-your-project-s-templates)

`templates`在你的项目目录（包含的目录）中创建一个目录`manage.py`。模板可以存放在Django可以访问的文件系统的任何位置。（Django以你的服务器运行的任何用户身份运行。）但是，将模板保留在项目中是一个很好的约定。

打开您的设置文件（`mysite/settings.py`请记住）并[`DIRS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES-DIRS)在[`TEMPLATES`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES)设置中添加一个 选项：

mysite/settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

[`DIRS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES-DIRS)是加载Django模板时要检查的文件系统目录列表; 这是一个搜索路径。

组织模板

就像静态文件一样，我们*可以*将所有模板放在一个大模板目录中，并且它可以很好地工作。但是，属于特定应用程序的模板应放置在该应用程序的模板目录（例如`polls/templates`）中，而不是项目的（`templates`）。我们将在[可重用应用程序教程](https://docs.djangoproject.com/en/2.0/intro/reusable-apps/) 中更详细地讨论我们 *为什么*要这样做。

现在创建一个名为`admin`inside 的目录`templates`，并将该模板`admin/base_site.html`从Django自身（`django/contrib/admin/templates`）的源代码中的默认Django管理模板目录中复制到该目录中。

Django源文件在哪里？

如果您难以找到Django源文件在系统中的位置，请运行以下命令：

```shell
$ python -c "import django; print(django.__path__)"
```

然后，只需编辑该文件，并根据您的意愿替换 （包括大括号）和您自己的网站名称即可。你应该得到一段代码：`{{ site_header|default:_('Djangoadministration') }}`

```html
{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></h1>
{% endblock %}
```

我们使用这种方法来教你如何覆盖模板。在实际的项目中，您可能会使用该[`django.contrib.admin.AdminSite.site_header`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.AdminSite.site_header)属性来更轻松地进行此特定定制。

该模板文件包含许多类似于 和的文本。在和标签是Django的模板语言的一部分。Django呈现时，将评估此模板语言以生成最终的HTML页面，就像我们在[教程3中](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)看到的那样。`{% block branding %}``{{ title }}``{%``{{``admin/base_site.html`

请注意，任何Django的默认管理模板都可以被覆盖。要覆盖模板，只需执行与之相同的操作`base_site.html`- 将其从默认目录复制到您的自定义目录中，然后进行更改。

### 定制*应用程序的*模板[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#customizing-your-application-s-templates)

精明的读者会问：但如果[`DIRS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES-DIRS)默认为空，Django如何找到默认的管理模板？答案是，既然[`APP_DIRS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEMPLATES-APP_DIRS)设置为`True`，Django自动查找`templates/`每个应用程序包内的子目录，作为后备（不要忘记这 `django.contrib.admin`是一个应用程序）。

我们的投票应用程序不是很复杂，不需要自定义管理模板。但是，如果它变得更复杂并且需要修改Django标准管理模板的某些功能，修改*应用程序的*模板而不是*项目中**的*模板会更明智。这样，您可以将投票应用程序包含在任何新项目中，并确保它能找到所需的自定义模板。

有关Django如何找到其模板的更多信息，请参阅[模板加载文档](https://docs.djangoproject.com/en/2.0/topics/templates/#template-loading)。

## 自定义管理索引页面[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#customize-the-admin-index-page)

在类似的说明中，您可能想要自定义Django管理索引页面的外观。

默认情况下，它会[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)按照字母顺序显示已在管理应用程序中注册的所有应用程序。您可能需要对布局进行重大更改。毕竟，索引可能是管理员最重要的页面，应该很容易使用。

要自定义的模板是`admin/index.html`。（与`admin/base_site.html`前一节中的操作相同 - 将其从默认目录复制到您的自定义模板目录中）。编辑文件，你会看到它使用了一个名为的模板变量`app_list`。该变量包含每个已安装的Django应用程序。您可以用任何您认为最好的方式来硬编码指向特定于对象的管理页面的链接。

## 下一步是什么？[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial07/#what-s-next)

初学者教程在这里结束。同时，您可能想查看一下从[哪里开始的指南](https://docs.djangoproject.com/en/2.0/intro/whatsnext/)。

如果您熟悉Python打包并有兴趣学习如何将投票转换为“可重用应用程序”，请查看[高级教程：如何编写可重用应用程序](https://docs.djangoproject.com/en/2.0/intro/reusable-apps/)。