# 编写你的第一个Django应用程序，第2部分[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#writing-your-first-django-app-part-2)

本教程从[教程1](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)停止的地方开始。我们将设置数据库，创建您的第一个模型，并快速介绍Django自动生成的管理站点。

## 数据库设置[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#database-setup)

现在，开放`mysite/settings.py`。这是一个普通的Python模块，其模块级变量代表Django设置。

默认情况下，配置使用SQLite。如果你是数据库新手，或者你只是想尝试Django，这是最简单的选择。SQLite包含在Python中，所以你不需要安装其他任何东西来支持你的数据库。然而，当开始你的第一个真正的项目时，你可能想要使用像PostgreSQL这样的更具可扩展性的数据库，以避免数据库切换麻烦。

如果您希望使用其他数据库，请安装适当的[数据库绑定，](https://docs.djangoproject.com/en/2.0/topics/install/#database-installation)并在项目中更改以下键 以匹配数据库连接设置：[`DATABASES`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES) `'default'`

- [`ENGINE`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASE-ENGINE)-要么 `'django.db.backends.sqlite3'`，`'django.db.backends.postgresql'`， `'django.db.backends.mysql'`，或`'django.db.backends.oracle'`。其他后端[也可用](https://docs.djangoproject.com/en/2.0/ref/databases/#third-party-notes)。
- [`NAME`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-NAME) - 数据库的名称。如果您使用SQLite，数据库将成为您计算机上的文件; 在这种情况下，[`NAME`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-NAME) 应该是该文件的完整绝对路径，包括文件名。默认值，将把文件存储在你的项目目录中。`os.path.join(BASE_DIR, 'db.sqlite3')`

如果你不使用SQLite作为数据库，额外的设置，例如 [`USER`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USER)，[`PASSWORD`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PASSWORD)和[`HOST`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-HOST)必须加入。有关更多详细信息，请参阅参考文档[`DATABASES`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES)。

对于SQLite以外的数据库

如果你使用SQLite之外的数据库，请确保你已经创建了一个数据库。在数据库的交互式提示符下用“ ”来做到这一点。`CREATE DATABASEdatabase_name;`

还要确保提供的数据库用户`mysite/settings.py` 具有“创建数据库”权限。这允许自动创建 [测试数据库](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#the-test-database)，这将在稍后的教程中需要。

如果您使用的是SQLite，则无需事先创建任何内容 - 数据库文件将在需要时自动创建。

在编辑时`mysite/settings.py`，请设置[`TIME_ZONE`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TIME_ZONE)为您的时区。

另外，请注意[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)文件顶部的设置。它包含在此Django实例中激活的所有Django应用程序的名称。应用程序可以用于多个项目，您可以打包并分发这些应用程序以供他人在其项目中使用。

默认情况下，[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)包含以下应用程序，所有这些应用程序都附带Django：

- [`django.contrib.admin`](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#module-django.contrib.admin) - 管理网站。你会很快使用它。
- [`django.contrib.auth`](https://docs.djangoproject.com/en/2.0/topics/auth/#module-django.contrib.auth) - 一个认证系统。
- [`django.contrib.contenttypes`](https://docs.djangoproject.com/en/2.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes) - 内容类型的框架。
- [`django.contrib.sessions`](https://docs.djangoproject.com/en/2.0/topics/http/sessions/#module-django.contrib.sessions) - 会话框架。
- [`django.contrib.messages`](https://docs.djangoproject.com/en/2.0/ref/contrib/messages/#module-django.contrib.messages) - 消息传递框架。
- [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/2.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles) - 一个管理静态文件的框架。

默认情况下包含这些应用程序，以方便常见情况。

但是其中一些应用程序至少使用了一个数据库表，所以我们需要在数据库中创建表格，然后才能使用它们。为此，请运行以下命令：

```
$ python manage.py migrate
```

该[`migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)命令查看[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)设置并根据`mysite/settings.py`文件中的数据库设置以及应用程序随附的数据库迁移（稍后将介绍这些数据库迁移）创建任何必需的数据库表。您会看到每条适用的迁移消息。如果您有兴趣，请为您的数据库运行命令行客户端并输入`\dt`（PostgreSQL），（MySQL）， （SQLite）或（Oracle）以显示Django创建的表。`SHOW TABLES;``.schema``SELECT TABLE_NAME FROMUSER_TABLES;`

对于极简主义者

就像我们上面所说的那样，默认应用程序包含在常见的情况下，但不是每个人都需要它们。如果您不需要其中的任何一个或全部，请[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)在运行之前自由注释或删除相应的行 [`migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)。该[`migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)命令将仅运行应用程序的迁移 [`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)。

## 创建模型[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#creating-models)

现在我们将定义您的模型 - 实质上是您的数据库布局以及其他元数据。

哲学

模型是关于您的数据的单一，明确的真相来源。它包含您正在存储的数据的重要字段和行为。Django遵循[DRY原则](https://docs.djangoproject.com/en/2.0/misc/design-philosophies/#dry)。目标是在一个地方定义您的数据模型并自动从中推导出事物。

这包括迁移 - 与Ruby On Rails不同，例如，迁移完全从您的模型文件派生而来，本质上只是Django可以滚动更新数据库模式以符合当前模型的历史记录。

在我们简单的民意调查应用程序中，我们将创建两个模型：`Question`和`Choice`。A `Question`有一个问题和一个出版日期。A `Choice`有两个字段：选择的文本和一个票数。每个`Choice`都与一个关联`Question`。

这些概念由简单的Python类表示。编辑 `polls/models.py`文件，使其看起来像这样：

polls/models.py

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

代码很简单。每个模型都由一个子类表示[`django.db.models.Model`](https://docs.djangoproject.com/en/2.0/ref/models/instances/#django.db.models.Model)。每个模型都有许多类变量，每个变量表示模型中的数据库字段。

每个字段都由一个[`Field`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field) 类的实例表示- 例如[`CharField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField)字符字段和 [`DateTimeField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateTimeField)日期时间。这告诉Django每个字段拥有什么类型的数据。

每个[`Field`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field)实例的名称（例如 `question_text`或`pub_date`）是该字段的名称，以机器友好的格式。您将在您的Python代码中使用此值，并且您的数据库将使用它作为列名称。

您可以使用可选的第一个位置参数 [`Field`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field)来指定一个人类可读的名称。这在Django的一些内省部分中使用，并且它作为文档加倍。如果未提供此字段，则Django将使用机器可读名称。在这个例子中，我们只定义了一个人类可读的名字`Question.pub_date`。对于此模型中的所有其他字段，该字段的机器可读名称将作为其人类可读名称就足够了。

有些[`Field`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field)类需要参数。 [`CharField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField)例如，要求你给它一个 [`max_length`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField.max_length)。这不仅在数据库模式中使用，而且在验证中使用，我们很快就会看到。

A [`Field`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field)也可以有各种可选参数; 在这种情况下，我们已将[`default`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.default)值 设置`votes`为0。

最后，注意一个关系是使用定义的 [`ForeignKey`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey)。这告诉Django每一个`Choice`都与单个相关`Question`。Django支持所有常见的数据库关系：多对一，多对多和一对一。

## 激活模型[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#activating-models)

这一小部分模型代码为Django提供了大量信息。有了它，Django能够：

- 为此应用程序创建数据库模式（语句）。`CREATE TABLE`
- 创建一个用于访问`Question`和`Choice`对象的Python数据库访问API 。

但首先我们需要告诉我们的项目，该`polls`应用程序已安装。

哲学

Django应用程序是“可插入的”：您可以在多个项目中使用应用程序，并且可以分发应用程序，因为它们不必绑定到给定的Django安装。

要将该应用程序包含在我们的项目中，我们需要在设置中添加对其配置类的引用[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)。该 `PollsConfig`班是在`polls/apps.py`文件中，所以它的虚线路径`'polls.apps.PollsConfig'`。编辑该`mysite/settings.py`文件并将该虚线路径添加到该[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)设置。它看起来像这样：

mysite/settings.py

```python
INSTALLED_APPS  =  [ 
    'polls.apps.PollsConfig' ，
    'django.contrib.admin' ，
    'django.contrib.auth' ，
    'django.contrib.contenttypes' ，
    'django.contrib.sessions' ，
    'django.contrib.messages' ，
    'django.contrib.staticfiles' ，
]
```

现在Django知道包含该`polls`应用程序。让我们运行另一个命令：

```python
$ python manage.py makemigrations polls
```

您应该看到类似于以下内容的内容：

```shell
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice
```

通过运行`makemigrations`，您告诉Django您已经对模型进行了一些更改（在这种情况下，您已经创建了新模型），并且希望将这些更改存储为*迁移*。

迁移是Django如何将更改存储到模型（以及数据库模式） - 它们只是磁盘上的文件。如果你喜欢，你可以阅读你的新模型的迁移; 这是文件`polls/migrations/0001_initial.py`。别担心，Django每次创建时都不会读取它们，但是它们的设计是可以人为编辑的，以防您想要手动调整Django如何更改内容。

有一个命令可以为你运行迁移并自动管理你的数据库模式 - 这就是所谓的[`migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)，我们马上就会谈到 - 但首先，让我们看看迁移的SQL将运行什么。该 [`sqlmigrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-sqlmigrate)命令采用迁移名称并返回它们的SQL：

```
$ python manage.py sqlmigrate polls 0001
```

您应该看到类似于以下内容的内容（为便于阅读，我们已将其重新格式化）：

```
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Add field question to choice
--
ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;

COMMIT;
```

请注意以下几点：

- 确切的输出将取决于您使用的数据库。上面的例子是为PostgreSQL生成的。
- 表名是通过组合应用程序的名称（自动生成`polls`）和模型的小写名字- `question`和`choice`。（您可以覆盖此行为。）
- 主键（ID）会自动添加。（你也可以覆盖它。）
- 按照惯例，Django追加`"_id"`到外键字段名称。（是的，你也可以重写这个。）
- 外键关系通过 约束来显式化。不要担心部件; 这只是告诉PostgreSQL在事务结束之前不执行外键。`FOREIGN KEY``DEFERRABLE`
- 它针对您正在使用的数据库量身定制，因此数据库特定的字段类型（例如`auto_increment`（MySQL），`serial`（PostgreSQL）或（SQLite））会自动处理。字段名称的引用也是如此 - 例如，使用双引号或单引号。`integer primarykey autoincrement`
- 该[`sqlmigrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-sqlmigrate)命令实际上不会在数据库上运行迁移 - 它只是将其打印到屏幕上，以便您可以看到SQL Django认为需要什么。这对于检查Django将要做什么或者如果您有需要SQL脚本进行更改的数据库管理员很有用。

如果你有兴趣，你也可以跑步 ; 这可以检查项目中的任何问题，而无需进行迁移或触摸数据库。[`python manage.py check`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-check)

现在，[`migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)再次运行以在您的数据库中创建这些模型表：

```shell
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Rendering model states... DONE
  Applying polls.0001_initial... OK
```

该[`migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)命令获取所有尚未应用的迁移（Django使用数据库中的特殊表跟踪哪些应用程序被调用`django_migrations`），并根据数据库运行它们 - 本质上，将您对模型所做的更改与数据库。

迁移非常强大，随着时间的推移，您可以随时更改模型，而无需删除数据库或表并创建新的数据库 - 它专门用于实时升级数据库，而不会丢失数据。我们将在本教程的后面部分更深入地介绍它们，但现在请记住进行模型更改的三步指南：

- 改变你的模型（in `models.py`）。
- 运行以为这些更改创建迁移[`python manage.py makemigrations`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-makemigrations)
- 运行以将这些更改应用于数据库。[`python manage.py migrate`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-migrate)

之所以有单独的命令来进行和应用迁移，是因为您将迁移到您的版本控制系统并将它们与您的应用程序一起发送; 它们不仅使您的开发更容易，而且还可以被其他开发人员和生产使用。

阅读[django-admin文档](https://docs.djangoproject.com/en/2.0/ref/django-admin/)以获取该`manage.py`实用程序可以执行的操作的完整信息。

## 使用[API¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#playing-with-the-api)

现在，让我们跳入交互式Python shell并使用Django提供的免费API。要调用Python shell，请使用以下命令：

```
$ python manage.py shell
```

我们使用这个而不是简单地输入“python”，因为`manage.py` 设置了`DJANGO_SETTINGS_MODULE`环境变量，它使Django成为`mysite/settings.py`文件的Python导入路径。

一旦你在shell中，探索[数据库API](https://docs.djangoproject.com/en/2.0/topics/db/queries/)：

```python
>>> from polls.models import Question, Choice   # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

等一下。不是这个对象的有用表示。让我们来解决这个问题通过编辑模型（在文件），并加入 到两个方法和 ：`<Question: Question object(1)>``Question``polls/models.py`[`__str__()`](https://docs.djangoproject.com/en/2.0/ref/models/instances/#django.db.models.Model.__str__)`Question``Choice`

polls/models.py

```python
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

[`__str__()`](https://docs.djangoproject.com/en/2.0/ref/models/instances/#django.db.models.Model.__str__)向模型中添加方法非常重要，这不仅仅是为了您在处理交互式提示时的方便，还因为在Django的自动生成的管理中使用了对象的表示。

请注意，这些是普通的Python方法。让我们添加一个自定义方法，仅供演示：

polls/models.py

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

请注意添加和，分别引用Python的标准模块和Django的时区相关实用程序。如果您不熟悉Python中的时区处理，您可以在[时区支持文档中](https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/)了解更多信息。`importdatetime``from django.utils importtimezone`[`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime)[`django.utils.timezone`](https://docs.djangoproject.com/en/2.0/ref/utils/#module-django.utils.timezone)

通过再次运行保存这些更改并启动一个新的Python交互式shell ：`python manage.pyshell`

```python
>>> from polls.models import Question, Choice

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

有关模型关系的更多信息，请参阅[访问相关对象](https://docs.djangoproject.com/en/2.0/ref/models/relations/)。有关如何使用双下划线通过API执行字段查找的更多信息，请参阅[字段查找](https://docs.djangoproject.com/en/2.0/topics/db/queries/#field-lookups-intro)。有关数据库API的完整详细信息，请参阅我们的[数据库API参考](https://docs.djangoproject.com/en/2.0/topics/db/queries/)。

## 介绍Django [Admin¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#introducing-the-django-admin)

哲学

为您的员工或客户生成管理网站来添加，更改和删除内容是一项繁琐的工作，不需要太多创造性。出于这个原因，Django完全自动为模型创建管理界面。

Django是在新闻编辑室编写的，在“内容发布者”和“公共”网站之间有着非常明确的分离。网站管理员使用该系统添加新闻报道，事件，体育比分等，并且该内容显示在公共站点上。Django解决了为站点管理员创建统一界面以编辑内容的问题。

管理员不打算被网站访问者使用。这是给现场经理。

### 创建一个管理员用户[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#creating-an-admin-user)

首先，我们需要创建一个可以登录管理网站的用户。运行以下命令：

```
$ python manage.py createsuperuser
```

输入你想要的用户名并按回车。

```
Username: admin
```

您将被提示输入您想要的电子邮件地址：

```
Email address: admin@example.com
```

最后一步是输入您的密码。您将被要求输入两次密码，第二次作为第一次确认。

```
Password: **********
Password (again): *********
Superuser created successfully.
```

### 启动开发服务器[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#start-the-development-server)

Django管理站点默认是激活的。让我们开始开发服务器并探索它。

如果服务器未运行，则启动它如下所示：

```
$ python manage.py runserver
```

现在，打开Web浏览器并转至本地域的“/ admin /” - 例如 <http://127.0.0.1:8000/admin/>。您应该看到管理员的登录屏幕：

由于默认情况下启用了[翻译](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/)，因此根据您的浏览器设置以及Django是否具有该语言的翻译，登录屏幕可能会以您自己的语言显示。

### 进入管理网站[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#enter-the-admin-site)

现在，尝试使用您在上一步中创建的超级用户帐户登录。你应该看到Django管理索引页面：

您应该看到几种可编辑的内容：组和用户。它们[`django.contrib.auth`](https://docs.djangoproject.com/en/2.0/topics/auth/#module-django.contrib.auth)由Django 提供的身份验证框架提供。

### 请投票应用程序的管理修改[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin)

但我们的民意调查程序在哪里？它不显示在管理索引页面上。

只需要做一件事：我们需要告诉管理员`Question` 对象具有管理界面。要做到这一点，打开`polls/admin.py` 文件，并编辑它看起来像这样：

polls/admin.py

```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

### 探索免费管理功能[¶](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#explore-the-free-admin-functionality)

现在我们已经注册了`Question`，Django知道它应该显示在管理索引页面上：

点击“问题”。现在你在“更改列表”页面寻找问题。此页面显示数据库中的所有问题，并让您选择一个来更改它。我们之前创建的“What's up？”问题是：

点击“What's up？”问题来编辑它：

这里需要注意的事项：

- 表格是从`Question`模型自动生成的。
- 不同的模型字段类型（[`DateTimeField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateTimeField)， [`CharField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField)）对应于适当的HTML输入小部件。每种类型的领域都知道如何在Django管理中显示自己。
- 每个[`DateTimeField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateTimeField)获得免费的JavaScript快捷方式。日期获取“今日”快捷键和日历弹出窗口，时间显示“现在”快捷方式以及列出常用时间的便捷弹出窗口。

页面的底部给你几个选项：

- 保存 - 保存更改并返回到此类型对象的更改列表页面。
- 保存并继续编辑 - 保存更改并重新加载此对象的管理页面。
- 保存并添加另一个 - 保存更改并为此类型的对象加载一个新的空白表单。
- 删除 - 显示删除确认页面。

如果“发布日期”的值与您在[教程1中](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)创建问题的时间不匹配，则可能意味着您忘记为设置设置正确的值[`TIME_ZONE`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TIME_ZONE)。更改它，重新加载页面并检查是否显示正确的值。

点击“今日”和“现在”快捷方式更改“发布日期”。然后点击“保存并继续编辑”，然后点击右上角的“历史记录”。您将看到一个页面，其中列出了通过Django管理员对此对象所做的所有更改，以及进行更改的人员的时间戳和用户名：

当您熟悉模型API并熟悉管理网站时，请阅读[本教程的第3部分](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)，了解如何向我们的投票应用添加更多视图。