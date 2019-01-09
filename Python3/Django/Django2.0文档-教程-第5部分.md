# 编写你的第一个Django应用，部分5 [¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#writing-your-first-django-app-part-5)

本教程从[教程4](https://docs.djangoproject.com/en/2.0/intro/tutorial04/)停止的地方开始。我们已经构建了一个Web轮询应用程序，现在我们将为它创建一些自动化测试。

## 介绍自动化测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#introducing-automated-testing)

### 什么是自动化测试？[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#what-are-automated-tests)

测试是检查代码操作的简单例程。

测试在不同的层面上运行。一些测试可能适用于微小的细节（*特定的模型方法是否像预期的那样返回值？*），而其他测试则检查软件的整体操作（*网站上的用户输入序列是否产生期望的结果？*）。这与您之前在[教程2](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)中进行的那种测试没有什么不同，使用它[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)来检查方法的行为，或运行应用程序并输入数据以检查其行为。

*自动化*测试的不同之处在于测试工作是由系统为您完成的。您只需创建一组测试，然后在对应用程序进行更改时，可以检查代码是否仍按原计划运行，而无需执行耗时的手动测试。

### 为什么你需要创建测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#why-you-need-to-create-tests)

那么为什么要创建测试，为什么呢？

你可能会觉得自己刚刚学习Python / Django已经足够了，还有一件事要学习和做，看起来可能是压倒性的，也许是不必要的。毕竟，我们的民意调查应用程序现在非常开心，经历创建自动化测试的麻烦不会使它工作得更好。如果创建民意调查应用程序是您将要做的Django编程的最后一部分，那么确实如此，您不需要知道如何创建自动化测试。但是，如果情况并非如此，现在是学习的好时机。

#### 测试会节省你的时间[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#tests-will-save-you-time)

直到某一点，“检查它似乎工作”将是一个令人满意的测试。在更复杂的应用程序中，组件之间可能会有数十个复杂的交互。

任何这些组件的变化都会对应用程序的行为产生意想不到的后果。检查它仍然“似乎工作”可能意味着通过您的代码的功能运行20个不同的测试数据变化，以确保您没有损坏某些东西 - 不是很好地利用您的时间。

当自动化测试可以在几秒钟内完成时，尤其如此。如果出现问题，测试还可以帮助识别导致意外行为的代码。

有时，将自己从生产性的，富有创造性的编程工作中解放出来，面对写作测试这些毫无吸引力和令人沮丧的事情，特别是当你知道你的代码工作正常时，看起来很麻烦。

然而，编写测试的任务要比花费数小时手动测试应用程序或试图确定新引入问题的原因更具成效。

#### 测试不只是发现问题，他们阻止他们[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#tests-don-t-just-identify-problems-they-prevent-them)

将测试仅仅视为发展的消极方面是错误的。

没有测试，应用程序的目的或预期行为可能会相当不透明。即使它是你自己的代码，你有时会发现自己在试图弄清它到底在做什么。

测试改变了这一点; 他们从内部点亮你的代码，当出现问题时，他们会把注意力集中在出错的部分 - *即使你甚至没有意识到出错了*。

#### 测试使你的代码更具吸引力[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#tests-make-your-code-more-attractive)

您可能已经创建了一个精彩的软件，但您会发现许多其他开发人员会拒绝查看它，因为它缺少测试; 没有测试，他们不会相信它。Django最初的开发人员之一Jacob Kaplan-Moss说：“没有测试的代码是按设计划分的。”

其他开发人员希望在认真对待软件之前查看软件中的测试是您开始编写测试的另一个原因。

#### 测试帮助团队一起工作[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#tests-help-teams-work-together)

以前的观点是从单个开发人员维护应用程序的角度编写的。复杂的应用程序将由团队维护。测试保证同事不会无意中破坏你的代码（并且你不会在不知情的情况下破坏他们的代码）。如果你想以Django程序员的身份谋生，你必须善于编写测试！

## 基本测试策略[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#basic-testing-strategies)

写作考试有很多方法。

一些程序员遵循一种称为“ [测试驱动开发](https://en.wikipedia.org/wiki/Test-driven_development) ”的规则; 他们在编写代码之前实际编写测试。这看起来可能与直觉相反，但实际上它与大多数人经常会做的事情类似：他们描述一个问题，然后创建一些代码来解决它。测试驱动开发只是在Python测试用例中形式化问题。

更多的时候，测试的新手会创建一些代码，然后决定应该进行一些测试。也许早些时候写一些测试会更好，但开始之前永远不会太晚。

有时候很难确定从哪里开始编写测试。如果您已经编写了几千行Python，则选择要测试的内容可能并不容易。在这种情况下，在您下次进行更改时编写第一个测试，无论是添加新功能还是修复错误，都是有益的。

所以我们马上做。

## 编写我们的第一个测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#writing-our-first-test)

### 我们确定一个错误[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#we-identify-a-bug)

幸运的是，在一个小错误`polls`的应用为我们立即进行修复：该`Question.was_published_recently()`方法返回`True`，如果`Question`是最后一天（这是正确的）内发布，而且如果`Question`的`pub_date`领域是未来（这当然不是） 。

要检查错误是否真的存在，使用Admin创建一个问题，其日期在将来，并使用以下命令检查方法[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)：

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
```

由于未来的事情不是“最近的”，这显然是错误的。

### 创建一个测试揭露错误[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#create-a-test-to-expose-the-bug)

我们刚才在[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)测试这个问题时所做的工作正是我们在自动化测试中所能做的，所以让我们将其转化为自动化测试。

应用程序测试的常规位置在应用程序的 `tests.py`文件中; 测试系统将自动在任何名称以文件开始的文件中查找测试`test`。

将以下内容放入应用程序中的`tests.py`文件中`polls`：

polls/tests.py

```python
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

我们在这里完成的工作是创建一个[`django.test.TestCase`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)子类，其中有一个方法可以在未来创建一个`Question`实例`pub_date`。然后我们检查输出`was_published_recently()`- 哪一个 *应该*是False。

### 运行测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#running-tests)

在终端中，我们可以运行我们的测试：

```shell
$ python manage.py test polls
```

你会看到像这样的东西：

```shell
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

发生了什么是这样的：

- `python manage.py test polls`在`polls`应用程序中寻找测试
- 它找到了这个类的一个子[`django.test.TestCase`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)类
- 它创建了一个专门用于测试目的的数据库
- 它寻找测试方法 - 名称以。开始的测试方法 `test`
- 在`test_was_published_recently_with_future_question`它创建了一个`Question` 实例，其`pub_date`领域将来30天
- ...并使用该`assertIs()`方法，它发现它的 `was_published_recently()`回报`True`，尽管我们希望它回来 `False`

测试通知我们哪个测试失败，甚至发生故障的线路。

### 修复[bug¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#fixing-the-bug)

我们已经知道问题是什么：如果将来它`Question.was_published_recently()`应该返回。修改方法 ，以便只有当日期也是过去时才会返回：`False``pub_date``models.py``True`

polls/models.py

```
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

并再次运行测试：

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

在确定了一个错误之后，我们编写了一个测试，公开它并纠正了代码中的错误，以便我们的测试通过。

未来我们的应用程序可能会出现其他许多问题，但我们可以肯定，我们不会无意中重新引入此错误，因为只需运行测试就会立即发出警告。我们可以认为应用程序的这一小部分永远安全地固定下来。

### 更全面的测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#more-comprehensive-tests)

当我们在这里时，我们可以进一步确定`was_published_recently()` 方法; 事实上，如果在修复一个我们引入另一个的bug的时候，这将会令人感到非常尴尬。

将两个更多的测试方法添加到同一个类中，以更全面地测试该方法的行为：

polls/tests.py

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

而现在我们有三个测试确认它`Question.was_published_recently()` 为过去，近期和未来的问题返回明智的价值。

再一次，它`polls`是一个简单的应用程序，但是它在未来发展的复杂性以及它与其交互的任何其他代码，我们现在可以保证我们编写测试的方法将以预期的方式运行。

## 测试视图[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#test-a-view)

民意调查的应用程序是相当不加区别的：它会公布任何问题，包括`pub_date`未来领域的问题。我们应该改善这一点。`pub_date`在未来设置应该意味着该问题在当时公布，但在那之前是不可见的。

### 视图测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#a-test-for-a-view)

当我们修复上面的错误时，我们先编写了测试，然后再编写代码来修复它。事实上，这是一个简单的测试驱动开发的例子，但是我们的工作顺序并不重要。

在我们的第一个测试中，我们密切关注代码的内部行为。对于这个测试，我们想要检查它的行为，就像用户通过Web浏览器所经历的那样。

在我们尝试解决任何问题之前，让我们看看我们可以使用的工具。

### Django的测试客户端[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#the-django-test-client)

Django提供了一个测试[`Client`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.Client)来模拟用户在视图级别与代码进行交互。我们可以使用它`tests.py` 甚至可以在中使用它[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)。

我们将重新开始[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)，在那里我们需要做几件不必要的事情`tests.py`。首先是在以下方面建立测试环境[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)：

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

[`setup_test_environment()`](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#django.test.utils.setup_test_environment)安装一个模板渲染器，这将允许我们检查响应中的一些附加属性，例如 `response.context`否则将不可用。请注意，此方法*未*设置测试数据库，因此将针对现有数据库运行以下内容，并且输出可能会略有不同，具体取决于您已创建的问题。如果您的`TIME_ZONE`输入`settings.py`不正确，您可能会收到意想不到的结果 。如果您不记得提前设置，请在继续之前检查它。

接下来，我们需要导入测试客户端类（稍后，`tests.py`我们将使用[`django.test.TestCase`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)该类，该类自带客户端，因此不需要）：

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

随着这一点，我们可以要求客户为我们做一些工作：

```python
>>> # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```

### 提高我们的观点[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#improving-our-view)

民意调查列表显示了尚未发布的民意调查（即那些`pub_date`未来有民意调查的民意调查）。我们来解决这个问题。

在[教程4中，](https://docs.djangoproject.com/en/2.0/intro/tutorial04/)我们介绍了一个基于类的视图，基于[`ListView`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView)：

polls/views.py

```python
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
```

我们需要修改`get_queryset()`方法并对其进行修改，以便通过与日期比较来检查日期`timezone.now()`。首先，我们需要添加一个导入：

polls/views.py

```python
from django.utils import timezone
```

然后我们必须`get_queryset`像这样修改方法：

polls/views.py

```python
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
```

`Question.objects.filter(pub_date__lte=timezone.now())`返回一个包含`Question`s `pub_date`小于或等于 - 即早于或等于 - 的查询集`timezone.now`。

### 测试我们的新视图[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#testing-our-new-view)

现在，您可以通过启动runserver，在浏览器中加载站点，`Questions`使用过去和未来的日期创建以及检查仅列出已发布的站点来满足您的行为。您不希望*每次进行任何可能影响此操作的更改时*都这样做- 因此，让我们根据[`shell`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-shell)上述会话创建一个测试 。

将以下内容添加到`polls/tests.py`：

polls/tests.py

```python
from django.urls import reverse
```

我们将创建一个快捷方式来创建问题以及一个新的测试类：

polls/tests.py

```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
```

我们来仔细看看其中的一些。

首先是一个问题快捷功能，`create_question`在创建问题的过程中采取一些重复。

`test_no_questions`不会产生任何问题，但会检查消息：“没有民意调查可用”，并验证它是否`latest_question_list`为空。请注意，[`django.test.TestCase`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)该类提供了一些额外的断言方法。在这些例子中，我们使用 [`assertContains()`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains)和[`assertQuerysetEqual()`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerysetEqual)。

在`test_past_question`，我们创建一个问题，并验证它出现在列表中。

在`test_future_question`，我们`pub_date`在未来创建一个问题。每个测试方法都重置数据库，因此第一个问题不再存在，因此索引也不应该有任何问题。

等等。实际上，我们正在使用这些测试来讲述管理员在网站上的输入和用户体验，并检查每个州和每个系统状态的新变化，预期结果都会发布。

### 测试`DetailView`[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#testing-the-detailview)

我们的运作良好; 然而，即使未来的问题没有出现在*索引中*，用户如果知道或猜测正确的URL，仍然可以联系到他们。所以我们需要添加一个类似的约束`DetailView`：

polls/views.py

```python
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

当然，我们将增加一些测试，以检查一个`Question`，其 `pub_date`在过去可以显示，而一个具有`pub_date` 在未来是不是：

polls/tests.py

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

### 更多测试的想法[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#ideas-for-more-tests)

我们应该添加一个类似的`get_queryset`方法来`ResultsView`为该视图创建一个新的测试类。它与我们刚刚创建的非常相似; 实际上会有很多重复。

我们还可以通过其他方式改进我们的应用程序，并在此过程中添加测试。例如，`Questions`可以在网站上发布的没有`Choices`。所以，我们的意见可以检查这一点，并排除这种情况 `Questions`。我们的测试将创造一个`Question`没有`Choices`，然后测试它没有公布，以及创建一个类似`Question` *与* `Choices`和测试，它*被*发表。

也许登录管理员用户应该被允许看到未发布的 `Questions`，但不是普通的访问者。同样，无论您需要添加到软件中来完成此任务，都应该附带一个测试，无论您先编写测试，然后让代码通过测试，或先编写代码中的逻辑，然后编写测试证明给我看。

在某个时候，你一定会看看你的测试，并想知道你的代码是否正在遭受测试膨胀的困扰，这会让我们看到：

## 测试时，越多越好[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#when-testing-more-is-better)

看起来我们的测试正在失控。按照这个速度，我们测试中的代码很快就会比我们的应用程序中的代码更多，并且与我们其他代码的优雅简洁相比，重复是不美观的。

**没关系**。让他们成长。大多数情况下，你可以写一次测试，然后忘掉它。继续开发程序时，它将继续执行其有用的功能。

有时测试需要更新。假设我们修正了我们的观点，以便只`Questions`与`Choices`发布。在这种情况下，我们现有的许多测试都会失败 - *告诉我们需要修改哪些测试以使其更新*，因此在这种情况下，测试可以帮助自己照顾自己。

最糟糕的是，随着你继续发展，你可能会发现你有一些现在是多余的测试。即使这不是问题; 在测试中的冗余是一个*很好的*事情。

只要你的测试合理安排，它们就不会变得难以管理。良好的经验法则包括：

- `TestClass`为每个模型或视图分开
- 针对您要测试的每组条件的单独测试方法
- 描述其功能的测试方法名称

## 进一步测试[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#further-testing)

本教程仅介绍一些测试基础知识。你可以做的事情还有很多，还有一些非常有用的工具可以帮助你实现一些非常聪明的事情。

例如，尽管我们的测试涵盖了模型的一些内部逻辑以及视图发布信息的方式，但您可以使用“浏览器内”框架（如[Selenium）](http://seleniumhq.org/)来测试HTML在浏览器中实际呈现的方式。这些工具不仅允许您检查Django代码的行为，还可以检查JavaScript的行为。看到测试启动一个浏览器，并开始与您的网站进行交互，就好像一个人在驾驶它！Django包括[`LiveServerTestCase`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.LiveServerTestCase) 促进与Selenium等工具的集成。

如果你有一个复杂的应用程序，为了[持续集成](https://en.wikipedia.org/wiki/Continuous_integration)的目的，你可能希望自动运行测试，以便质量控制本身 - 至少部分 - 自动化。

发现应用程序未经测试的部分的好方法是检查代码覆盖率。这也有助于识别脆弱甚至死锁的代码。如果你不能测试一段代码，通常意味着应该重构或删除代码。覆盖范围将有助于识别死代码。有关详细信息，请参阅 [与coverage.py的集成](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#topics-testing-code-coverage)。

[在Django](https://docs.djangoproject.com/en/2.0/topics/testing/)中[测试](https://docs.djangoproject.com/en/2.0/topics/testing/)有关于测试的全面信息。

## 下一步是什么？[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial05/#what-s-next)

有关测试的完整详细信息，请参阅[Django中的测试](https://docs.djangoproject.com/en/2.0/topics/testing/)。

当您熟练测试Django视图时，请阅读 [本教程的第6部分](https://docs.djangoproject.com/en/2.0/intro/tutorial06/)以了解静态文件管理。