​

# 编写作业步骤流程

本文档描述如何编写作业和步骤来构建，测试和部署项目目。在您的CircleCI授权的存储库分支中存在一个`.circleci/config.yml`文件表示您要使用2.0基础架构。

​	如果您已经有一个CircleCI 1.0配置，该`config.yml`文件允许您在单独的分支上测试2.0版本，使旧`circle.yml`样式中的任何现有配置不受影响，并且在不包含的分支中的CircleCI 1.0基础架构上运行`.circleci/config.yml`。

​	您可以`config.yml`在我们的[完整示例中](https://circleci.com/docs/2.0/configuration-reference/#full-example)看到一个完整的。

------

## Table of Contents

- [**version**](https://circleci.com/docs/2.0/configuration-reference/#version)
- [**jobs**](https://circleci.com/docs/2.0/configuration-reference/#jobs)
  - [**build**](https://circleci.com/docs/2.0/configuration-reference/#build)
    - [**docker** | **machine** (*executor*)](https://circleci.com/docs/2.0/configuration-reference/#docker--machine-executor)
    - [**branches**](https://circleci.com/docs/2.0/configuration-reference/#branches)
    - [**resource_class**](https://circleci.com/docs/2.0/configuration-reference/#resource_class)
    - [**steps**](https://circleci.com/docs/2.0/configuration-reference/#steps)
      - [**run**](https://circleci.com/docs/2.0/configuration-reference/#run)
      - [*Default shell options*](https://circleci.com/docs/2.0/configuration-reference/#default-shell-options)
      - [*Background commands*](https://circleci.com/docs/2.0/configuration-reference/#background-commands)
      - [*Shorthand syntax*](https://circleci.com/docs/2.0/configuration-reference/#shorthand-syntax)
      - [The `when` Attribute](https://circleci.com/docs/2.0/configuration-reference/#the-when-attribute)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example)
      - [**checkout**](https://circleci.com/docs/2.0/configuration-reference/#checkout)
      - [**save_cache**](https://circleci.com/docs/2.0/configuration-reference/#save_cache)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-1)
      - [**restore_cache**](https://circleci.com/docs/2.0/configuration-reference/#restore_cache)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-2)
      - [**deploy**](https://circleci.com/docs/2.0/configuration-reference/#deploy)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-3)
      - [**store_artifacts**](https://circleci.com/docs/2.0/configuration-reference/#store_artifacts)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-4)
      - [**store_test_results**](https://circleci.com/docs/2.0/configuration-reference/#store_test_results)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-5)
      - [**persist_to_workspace**](https://circleci.com/docs/2.0/configuration-reference/#persist_to_workspace)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-6)
      - [**attach_workspace**](https://circleci.com/docs/2.0/configuration-reference/#attach_workspace)
        - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-7)
      - [**add_ssh_keys**](https://circleci.com/docs/2.0/configuration-reference/#add_ssh_keys)
- [**workflows**](https://circleci.com/docs/2.0/configuration-reference/#workflows)
  - [**version**](https://circleci.com/docs/2.0/configuration-reference/#version-1)
  - [**jobs**](https://circleci.com/docs/2.0/configuration-reference/#jobs-1)
    - [**build**](https://circleci.com/docs/2.0/configuration-reference/#build-1)
      - [**requires**](https://circleci.com/docs/2.0/configuration-reference/#requires)
      - [**contexts**](https://circleci.com/docs/2.0/configuration-reference/#contexts)
      - [**type**](https://circleci.com/docs/2.0/configuration-reference/#type)
      - [**filters**](https://circleci.com/docs/2.0/configuration-reference/#filters)
        - [**branches**](https://circleci.com/docs/2.0/configuration-reference/#branches-1)
        - [**tags**](https://circleci.com/docs/2.0/configuration-reference/#tags)
      - [*Example*](https://circleci.com/docs/2.0/configuration-reference/#example-8)

------

## **version**

| Key     | Required ／必须 | Type   | Description /描述 |
| ------- | ------------ | ------ | --------------- |
| version | Y            | String | 应该为 `2`         |

 `version`   字段 主要用于发出废止或破坏更改的警告。

## **jobs** ／作业

每个作业都来源于 `jobs` 列表中 的项目

### **build**

build 作业是默认的作业。 如果不使用工作流程，则必须构建build作业 。

如果使用工作流程，则名为 build 的作业就为可选的，有关详细信息，请参阅[工作流【Workflows】](https://circleci.com/docs/2.0/workflows/) 文档。

每个作业由作为key的作业名称 与 作为value 的map  构成，名称在当前 jobs列表应该是唯一的。

Value map 具有以下属性：

| Key               | Required | Type    | Description                              |
| ----------------- | -------- | ------- | ---------------------------------------- |
| docker            | Y (1)    | List    | [docker executor](https://circleci.com/docs/2.0/configuration-reference/#docker)的选项 |
| machine           | Y (1)    | Map     | [machine executor](https://circleci.com/docs/2.0/configuration-reference/#machine)的选项 |
| shell             | N        | String  | Shell 在所有步骤中用于执行命令.每个步骤都可以被shell覆盖 (默认: 查看 [Default Shell Options](https://circleci.com/docs/2.0/configuration-reference/#default-shell-options)) |
| steps             | Y        | List    | 要执行的[steps【步骤】](https://circleci.com/docs/2.0/configuration-reference/#steps) 列表 |
| working_directory | N        | String  | 运行步骤的目录 (默认值: `~/project`. `project` 是一个字符串, 而不是项目的名称.) 你还可以将目录与 `$CIRCLE_WORKING_DIRECTORY` 环境变量 |
| parallelism       | N        | Integer | 运行作业的并行实例数 (默认值: 1)                      |
| environment       | N        | Map     | 环境变量名称和贵重物品的地图 (注意：这些将覆盖您在CircleCI Web界面中设置的任何环境变量). |
| branches          | N        | Map     | 定义一个map的白名单／黑名单规则，用于执行工作流外的特定分支的单个作业。(默认: 全部列入白名单). 请参阅 [Workflows【工作流程】](https://circleci.com/docs/2.0/configuration-reference/#workflows) 配置执行工作流中的作业分支 |
| resource_class    | N        | String  | 分配给作业中单位容器的CPU和RAM值. (注意:  注意：仅适用`docker`于付费帐户的密钥，并在将来的定价更新中可能会更改。 |

(1) 标注的几项属性中指定一个设置，设置多个是一个错误 .

如果`parallelism`设置为N> 1，则N个独立执行者将被设置，并且它们将并行执行该作业的步骤。某些并行性感知步骤可以选择不采用并行性，只能在单个执行器上运行（例如[`deploy`步骤](https://circleci.com/docs/2.0/configuration-reference/#deploy)）。详细了解[并行作业](https://circleci.com/docs/2.0/parallelism-faster-jobs/)。

`working_directory` 如果不存在，将自动创建。

Example:

```
jobs:
  build:
    docker:
      - image: buildpack-deps:trusty
    environment:
      - FOO: "bar"
    parallelism: 3
    resource_class: large
    working_directory: ~/my-app
    branches:
      only:
        - master
        - /rc-.*/
    steps:
      - run: make test
      - run: make
```

#### **docker** | **machine** (*executor*)

 “executor” 大致是“a place where steps occur”. 

CircleCI 2.0 只需要通过启动一次Docker 容器来构建必要的环境，或者使用完整的虚拟机。详情了解  [different executors【不同的执行者】](https://circleci.com/docs/2.0/executor-types/).

#### `docker`

Configured by `docker` key which takes a list of maps:

`docker` key 的配置，map 列表

| Key         | Required | Type           | Description                              |
| ----------- | -------- | -------------- | ---------------------------------------- |
| image       | Y        | String         | 要使用的Docker镜像名称                           |
| entrypoint  | N        | String or List |                                          |
| command     | N        | String or List | The command used as pid 1 (or args for entrypoint) when launching the container |
| user        | N        | String         | Which user to run the command as         |
| environment | N        | Map            | A map of environment variable names and values |
| auth        | N        | Map            | Authentication info for private images   |

The first `image` listed in the file defines the primary container image where all steps will run.

`entrypoint` overrides default entrypoint from Dockerfile.

`command` will be used as arguments to image entrypoint (if specified in Dockerfile) or as executable (if no entrypoint is provided here or in the Dockerfile).

For [primary container](https://circleci.com/docs/2.0/glossary/#primary-container) (listed first in the list) if no `command` is specified then `command` and image entrypoint will be ignored, to avoid errors caused by the entrypoint executable consuming significant resources or exiting prematurely. At this time all `steps` run in the primary container only.

The `environment` settings apply to all commands run in this executor, not just the initial `command`. The `environment` here has higher precedence over setting it in the job map above.

You can specify image versions using tags or digest. You can use any public images from any public Docker registry (defaults to Docker Hub). Learn more about [specifying images](https://circleci.com/docs/2.0/executor-types).

Example:

```
jobs:
  build:
    docker:
      - image: buildpack-deps:trusty # primary container
        environment:
          ENV: CI

      - image: mongo:2.6.8
        command: [--smallfiles]

      - image: postgres:9.4.1
        environment:
          POSTGRES_USER: root

      - image: redis@sha256:54057dd7e125ca41afe526a877e8bd35ec2cdd33b9217e022ed37bdcf7d09673

```

If you are using a private image, you can specify the username/password in the `auth` field. To protect the password, you can set it as a project setting which you reference here:

```
jobs:
  build:
    docker:
      - image: acme-private/private-image:321
        auth:
          username: mydockerhub-user  # can specify string literal values
          password: $DOCKERHUB_PASSWORD  # or project UI env-var reference

```

#### **machine**

The usage of the [machine executor](https://circleci.com/docs/2.0/executor-types) is configured by using the `machine` key, which takes a map:

| Key     | Required | Type    | Description                              |
| ------- | -------- | ------- | ---------------------------------------- |
| enabled | N        | Boolean | This must be true in order to enable the `machine` executor. Is required if no other value is specified |
| image   | N        | String  | The image to use (default: `circleci/classic:latest`) |

As a shorthand, you can set the `machine` key to `true`.

Example:

```
jobs:
  build:
    machine:
      enabled: true

# or just

jobs:
  build:
    machine: true

```

CircleCI supports multiple machine images that can be specified in `image` field:

- `circleci/classic:latest` (default) - an Ubuntu version `14.04` image that includes Docker version `17.03.0-ce` along with common language tools found in CircleCI 1.0 build image. The `latest` channel provides the latest tested images, changes to the channel are announced at least a week in advance.
- `circleci/classic:edge` - an Ubuntu version `14.04` image with Docker version `17.06.0-ce` along with common language tools found in CircleCI 1.0 build image. The `edge` channel provides release candidates that will eventually be promoted to `classic:latest`.

So you can set the following to use an Ubuntu version `14.04` image with Docker `17.06.0-ce`:

```
jobs:
  build:
    machine:
      image: circleci/classic:edge

```

#### **branches**

Defines rules for whitelisting/blacklisting execution of some branches if Workflows are **not** configured. If you are using Workflows, job-level branches will be ignored and must be configured in the Workflows section of your ‘config.yml’ file. See the [workflows](https://circleci.com/docs/2.0/configuration-reference/#workflows) section for details. The job-level `branch` key takes a map:

| Key    | Required | Type | Description                              |
| ------ | -------- | ---- | ---------------------------------------- |
| only   | N        | List | List of branches that only will be executed |
| ignore | N        | List | List of branches to ignore               |

Both `only` and `ignore` lists can have full names and regular expressions. For example:

```
branches:
  only:
    - master
    - /rc-.*/

```

In this case only “master” branch and branches matching regex “rc-.*” will be executed.

```
branches:
  ignore:
    - develop
    - /feature-.*/

```

In this example all the branches will be executed except “develop” and branches matching regex “feature-.*”.

If both `ignore` and `only` are present in config, only `ignore` will be taken into account.

A job that was not executed due to configured rules will show up in the list of jobs in UI, but will be marked as skipped.

#### **resource_class**

It is possible to configure CPU and RAM resources for each job as described in the following table. If `resource_class` is not specified or an invalid class is specified, the default `resource_class: medium` will be used. The `resource_class` key is currently only available for use with the `docker` executor. Paid accounts may request this feature from their Customer Success Manager, non-paid users may request to get started by sending email to support@circleci.com.

| Class   | CPU  | RAM  |
| ------- | ---- | ---- |
| small   | 1.0  | 2GB  |
| medium  | 2.0  | 4GB  |
| medium+ | 3.0  | 6GB  |
| large   | 4.0  | 8GB  |
| xlarge  | 8.0  | 16GB |

#### **steps**

The `steps` setting in a job should be a list of single key/value pairs, the key of which indicates the step type. The value may be either a configuration map or a string (depending on what that type of step requires). For example, using a map:

```
jobs:
  build:
    working_directory: ~/canary-python
    environment:
      - FOO: "bar"
    steps:
      - run:
          name: Running tests
          command: make test

```

Here `run` is a step type. The `name` attribute is used by the UI for display purposes. The `command` attribute is specific for `run` step and defines command to execute.

Some steps may implement a shorthand semantic. For example, `run` may be also be called like this:

```
jobs:
  build:
    steps:
      - run: make test

```

In its short form, the `run` step allows us to directly specify which `command` to execute as a string value. In this case step itself provides default suitable values for other attributes (`name` here will have the same value as `command`, for example).

Another shorthand, which is possible for some steps, is to simply use the step name as a string instead of a key/value pair:

```
jobs:
  build:
    steps:
      - checkout

```

In this case, the `checkout` step will checkout project source code into the job’s [`working_directory`](https://circleci.com/docs/2.0/configuration-reference/#jobs).

In general all steps can be describe as:

| Key         | Required | Type          | Description                              |
| ----------- | -------- | ------------- | ---------------------------------------- |
| <step_type> | Y        | Map or String | A configuration map for the step or some string whose semantics are defined by the step. |

Each built-in step is described in detail below.

##### **run**

Used for invoking all command-line programs, taking either a map of configuration values, or, when called in its short-form, a string that will be used as both the `command` and `name`. Run commands are executed using non-login shells by default, so you must explicitly source any dotfiles as part of the command.

| Key               | Required | Type    | Description                              |
| ----------------- | -------- | ------- | ---------------------------------------- |
| command           | Y        | String  | Command to run via the shell             |
| name              | N        | String  | Title of the step to be shown in the CircleCI UI (default: full `command`) |
| shell             | N        | String  | Shell to use for execution command (default: See [Default Shell Options](https://circleci.com/docs/2.0/configuration-reference/#default-shell-options)) |
| environment       | N        | Map     | Additional environmental variables, locally scoped to command |
| background        | N        | Boolean | Whether or not this step should run in the background (default: false) |
| working_directory | N        | String  | In which directory to run this step (default: [`working_directory`](https://circleci.com/docs/2.0/configuration-reference/#jobs) of the job) |
| no_output_timeout | N        | String  | Elapsed time the command can run without output. The string is a decimal with unit suffix, such as “20m”, “1.25h”, “5s” (default: 10 minutes) |
| when              | N        | String  | [Specify when to enable or disable the step](https://circleci.com/docs/2.0/configuration-reference/#the-when-attribute). Takes the following values: `always`, `on_success`, `on_fail` (default: `on_success`) |

Each `run` declaration represents a new shell. It’s possible to specify a multi-line `command`, each line of which will be run in the same shell:

```
- run:
    command: |
      echo Running test
      mkdir -p /tmp/test-results
      make test

```

##### *Default shell options*

Our default `shell` has a few options enabled by default:

`-e`

> Exit immediately if a pipeline (which may consist of a single simple command), a subshell command enclosed in parentheses, or one of the commands executed as part of a command list enclosed by braces exits with a non-zero status.

So if in the previous example `mkdir` failed to create a directory and returned a non-zero status, then command execution would be terminated, and the whole step would be marked as failed. If you desire the opposite behaviour, you need to add `set +e` in your `command` or override the default `shell` in your configuration map of `run`. For example:

```
- run:
    command: |
      echo Running test
      set +e
      mkdir -p /tmp/test-results
      make test

- run:
    shell: /bin/sh
    command: |
      echo Running test
      mkdir -p /tmp/test-results
      make test

```

`-o`

> If pipefail is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. The shell waits for all commands in the pipeline to terminate before returning a value.

For example:

```
- run: make test | tee test-output.log

```

If `make test` fails, the `-o pipefail` option will cause the whole step to fail. Without `-o pipefail`, the step will always run successfully because the result of the whole pipeline is determined by the last command (`tee test-output.log`), which will always return a zero status.

Note that even if `make test` fails the rest of pipeline will be executed.

If you want to avoid this behaviour, you can specify `set +o pipefail` in the command or override the whole `shell` (see example above).

In general, we recommend using the default options (`-eo pipefail`) because they show errors in intermediate commands and simplify debugging job failures. For convenience, the UI displays the used shell and all active options for each `run` step.

##### *Background commands*

The `background` attribute allows for executing commands in the background. In this case, job execution will immediately proceed to the next step rather than waiting for the command to return. While debugging background commands is more difficult, running commands in the background might be necessary in some cases. For instance, to run Selenium tests you may need to have X virtual framebuffer running:

```
- run:
    name: Running X virtual framebuffer
    command: Xvfb :99 -screen 0 1280x1024x24
    background: true

- run: make test

```

##### *Shorthand syntax*

`run` has a very convenient shorthand syntax:

```
- run: make test

# shorthanded command can also have multiple lines
- run: |
    mkdir -p /tmp/test-results
    make test

```

In this case, `command` and `name` become the string value of `run`, and the rest of the config map for that `run` have their default values.

##### The `when` Attribute

By default, CircleCI will execute job steps one at a time, in the order that they are defined in `config.yml`, until a step fails (returns a non-zero exit code). After a command fails, no further job steps will be executed.

Adding the `when` attribute to a job step allows you to override this default behaviour, and selectively run or skip steps depending on the status of the job.

The default value of `on_success` means that the step will run only if all of the previous steps have been successful (returned exit code 0).

A value of `always` means that the step will run regardless of the exit status of previous steps. This is useful if you have a task that you want to run regardless of whether the previous steps are successful or not. For example, you might have a job step that needs to upload logs or code-coverage data somewhere.

A value of `on_fail` means that the step will run only if one of the preceding steps has failed (returns a non-zero exit code). It is common to use `on_fail` if you want to store some diagnostic data to help debug test failures, or to run custom notifications about the failure, such as sending emails or triggering alerts in chatrooms.

##### *Example*

```
- run:
    name: Testing application
    command: make test
    shell: /bin/bash
    working_directory: ~/my-app
    no_output_timeout: 30m
    environment:
      FOO: "bar"

- run: echo 127.0.0.1 devhost | sudo tee -a /etc/hosts

- run: |
    sudo -u root createuser -h localhost --superuser ubuntu &&
    sudo createdb -h localhost test_db

- run:
    name: Upload Failed Tests
    command: curl --data fail_tests.log http://example.com/error_logs
    when: on_fail


```

##### **checkout**

Special step used to check out source code to the configured `path` (defaults to the `working_directory`).

| Key  | Required | Type   | Description                              |
| ---- | -------- | ------ | ---------------------------------------- |
| path | N        | String | Checkout directory (default: job’s [`working_directory`](https://circleci.com/docs/2.0/configuration-reference/#jobs)) |

If `path` already exists and is:

- a git repo - step will not clone whole repo, instead will pull origin
- NOT a git repo - step will fail.

In the case of `checkout`, the step type is just a string with no additional attributes:

```
- checkout

```

##### **save_cache**

Generates and stores a cache of a file or directory of files such as dependencies or source code in our object storage. Later jobs can [restore this cache](https://circleci.com/docs/2.0/configuration-reference/#restore_cache). Learn more in [the caching documentation](https://circleci.com/docs/2.0/caching/).

| Key   | Required | Type   | Description                              |
| ----- | -------- | ------ | ---------------------------------------- |
| paths | Y        | List   | List of directories which should be added to the cache |
| key   | Y        | String | Unique identifier for this cache         |
| when  | N        | String | [Specify when to enable or disable the step](https://circleci.com/docs/2.0/configuration-reference/#the-when-attribute). Takes the following values: `always`, `on_success`, `on_fail` (default: `on_success`) |

The cache for a specific `key` is immutable and cannot be changed once written. NOTE: *If the cache for the given key already exists it won’t be modified, and job execution will proceed to the next step.*

When storing a new cache, the `key` value may contain special templated values for your convenience:

| Template                          | Description                              |
| --------------------------------- | ---------------------------------------- |
| `{{ .Branch }}`                   | The VCS branch currently being built.    |
| `{{ .BuildNum }}`                 | The CircleCI build number for this build. |
| `{{ .Revision }}`                 | The VCS revision currently being built.  |
| `{{ .CheckoutKey }}`              | The SSH key used to checkout the repo.   |
| `{{ .Environment.variableName }}` | The environment variable `variableName`, supports any environment variable supplied by CircleCI, **not** any arbitrary environment variable. |
| `{{ checksum "filename" }}`       | A base64 encoded SHA256 hash of the given filename’s contents. This should be a file committed in your repo. Good candidates are dependency manifests, such as `package.json`, `pom.xml` or `project.clj`. It’s important that this file does not change between `restore_cache` and `save_cache`, otherwise the cache will be saved under a cache key different than the one used at `restore_cache` time. |
| `{{ epoch }}`                     | The current time in seconds since the unix epoch. |

During step execution, the templates above will be replaced by runtime values and use the resultant string as the `key`.

Template examples:

- `myapp-{{ checksum "package.json" }}` - cache will be regenerated every time something is changed in `package.json` file, different branches of this project will generate the same cache key.
- `myapp-{{ .Branch }}-{{ checksum "package.json" }}` - same as the previous one, but each branch will generate separate cache
- `myapp-{{ epoch }}` - every run of a job will generate a separate cache

While choosing suitable templates for your cache `key`, keep in mind that cache saving is not a free operation, because it will take some time to upload the cache to our storage. So it make sense to have a `key` that generates a new cache only if something actually changed and avoid generating a new one every run of a job.

**Tip:** Given the immutability of caches, it might be helpful to start all your cache keys with a version prefix `v1-...`. That way you will be able to regenerate all your caches just by incrementing the version in this prefix.

###### *Example*

```
- save_cache:
    key: v1-myapp-{{ checksum "project.clj" }}
    paths:
      - /home/ubuntu/.m2

```

##### **restore_cache**

Restores a previously saved cache based on a `key`. Cache needs to have been saved first for this key using [`save_cache` step](https://circleci.com/docs/2.0/configuration-reference/#save_cache). Learn more in [the caching documentation](https://circleci.com/docs/2.0/caching/).

| Key  | Required | Type   | Description                              |
| ---- | -------- | ------ | ---------------------------------------- |
| key  | Y (1)    | String | Single cache key to restore              |
| keys | Y (1)    | List   | List of cache keys to lookup for a cache to restore. Only first existing key will be restored. |

(1) at least one attribute has to be present. If `key` and `keys` are both given, `key` will be checked first, and then `keys`.

A key is searched against existing keys as a prefix.

NOTE: *When there are multiple matches, the \**most recent match** will be used, even if there is a more precise match.*

For example:

```
steps:
  - save_cache:
      key: v1-myapp-cache
      paths:
        - ~/d1

  - save_cache:
      key: v1-myapp-cache-new
      paths:
        - ~/d2

  - run: rm -f ~/d1 ~/d2

  - restore_cache:
      key: v1-myapp-cache

```

In this case cache `v1-myapp-cache-new` will be restored because it’s the most recent match with `v1-myapp-cache`prefix even if the first key (`v1-myapp-cache`) has exact match.

For more information on key formatting, see the `key` section of [`save_cache` step](https://circleci.com/docs/2.0/configuration-reference/#save_cache).

When CircleCI encounters a list of `keys`, the cache will be restored from the first one matching an existing cache. Most probably you would want to have a more specific key to be first (for example, cache for exact version of `package.json` file) and more generic keys after (for example, any cache for this project). If no key has a cache that exists, the step will be skipped with a warning.

A path is not required here because the cache will be restored to the location from which it was originally saved.

###### *Example*

```
- restore_cache:
    keys:
      - v1-myapp-{{ checksum "project.clj" }}
      # if cache for exact version of `project.clj` is not present then load any most recent one
      - v1-myapp-

# ... Steps building and testing your application ...

# cache will be saved only once for each version of `project.clj`
- save_cache:
    key: v1-myapp-{{ checksum "project.clj" }}
    paths:
      - /foo

```

##### **deploy**

Special step for deploying artifacts.

`deploy` uses the same configuration map and semantics as [`run`](https://circleci.com/docs/2.0/configuration-reference/#run) step. Jobs may have more than one `deploy` step.

In general `deploy` step behaves just like `run` with one exception - in a job with `parallelism`, the `deploy` step will only be executed by node #0 and only if all nodes succeed. Nodes other than #0 will skip this step.

###### *Example*

```
- deploy:
    command: |
      if [ "${CIRCLE_BRANCH}" == "master" ]; then
        ansible-playbook site.yml
      fi

```

##### **store_artifacts**

Step to store artifacts (for example logs, binaries, etc) to be available in the web app or through the API. See the[Uploading Artifacts](https://circleci.com/docs/2.0/artifacts/) document for more information.

| Key         | Required | Type   | Description                              |
| ----------- | -------- | ------ | ---------------------------------------- |
| path        | Y        | String | Directory in the primary container to save as job artifacts |
| destination | N        | String | Prefix added to the artifact paths in the artifacts API (default: the directory of the file specified in `path`) |

There can be multiple `store_artifacts` steps in a job. Using a unique prefix for each step prevents them from overwriting files.

###### *Example*

```
- store_artifacts:
    path: /code/test-results
    destination: prefix

```

##### **store_test_results**

Special step used to upload test results so they can be used for timing analysis. **Note** At this time the results are not shown as artifacts in the web UI. To see test result as artifacts please also upload them using **store_artifacts**. This key is **not** supported with Workflows.

| Key  | Required | Type   | Description                              |
| ---- | -------- | ------ | ---------------------------------------- |
| path | Y        | String | Directory containing JUnit XML or Cucumber JSON test metadata files |

The directory layout should match the [classic CircleCI test metadata directory layout](https://circleci.com/docs/1.0/test-metadata/#metadata-collection-in-custom-test-steps).

###### *Example*

```
- store_test_results:
    path: /tmp/test-results

```

##### **persist_to_workspace**

Special step used to persist a temporary file to be used by another job in the workflow.

| Key   | Required | Type   | Description                              |
| ----- | -------- | ------ | ---------------------------------------- |
| root  | Y        | String | Either an absolute path or a path relative to `working_directory` |
| paths | Y        | List   | Glob identifying file(s), or a non-glob path to a directory to add to the shared workspace. Interpreted as relative to the workspace root. Must not be the workspace root itself. |

###### *Example*

```
- persist_to_workspace:
    root: /tmp/workspace
    paths: 
      - target/application.jar
      - build/*

```

##### **attach_workspace**

Special step used to attach the workflow’s workspace to the current container. The full contents of the workspace are downloaded and copied into the directory the workspace is being attached at.

| Key  | Required | Type   | Description                           |
| ---- | -------- | ------ | ------------------------------------- |
| at   | Y        | String | Directory to attach the workspace to. |

###### *Example*

```
- attach_workspace:
    at: /tmp/workspace

```

Each workflow has a temporary workspace associated with it. The workspace can be used to pass along unique data built during a job to other jobs in the same workflow. Jobs can add files into the workspace using the `persist_to_workspace` step and download the workspace content into their fileystem using the `attach_workspace` step. The workspace is additive only, jobs may add files to the workspace but cannot delete files from the workspace. Each job can only see content added to the workspace by the jobs that are upstream of it.

When attaching a workspace the “layer” from each upstream job is applied in the order the upstream jobs appear in the workflow graph. When two jobs run concurrently the order in which their layers are applied is undefined. If multiple concurrent jobs persist the same filename then attaching the workspace will error.

If a workflow is re-run it inherits the same workspace as the original workflow. When re-running failed jobs only the re-run jobs will see the same workspace content as the jobs in the original workflow.

Note the following distinctions between Artifacts, Workspaces, and Caches:

| Type       | lifetime             | Use                                      | Example                                  |
| ---------- | -------------------- | ---------------------------------------- | ---------------------------------------- |
| Artifacts  | Months               | Preserve long-term artifacts.            | Available in the Artifacts tab of the Build details under the `tmp/circle-artifacts.<hash>/container`   or similar directory. |
| Workspaces | Duration of workflow | Attach the workspace in a downstream container with the `attach_workspace:`step. | The `attach_workspace` copies and re-creates the entire workspace content when it runs. |
| Caches     | Months               | Store non-vital data that may help the job run faster, for example npm or Gem packages. | The `save_cache` job step with a `path` to a list of directories to add and a `key` to uniquely identify the cache (for example, the branch, build number, or revision). Restore the cache with `restore_cache` and the appropriate `key`. |

##### **add_ssh_keys**

Special step that adds SSH keys configured in the project’s UI to the container, and configure ssh to use them.

| Key          | Required | Type | Description                              |
| ------------ | -------- | ---- | ---------------------------------------- |
| fingerprints | N        | List | List of fingerprints corresponding to the keys to be added (default: all keys added) |

```
- add_ssh_keys:
    fingerprints:
      - "b7:35:a6:4e:9b:0d:6d:d4:78:1e:9a:97:2a:66:6b:be"

```

Note that CircleCI 2.0 jobs are auto configured with `ssh-agent` with all keys auto-loaded, and is sufficient for most cases. `add_ssh_keys` may be needed to have greater control over which SSH keys to authenticate (e.g. avoid “Too many authentication failures” problem when having too many SSH keys).

## **workflows**

Used for orchestrating all jobs. Each workflow consists of the workflow name as a key and a map as a value. A name should be unique within the current `config.yml`. The top-level keys for the Workflows configuration are `version`and `jobs`.

### **version**

The Workflows `version` field is used to issue warnings for deprecation or breaking changes during Beta.

| Key     | Required | Type   | Description             |
| ------- | -------- | ------ | ----------------------- |
| version | Y        | String | Should currently be `2` |

### **jobs**

A job can have the keys `requires`, `filters`, and `context`.

| Key  | Required | Type | Description                              |
| ---- | -------- | ---- | ---------------------------------------- |
| jobs | Y        | List | A list of jobs to run with their dependencies |

#### **build**

A unique name for your job.

##### **requires**

Jobs are run in parallel by default, so you must explicitly require any dependencies by their job name.

| Key      | Required | Type | Description                              |
| -------- | -------- | ---- | ---------------------------------------- |
| requires | N        | List | A list of jobs that must succeed for the job to start |

##### **contexts**

Jobs may be configured to use global environment variables set for an organization, see the [Contexts](https://circleci.com/docs/2.0/workflows) document for adding a context in the application settings.

| Key     | Required | Type   | Description                              |
| ------- | -------- | ------ | ---------------------------------------- |
| context | N        | String | The name of the context. The default name is `org-global`. |

##### **type**

A job may have a `type` of `approval` indicating it must be manually approved before downstream jobs may proceed. Jobs run in the dependency order until the workflow processes a job with the `type: approval` key followed by a job on which it depends, for example:

```
      - hold:
          type: approval
          requires:
            - test1
            - test2
      - deploy:
          requires:
            - hold

```

**Note:** The `hold` job must not exist in the main configuration.

##### **filters**

Filters can have the key `branches` or `tags`. **Note** Workflows will ignore job-level branching. If you use job-level branching and later add workflows, you must remove the branching at the job level and instead declare it in the workflows section of your `config.yml`, as follows:

| Key     | Required | Type | Description                              |
| ------- | -------- | ---- | ---------------------------------------- |
| filters | N        | Map  | A map defining rules for execution on specific branches |

###### **branches**

Branches can have the keys `only` and `ignore` which either map to a single string naming a branch (or a regexp to match against branches, which is required to be enclosed with /s) or map to a list of such strings.

- Any branches that match `only` will run the job.
- Any branches that match `ignore` will not run the job.
- If neither `only` nor `ignore` are specified then all branches will run the job.
- If both `only` and `ignore` are specified the `only` is considered before `ignore`.

| Key      | Required | Type                       | Description                              |
| -------- | -------- | -------------------------- | ---------------------------------------- |
| branches | N        | Map                        | A map defining rules for execution on specific branches |
| only     | N        | String, or List of Strings | Either a single branch specifier, or a list of branch specifiers |
| ignore   | N        | String, or List of Strings | Either a single branch specifier, or a list of branch specifiers |

###### **tags**

CircleCI treats tag and branch filters differently when deciding whether a job should run.

1. For a branch push unaffected by any filters, CircleCI runs the job.
2. For a tag push unaffected by any filters, CircleCI skips the job.

Item two above means that a job **must** have a `filters` `tags` section to run as a part of a tag push and all its transitively dependent jobs **must** also have a `filters` `tags` section. Refer to the [Git Tag Job Execution](https://circleci.com/docs/2.0/workflows/#git-tag-job-execution) section of the Orchestrating Workflows document for more examples.

Tags can have the keys `only` and `ignore` keys.

- Any tags that match `only` will run the job.
- Any tags that match `ignore` will not run the job.
- If neither `only` nor `ignore` are specified then the job is skipped for all tags.
- If both `only` and `ignore` are specified the `only` is considered before `ignore`.

| Key    | Required | Type                       | Description                              |
| ------ | -------- | -------------------------- | ---------------------------------------- |
| tags   | N        | Map                        | A map defining rules for execution on specific tags |
| only   | N        | String, or List of Strings | Either a single tag specifier, or a list of tag specifiers |
| ignore | N        | String, or List of Strings | Either a single tag specifier, or a list of tag specifiers |

##### *Example*

```
workflows:
  version: 2

  build_test_deploy:
    jobs:
      - flow
      - downstream:
          requires:
            - flow
          filters:
            branches:
              only: master

```

Refer to the [Orchestrating Workflows](https://circleci.com/docs/2.0/workflows) document for more examples and conceptual information.

## *Full Example*

```
version: 2
jobs:
  build:
    docker:
      - image: ubuntu:14.04

      - image: mongo:2.6.8
        command: [mongod, --smallfiles]

      - image: postgres:9.4.1
        # some containers require setting environment variables
        environment:
          POSTGRES_USER: root

      - image: redis@sha256:54057dd7e125ca41afe526a877e8bd35ec2cdd33b9217e022ed37bdcf7d09673

      - image: rabbitmq:3.5.4

    environment:
      TEST_REPORTS: /tmp/test-reports

    working_directory: ~/my-project

    branches:
      ignore:
        - develop
        - /feature-.*/

    steps:
      - checkout

      - run: command: echo 127.0.0.1 devhost | sudo tee -a /etc/hosts

      # Create Postgres users and database
      # Note the YAML heredoc '|' for nicer formatting
      - run: |
          sudo -u root createuser -h localhost --superuser ubuntu &&
          sudo createdb -h localhost test_db

      - restore_cache:
          keys:
            - v1-my-project-{{ checksum "project.clj" }}
            - v1-my-project-

      - run:
          environment:
            SSH_TARGET: "localhost"
            TEST_ENV: "linux"
          command: |
            set -xu
            mkdir -p ${TEST_REPORTS}
            run-tests.sh
            cp out/tests/*.xml ${TEST_REPORTS}

      - run: |
          set -xu
          mkdir -p /tmp/artifacts
          create_jars.sh ${CIRCLE_BUILD_NUM}
          cp *.jar /tmp/artifacts

      - save_cache:
          key: v1-my-project-{{ checksum "project.clj" }}
          paths:
            - ~/.m2

      # Deploy staging
      - deploy:
          command: |
            if [ "${CIRCLE_BRANCH}" == "staging" ];
              then ansible-playbook site.yml -i staging;
            fi

      # Deploy production
      - deploy:
          command: |
            if [ "${CIRCLE_BRANCH}" == "master" ];
              then ansible-playbook site.yml -i production;
            fi

      # Save artifacts
      - store_artifacts:
          path: /tmp/artifacts
          destination: build

      # Upload test results
      - store_test_results:
          path: /tmp/test-reports

```

------

## Help make this document better

This guide, as well as the rest of our docs, are open-source and available on [GitHub](https://github.com/circleci/circleci-docs). We welcome your contributions.

- [Suggest an edit to this page](https://github.com/circleci/circleci-docs/blob/master/jekyll/_cci2/configuration-reference.md) (please read the [contributing guide](https://github.com/circleci/circleci-docs/blob/master/CONTRIBUTING.md#contributing-to-circleci-docs) first).
- [Open an issue about this page](https://github.com/circleci/circleci-docs/issues/new?body=This%20issue%20is%20about%20%3Chttps://circleci.com/docs/2.0/configuration-reference/%3E%20(source%20file%3A%20%3Chttps://github.com/circleci/circleci-docs/blob/master/jekyll/_cci2/configuration-reference.md%3E)) to report a problem.
- [Visit our forum 'Discuss'](https://discuss.circleci.com/) to ask questions and search for solutions.

------

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)
CircleCI Documentation by [CircleCI](https://circleci.com/docs/) is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).