```
执行Bash脚本，命令或一组命令.

:param bash_command: 该命令，一组命令或对一个参考bash脚本（必须是'.sh'）才能执行。
:type bash_command: string
:param xcom_push: I如果xcom_push为True，则写入stdout的最后一行
    也会在bash命令完成时被推送到XCom。
:type xcom_push: bool
:param env: If env is not None, it must be a mapping that defines the
    environment variables for the new process; these are used instead
    of inheriting the current process environment, which is the default
    behavior. (templated)
:type env: dict
:type output_encoding: output encoding of bash command
```


## 关闭airflow 服务器

```
kill -9 `ps aux|grep airflow|awk '{print $2}'`
```



## Airflow 配置mysql 

```
CREATE DATABASE airflow;

GRANT all privileges on airflow.* TO 'kevin_air'@'%'  IDENTIFIED BY '654321';

FLUSH PRIVILEGES; 


```

## 更改airflow   配置文件

- `airflow.cfg` 文件通常在`~/airflow`目录下

- ```
  sql_alchemy_conn = mysql://kevin_air:654321@localhost/airflow
  对应字段解释如下： dialect+driver://username:password@host:port/database
  ```

- ```
  docker run -itd 
             --link mysql:mysql 
             -v /root/git_repo/Lighten/:/home/docker/code/Lighten 
             --name webapp-lighten 
             -p 80:80
         lighten
         bash
         
         
  ```

- ​








-------------------------------------------

# Airflow usage

Jump to...

1. [Airflow能做什么](http://blog.genesino.com/2016/05/airflow/#airflow%E8%83%BD%E5%81%9A%E4%BB%80%E4%B9%88)
2. 安装和使用
   1. [最简单安装](http://blog.genesino.com/2016/05/airflow/#%E6%9C%80%E7%AE%80%E5%8D%95%E5%AE%89%E8%A3%85)
   2. [配置 mysql以启用LocalExecutor和CeleryExecutor](http://blog.genesino.com/2016/05/airflow/#%E9%85%8D%E7%BD%AE-mysql%E4%BB%A5%E5%90%AF%E7%94%A8localexecutor%E5%92%8Cceleryexecutor)
   3. [配置LocalExecutor](http://blog.genesino.com/2016/05/airflow/#%E9%85%8D%E7%BD%AElocalexecutor)
   4. [配置CeleryExecutor (rabbitmq支持)](http://blog.genesino.com/2016/05/airflow/#%E9%85%8D%E7%BD%AEceleryexecutor-rabbitmq%E6%94%AF%E6%8C%81)
   5. [配置CeleryExecutor (redis支持)](http://blog.genesino.com/2016/05/airflow/#%E9%85%8D%E7%BD%AEceleryexecutor-redis%E6%94%AF%E6%8C%81)
   6. [一个脚本控制airflow系统的启动和重启](http://blog.genesino.com/2016/05/airflow/#%E4%B8%80%E4%B8%AA%E8%84%9A%E6%9C%AC%E6%8E%A7%E5%88%B6airflow%E7%B3%BB%E7%BB%9F%E7%9A%84%E5%90%AF%E5%8A%A8%E5%92%8C%E9%87%8D%E5%90%AF)
3. [airflow.cfg 其它配置](http://blog.genesino.com/2016/05/airflow/#airflowcfg-%E5%85%B6%E5%AE%83%E9%85%8D%E7%BD%AE)
4. [TASK](http://blog.genesino.com/2016/05/airflow/#task)
5. [其它问题](http://blog.genesino.com/2016/05/airflow/#%E5%85%B6%E5%AE%83%E9%97%AE%E9%A2%98)
6. [端口转发](http://blog.genesino.com/2016/05/airflow/#%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91)
7. [不同机器使用airflow](http://blog.genesino.com/2016/05/airflow/#%E4%B8%8D%E5%90%8C%E6%9C%BA%E5%99%A8%E4%BD%BF%E7%94%A8airflow)
8. [任务未按预期运行可能的原因](http://blog.genesino.com/2016/05/airflow/#%E4%BB%BB%E5%8A%A1%E6%9C%AA%E6%8C%89%E9%A2%84%E6%9C%9F%E8%BF%90%E8%A1%8C%E5%8F%AF%E8%83%BD%E7%9A%84%E5%8E%9F%E5%9B%A0)
9. [问题解决](http://blog.genesino.com/2016/05/airflow/#%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3)
10. [References](http://blog.genesino.com/2016/05/airflow/#references)
11. [Original link](http://blog.genesino.com/2016/05/airflow/#original-link)

### Airflow能做什么

[Airflow](https://airflow.incubator.apache.org/index.html)是一个工作流分配管理系统，通过有向非循环图的方式管理任务流程，设置任务依赖关系和时间调度。

Airflow独立于我们要运行的任务，只需要把任务的名字和运行方式提供给Airflow作为一个task就可以。

### 安装和使用

#### 最简单安装

在Linux终端运行如下命令 (需要已安装好`python2.x`和`pip`)：

```
pip install airflow
pip install "airflow[crypto, password]"
```

安装成功之后，执行下面三步，就可以使用了。默认是使用的`SequentialExecutor`, 只能顺次执行任务。

- 初始化数据库 `airflow initdb` [必须的步骤]
- 启动web服务器 `airflow webserver -p 8080` [方便可视化管理dag]
- 启动任务 `airflow scheduler` [scheduler启动后，DAG目录下的dags就会根据设定的时间定时启动]
- 此外我们还可以直接测试单个DAG，如测试文章末尾的DAG `airflow test ct1 print_date 2016-05-14`

最新版本的Airflow可从<https://github.com/apache/incubator-airflow>下载获得，解压缩按照安装python包的方式安装。

#### 配置 `mysql`以启用`LocalExecutor`和`CeleryExecutor`

- 安装mysql数据库支持 (5.7以上版本，如果是centos6，参考 <http://blog.genesino.com//collections/Linux_tips/>.

  ```
  yum install mysql mysql-server
  pip install airflow[mysql]
  ```

- 设置mysql根用户的密码

  ```
  ct@server:~/airflow: mysql -uroot #以root身份登录mysql，默认无密码
  mysql> SET PASSWORD=PASSWORD("passwd");
  mysql> FLUSH PRIVILEGES; 
  # 注意sql语句末尾的分号
  ```

- 新建用户和数据库

  ```
  # 新建名字为<airflow>的数据库
  mysql> CREATE DATABASE airflow; 
  # 新建用户`ct`，密码为`152108`, 该用户对数据库`airflow`有完全操作权限
  	  
  mysql> GRANT all privileges on airflow.* TO 'ct'@'localhost'  IDENTIFIED BY '152108'; 
  mysql> FLUSH PRIVILEGES; 
  ```

- 修改airflow配置文件支持mysql

  - `airflow.cfg` 文件通常在`~/airflow`目录下

  - 更改数据库链接

    ```
    sql_alchemy_conn = mysql://ct:152108@localhost:3306/airflow
    对应字段解释如下： dialect+driver://username:password@host:port/database
    ```

  - 初始化数据库 `airflow initdb`

  - 初始化数据库成功后，可进入mysql查看新生成的数据表。

    ```
    ct@server:~/airflow: mysql -uct -p152108
    mysql> USE airflow;
    mysql> SHOW TABLES;
    +-------------------+
    | Tables_in_airflow |
    +-------------------+
    | alembic_version   |
    | chart             |
    | connection        |
    | dag               |
    | dag_pickle        |
    | dag_run           |
    | import_error      |
    | job               |
    | known_event       |
    | known_event_type  |
    | log               |
    | sla_miss          |
    | slot_pool         |
    | task_instance     |
    | users             |
    | variable          |
    | xcom              |
    +-------------------+
    17 rows in set (0.00 sec)
    ```

- centos7中使用mariadb取代了mysql, 但所有命令的执行相同

  ```
  yum install mariadb mariadb-server
  systemctl start mariadb ==> 启动mariadb
  systemctl enable mariadb ==> 开机自启动
  mysql_secure_installation ==> 设置 root密码等相关
  mysql -uroot -p123456 ==> 测试登录！
  ```

#### 配置LocalExecutor

注：作为测试使用，此步可以跳过, 最后的生产环境用的是CeleryExecutor; 若CeleryExecutor配置不方便，也可使用LocalExecutor。

前面数据库已经配置好了，所以如果想使用LocalExecutor就只需要修改airflow配置文件就可以了。`airflow.cfg` 文件通常在`~/airflow`目录下，打开更改`executor`为 `executor = LocalExecutor`即完成了配置。

把文后[TASK](http://blog.genesino.com/2016/05/airflow/#task)部分的dag文件拷贝几个到`~/airflow/dags`目录下，顺次执行下面的命令，然后打开网址[http://127.0.0.1:8080](http://127.0.0.1:8080/)就可以实时侦测任务动态了：

```
ct@server:~/airflow: airflow initdb` (若前面执行过，就跳过)
ct@server:~/airflow: airflow webserver --debug &
ct@server:~/airflow: airflow scheduler
```

#### 配置CeleryExecutor (rabbitmq支持)

- 安装airflow的celery和rabbitmq组件

  ```
  pip install airflow[celery]
  pip install airflow[rabbitmq]
  ```

- 安装erlang和rabbitmq

  - 如果能直接使用`yum`或`apt-get`安装则万事大吉。

  - 我使用的CentOS6则不能，需要如下一番折腾，

    ```
    # (Centos6,[REF](http://www.rabbitmq.com/install-rpm.html))
    wget https://packages.erlang-solutions.com/erlang/esl-erlang/FLAVOUR_1_general/esl-erlang_18.3-1~centos~6_amd64.rpm
    yum install esl-erlang_18.3-1~centos~6_amd64.rpm
    wget https://github.com/jasonmcintosh/esl-erlang-compat/releases/download/1.1.1/esl-erlang-compat-18.1-1.noarch.rpm
    yum install esl-erlang-compat-18.1-1.noarch.rpm
    wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-3.6.1-1.noarch.rpm
    yum install rabbitmq-server-3.6.1-1.noarch.rpm
    ```

- 配置rabbitmq

  - 启动rabbitmq: `rabbitmq-server -detached`

  - 开机启动rabbitmq: `chkconfig rabbitmq-server on`

  - 配置rabbitmq ([REF](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html))

    ```
    rabbitmqctl add_user ct 152108
    rabbitmqctl add_vhost ct_airflow
    rabbitmqctl set_user_tags ct airflow
    rabbitmqctl set_permissions -p ct_airflow ct ".*" ".*" ".*"
    rabbitmq-plugins enable rabbitmq_management # no usage
    ```

- 修改airflow配置文件支持Celery

  - `airflow.cfg` 文件通常在`~/airflow`目录下

  - 更改executor为 `executor = CeleryExecutor`

  - 更改[broker_url](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html)

    ```
    broker_url = amqp://ct:152108@localhost:5672/ct_airflow
    Format explanation: transport://userid:password@hostname:port/virtual_host
    ```

  - 更改[celery_result_backend](http://docs.celeryproject.org/en/latest/configuration.html#conf-database-result-backend),

    ```
    # 可以与broker_url相同
    celery_result_backend = amqp://ct:152108@localhost:5672/ct_airflow
    Format explanation: transport://userid:password@hostname:port/virtual_host
    ```

#### 配置CeleryExecutor (redis支持)

- 安装airflow的celery和celery的redis组件

  ```
  pip install airflow[celery]
  pip install celery[redis]
  ```

- 安装redis

  ```
  #wget http://download.redis.io/releases/redis-3.2.0.tar.gz
  wget http://download.redis.io/releases/redis-stable.tar.gz
  tar xvzf redis-3.2.0.tar.gz
  cd redis*
  make
  ```

  `redis-server`启动redis

  启动时遇到的问题：

  ```
  26946:M 06 Sep 11:25:39.936 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
  26946:M 06 Sep 11:25:39.936 # Server initialized
  26946:M 06 Sep 11:25:39.936 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
  26946:M 06 Sep 11:25:39.936 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root,  and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
  ```

  解决方法

  1. overcommit_memory: [`0`表示内核将检查是否有足够的可用内存供应用进程使用；如果有足够的可用内存，内存申请允许；否则，内存申请失败，并把错误返回给应用进程。`1`表示内核允许分配所有的物理内存，而不管当前的内存状态如何。`2`表示内核允许分配超过所有物理内存和交换空间总和的内存。](https://jingyan.baidu.com/article/d5a880eba8af3c13f147ccb0.html)；修改办法按提示操作 `sysctl vm.overcommit_memory=1`。
  2. ransparent Huge Pages (THP): 透明大页；主要是用来提高内存管理效率的，目前还不推荐使用，按提示修改。

  ```
    echo never > /sys/kernel/mm/transparent_hugepage/enabled

   # 在 /etc/rc.local 中添加下面语句，保证重启后也有效
    if test -f /sys/kernel/mm/redhat_transparent_hugepage/enabled; then
        echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled
    fi
  ```

  参考：<http://www.jianshu.com/p/7ca4b74c92be>

  1. The TCP backlog setting of 511 cannot be enforced: `echo 511 > /proc/sys/net/core/somaxconn` [REF](https://github.com/docker-library/redis/issues/35#issuecomment-160620511) [REF2](https://stackoverflow.com/questions/26177059/refresh-net-core-somaxcomm-or-any-sysctl-property-for-docker-containers/26197875#26197875)

  使用`ps -ef | grep 'redis'`检测后台进程是否存在

  检测6379端口是否在监听`netstat -lntp | grep 6379`

  开机启动redis: `chkconfig redis-server`

- 修改airflow配置文件支持Celery-redis

  - `airflow.cfg` 文件通常在`~/airflow`目录下

  - 更改executor为 `executor = CeleryExecutor`

  - 更改[broker_url](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html)

    ```
    broker_url = redis://127.0.0.1:6379/0
    ```

  - 更改[celery_result_backend](http://docs.celeryproject.org/en/latest/configuration.html#conf-database-result-backend),

    ```
    # 可以与broker_url相同
    # celery_result_backend = redis://127.0.0.1:6379/0 
    # 或者使用mysql
    celery_result_backend = db+mysql://airflow:airflow@localhost:3306/airflow
    ```

- 测试

  - 启动服务器：`airflow webserver --debug`
  - 启动celery worker (不能用根用户)：`airflow worker`
  - 启动scheduler: `airflow scheduler`
  - 提示：
    - 测试过程中注意观察运行上面3个命令的3个窗口输出的日志
    - 当遇到不符合常理的情况时考虑清空 `airflow backend`的数据库, 可使用`airflow resetdb`清空。
    - 删除dag文件后，webserver中可能还会存在相应信息，这时需要重启webserver并刷新网页。
    - 关闭webserver: `ps -ef|grep -Ei '(airflow-webserver)'| grep master | awk '{print $2}'|xargs -i kill {}`

#### 一个脚本控制airflow系统的启动和重启

```
#!/bin/bash

#set -x
#set -e
set -u

usage()
{
cat <<EOF
${txtcyn}
Usage:

$0 options${txtrst}

${bldblu}Function${txtrst}:

This script is used to start or restart webserver service.

${txtbld}OPTIONS${txtrst}:
	-S	Start airflow system [${bldred}Default FALSE${txtrst}]
	-s	Restart airflow server only [${bldred}Default FALSE${txtrst}]
	-a	Restart all airflow programs including webserver, worker and
		scheduler. [${bldred}Default FALSE${txtrst}]
EOF
}

start_all=
server_only=
all=

while getopts "hs:S:a:" OPTION
do
	case $OPTION in
		h)
			usage
			exit 1
			;;
		S)
			start_all=$OPTARG
			;;
		s)
			server_only=$OPTARG
			;;
		a)
			all=$OPTARG
			;;
		?)
			usage
			exit 1
			;;
	esac
done

if [ -z "$server_only" ] && [ -z "$all" ] && [ -z "${start_all}" ]; then
	usage
	exit 1
fi

if [ "$server_only" == "TRUE" ]; then
	ps -ef | grep -Ei '(airflow-webserver)' | grep master | \
		awk '{print $2}' | xargs -i kill {}
	cd ~/airflow/
	nohup airflow webserver >webserver.log 2>&1 &
fi

if [ "$all" == "TRUE" ]; then
	ps -ef | grep -Ei 'airflow' | grep -v 'grep' | awk '{print $2}' | xargs -i kill {}
	cd ~/airflow/
	nohup airflow webserver >>webserver.log 2>&1 &
	nohup airflow worker >>worker.log 2>&1 &
	nohup airflow scheduler >>scheduler.log 2>&1 &
fi


if [ "${start_all}" == "TRUE" ]; then
	cd ~/airflow/
	nohup airflow webserver >>webserver.log 2>&1 &
	nohup airflow worker >>worker.log 2>&1 &
	nohup airflow scheduler >>scheduler.log 2>&1 &
fi
```

### airflow.cfg 其它配置

- dags_folder

  `dags_folder`目录支持子目录和软连接，因此不同的dag可以分门别类的存储起来。

- 设置邮件发送服务

  ```
  smtp_host = smtp.163.com
  smtp_starttls = True
  smtp_ssl = False
  smtp_user = username@163.com
  smtp_port = 25
  smtp_password = userpasswd
  smtp_mail_from = username@163.com
  ```

- 多用户登录设置 (似乎只有CeleryExecutor支持)

  - 修改`airflow.cfg`中的下面3行配置

    ```
    authenticate = True
    auth_backend = airflow.contrib.auth.backends.password_auth
    filter_by_owner = True
    ```

  - 增加一个用户(在airflow所在服务器的python下运行)

    ```
    import airflow
    from airflow import models,   settings
    from airflow.contrib.auth.backends.password_auth import PasswordUser
    user = PasswordUser(models.User())
    user.username = 'ehbio'
    user.email = 'mail@ehbio.com'
    user.password = 'ehbio'
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()
    exit()
    ```

### TASK

- 参数解释

  - `depends_on_past`

    Airflow assumes idempotent tasks that operate on immutable data chunks. It also assumes that all task instance (each task for each schedule) needs to run.

    If your tasks need to be executed sequentially, you need to tell Airflow: use the `depends_on_past=True` flag on the tasks that require sequential execution.)

    如果在TASK本该运行却没有运行时，或者设置的`interval`为`@once`时，推荐使用`depends_on_past=False`。我在运行dag时，有时会出现，明明上游任务已经运行结束，下游任务却没有启动，整个dag就卡住了。这时设置`depends_on_past=False`可以解决这类问题。

  - `timestamp` in format like `2016-01-01T00:03:00`

  - Task中调用的命令出错后需要在网站`Graph view`中点击`run`手动重启。 为了方便任务修改后的顺利运行，有个折衷的方法是：

    - 设置 `email_on_retry: True`
    - 设置较长的`retry_delay`，方便在收到邮件后，能有时间做出处理
    - 然后再修改为较短的`retry_delay`，方便快速启动

- 写完task DAG后，一定记得先检测下有无语法错误 `python dag.py`

- 测试文件1：ct1.py

  ```
  from airflow import DAG
  from airflow.operators import BashOperator, MySqlOperator
    
  from datetime import datetime, timedelta
    
  one_min_ago = datetime.combine(datetime.today() -
  	timedelta(minutes=1), datetime.min.time())
    
  default_args = {
      'owner': 'airflow',         
    		
  	  #为了测试方便，起始时间一般为当前时间减去schedule_interval
      'start_date': datetime(2016, 5, 29, 8, 30), 
      'email': ['chentong_biology@163.com'],
      'email_on_failure': False, 
      'email_on_retry': False, 
  	  'depends_on_past': False, 
      'retries': 1, 
      'retry_delay': timedelta(minutes=5), 
      #'queue': 'bash_queue',
      #'pool': 'backfill', 
      #'priority_weight': 10, 
  	  #'end_date': datetime(2016, 5, 29, 11, 30), 
  }
    
  # DAG id 'ct1'必须在airflow中是unique的, 一般与文件名相同
  # 多个用户时可加用户名做标记
  dag = DAG('ct1', default_args=default_args,
      schedule_interval="@once")
    
  t1 = BashOperator(
      task_id='print_date', 
      bash_command='date', 
      dag=dag)
    
  #cmd = "/home/test/test.bash " 注意末尾的空格
  #如果bash命令后面没有空格，会出现 "ERROR: template not found" 
  t2 = BashOperator(
      task_id='echo', 
      bash_command='echo "test" ', 
      retries=3, 
      dag=dag)
    
  templated_command = """
        
  """
  t3 = BashOperator(
      task_id='templated', 
      bash_command=templated_command, 
      params={'my_param': "Parameter I passed in"}, 
      dag=dag)
    
  # This means that t2 will depend on t1 running successfully to run
  # It is equivalent to t1.set_downstream(t2)
  t2.set_upstream(t1)
    
  t3.set_upstream(t1)
    
  # all of this is equivalent to
  # dag.set_dependency('print_date', 'sleep')
  # dag.set_dependency('print_date', 'templated')
  ```

- 测试文件2: `ct2.py`

  ```
  from airflow import DAG
  from airflow.operators import BashOperator
    
  from datetime import datetime, timedelta
    
  one_min_ago = datetime.combine(datetime.today() - timedelta(minutes=1),
                                    datetime.min.time())
    
  default_args = {
      'owner': 'airflow',         
      'depends_on_past': True, 
      'start_date': one_min_ago,
      'email': ['chentong_biology@163.com'],
      'email_on_failure': True, 
      'email_on_retry': True, 
      'retries': 5, 
      'retry_delay': timedelta(hours=30), 
      #'queue': 'bash_queue',
      #'pool': 'backfill', 
      #'priority_weight': 10, 
      #'end_date': datetime(2016, 5, 29, 11, 30), 
  }
    
  dag = DAG('ct2', default_args=default_args,
      schedule_interval="@once")
    
  t1 = BashOperator(
      task_id='run1', 
      bash_command='(cd /home/ct/test; bash run1.sh -f ct_t1) ', 
      dag=dag)
    
  t2 = BashOperator(
      task_id='run2', 
      bash_command='(cd /home/ct/test; bash run2.sh -f ct_t1) ', 
      dag=dag)
    
  t2.set_upstream(t1)
    
  ```

- run1.sh

  ```
  #!/bin/bash
    
  #set -x
  set -e
  set -u
    
  usage()
  {
  cat <<EOF
  ${txtcyn}
  Usage:
    
  $0 options${txtrst}
    
  ${bldblu}Function${txtrst}:
    
  This script is used to do ********************.
    
  ${txtbld}OPTIONS${txtrst}:
  	-f	Data file ${bldred}[NECESSARY]${txtrst}
  	-z	Is there a header[${bldred}Default TRUE${txtrst}]
  EOF
  }
    
  file=
  header='TRUE'
    
  while getopts "hf:z:" OPTION
  do
  	case $OPTION in
  		h)
  			usage
  			exit 1
  			;;
  		f)
  			file=$OPTARG
  			;;
  		z)
  			header=$OPTARG
  			;;
  		?)
  			usage
  			exit 1
  			;;
  	esac
  done
    
  if [ -z $file ]; then
  	usage
  	exit 1
  fi
    
  cat <<END >$file
  A
  B
  C
  D
  E
  F
  G
  END
    
  sleep 20s
  ```

- run2.sh

  ```
  #!/bin/bash
    
  #set -x
  set -e
  set -u
    
  usage()
  {
  cat <<EOF
  ${txtcyn}
  Usage:
    
  $0 options${txtrst}
    
  ${bldblu}Function${txtrst}:
    
  This script is used to do ********************.
    
  ${txtbld}OPTIONS${txtrst}:
  	-f	Data file ${bldred}[NECESSARY]${txtrst}
  EOF
  }
    
  file=
  header='TRUE'
    
  while getopts "hf:z:" OPTION
  do
  	case $OPTION in
  		h)
  			usage
  			exit 1
  			;;
  		f)
  			file=$OPTARG
  			;;
  		?)
  			usage
  			exit 1
  			;;
  	esac
  done
    
  if [ -z $file ]; then
  	usage
  	exit 1
  fi
    
  awk 'BEGIN{OFS=FS="\t"}{print $0, "53"}' $file >${file}.out
    
  ```

### 其它问题

- The DagRun object has room for a `conf` parameter that gets exposed in the “context” (templates, operators, …). That is the place where you would associate parameters to a specific run. For now this is only possible in the context of an externally triggered DAG run. The way the `TriggerDagRunOperator` works, you can fill in the conf param during the execution of the callable that you pass to the operator.

  If you are looking to change the shape of your DAG through parameters, we recommend doing that using “singleton” DAGs (using a “@once” `schedule_interval`), meaning that you would write a Python program that generates multiple dag_ids, one of each run, probably based on metadata stored in a config file or elsewhere.

  The idea is that if you use parameters to alter the shape of your DAG, you break some of the assumptions around continuity of the schedule. Things like visualizing the tree view or how to perform a backfill becomes unclear and mushy. So if the shape of your DAG changes radically based on parameters, we consider those to be different DAGs, and you generate each one in your pipeline file.

- 完全删掉某个DAG的信息

  ```
  set @dag_id = 'BAD_DAG';
  delete from airflow.xcom where dag_id = @dag_id;
  delete from airflow.task_instance where dag_id = @dag_id;
  delete from airflow.sla_miss where dag_id = @dag_id;
  delete from airflow.log where dag_id = @dag_id;
  delete from airflow.job where dag_id = @dag_id;
  delete from airflow.dag_run where dag_id = @dag_id;
  delete from airflow.dag where dag_id = @dag_id;
  ```

- supervisord自动管理进程

  ```
  [program:airflow_webserver]
  command=/usr/local/bin/python2.7 /usr/local/bin/airflow webserver
  user=airflow
  environment=AIRFLOW_HOME="/home/airflow/airflow", PATH="/usr/local/bin:%(ENV_PATH)s"
  stderr_logfile=/var/log/airflow-webserver.err.log
  stdout_logfile=/var/log/airflow-webserver.out.log
    
  [program:airflow_worker]
  command=/usr/local/bin/python2.7 /usr/local/bin/airflow worker
  user=airflow
  environment=AIRFLOW_HOME="/home/airflow/airflow", PATH="/usr/local/bin:%(ENV_PATH)s"
  stderr_logfile=/var/log/airflow-worker.err.log
  stdout_logfile=/var/log/airflow-worker.out.log
    
  [program:airflow_scheduler]
  command=/usr/local/bin/python2.7 /usr/local/bin/airflow scheduler
  user=airflow
  environment=AIRFLOW_HOME="/home/airflow/airflow", PATH="/usr/local/bin:%(ENV_PATH)s"
  stderr_logfile=/var/log/airflow-scheduler.err.log
  stdout_logfile=/var/log/airflow-scheduler.out.log
  ```

- 在特定情况下，修改DAG后，为了避免当前日期之前任务的运行，可以使用`backfill`填补特定时间段的任务

  - `airflow backfill -s START -e END --mark_success DAG_ID`

### [端口转发](https://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/)

- 之前的配置都是在内网服务器进行的，但内网服务器只开放了SSH端口22,因此 我尝试在另外一台电脑上使用相同的配置，然后设置端口转发，把外网服务器 的rabbitmq的5672端口映射到内网服务器的对应端口，然后启动airflow连接 。

  - `ssh -v -4 -NF -R 5672:127.0.0.1:5672 aliyun`

  - 上一条命令表示的格式为

    `ssh -R <local port>:<remote host>:<remote port> <SSH hostname>`

    `local port`表示hostname的port

    `Remote connections from LOCALHOST:5672 forwarded to local address 127.0.0.1:5672`

  - -v: 在测试时打开

  - -4: 出现错误”bind: Cannot assign requested address”时，force the ssh client to use ipv4

  - 若出现”Warning: remote port forwarding failed for listen port 52698” ，关掉其它的ssh tunnel。

### 不同机器使用airflow

- 在外网服务器（用做任务分发服务器）配置与内网服务器相同的airflow模块
- 使用前述的端口转发以便外网服务器绕过内网服务器的防火墙访问`rabbitmq 5672`端口。
- 在外网服务器启动 airflow `webserver` `scheduler`, 在内网服务器启动 `airflow worker` 发现任务执行状态丢失。继续学习Celery，以解决此问题。

### 任务未按预期运行可能的原因

- 检查 `start_date` 和`end_date`是否在合适的时间范围内
- 检查 `airflow worker`, `airflow scheduler`和 `airflow webserver --debug`的输出，有没有某个任务运行异常
- 检查airflow配置路径中`logs`文件夹下的日志输出
- 若以上都没有问题，则考虑数据冲突，解决方式包括清空数据库或着给当前 `dag`一个新的`dag_id`
  - `airflow resetdb`
  - Login in mysql and execute `DROP DATABASE airflow`

### 问题解决

- When running `airflow initdb` get error like “You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ‘(6) NULL’ at line 1” ) [SQL: u’ALTER TABLE dag MODIFY last_scheduler_run DATETIME(6) NULL’

  Install mysql5.7, clicke [here](http://blog.genesino.com//collections/Linux_tips/) for ref.

- Operator importing

  `airflow.operators.PigOperator` is no longer supported; `from airflow.operators.pig_operator import PigOperator`

  `from airflow.operators import BashOperator` to `from airflow.operators.bash_operator import BashOperator`

### References

1. <https://pythonhosted.org/airflow/>
2. <http://kintoki.farbox.com/post/ji-chu-zhi-shi/airflow>
3. <http://www.jianshu.com/p/59d69981658a>
4. <http://bytepawn.com/luigi-airflow-pinball.html>
5. <https://github.com/airbnb/airflow>
6. <https://media.readthedocs.org/pdf/airflow/latest/airflow.pdf>
7. <http://www.csdn.net/article/1970-01-01/2825690>
8. <http://www.cnblogs.com/harrychinese/p/airflow.html>
9. <https://segmentfault.com/a/1190000005078547>
10. QQ group: Airflow调度系统交流 178978627
11. <https://gtoonstra.github.io/etl-with-airflow/fullexample.html>

### Original link

原文链接 <http://blog.genesino.com//2016/05/airflow/>





## Airflow 例子解析

- example_bash_operator , 例子_bash_operator 算得上一个基础的operator 例子

  ```python
  # -*- coding: utf-8 -*-
  #
  # Licensed under the Apache License, Version 2.0 (the "License");
  # you may not use this file except in compliance with the License.
  # You may obtain a copy of the License at
  #
  # http://www.apache.org/licenses/LICENSE-2.0
  #
  # Unless required by applicable law or agreed to in writing, software
  # distributed under the License is distributed on an "AS IS" BASIS,
  # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  # See the License for the specific language governing permissions and
  # limitations under the License.

  import airflow
  from builtins import range
  from airflow.operators.bash_operator import BashOperator
  from airflow.operators.dummy_operator import DummyOperator
  from airflow.models import DAG
  from datetime import timedelta


  args = {
      'owner': 'airflow',
      'start_date': airflow.utils.dates.days_ago(2)
  }

  dag = DAG(
      dag_id='example_bash_operator', default_args=args,
      schedule_interval='0 0 * * *',
      dagrun_timeout=timedelta(minutes=60))

  cmd = 'ls -l'
  run_this_last = DummyOperator(task_id='run_this_last', dag=dag)

  run_this = BashOperator(
      task_id='run_after_loop', bash_command='echo 1', dag=dag)
  run_this.set_downstream(run_this_last)

  for i in range(3):
      i = str(i)
      task = BashOperator(
          task_id='runme_'+i,
          bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
          dag=dag)
      task.set_downstream(run_this)

  task = BashOperator(
      task_id='also_run_this',
      bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
      dag=dag)
  task.set_downstream(run_this_last)

  if __name__ == "__main__":
      dag.cli()
  ```

- example_branch_dop_operator_v3， dop分支 operator

  ```

  ```



### docker_operator

```
Execute a command inside a docker container.

    A temporary directory is created on the host and mounted into a container to allow storing files
    that together exceed the default disk size of 10GB in a container. The path to the mounted
    directory can be accessed via the environment variable ``AIRFLOW_TMP_DIR``.

    If a login to a private registry is required prior to pulling the image, a
    Docker connection needs to be configured in Airflow and the connection ID
    be provided with the parameter ``docker_conn_id``.

    :param image: Docker image from which to create the container.
    :type image: str
    :param api_version: Remote API version. Set to ``auto`` to automatically
        detect the server's version.
    :type api_version: str
    :param command: Command to be run in the container.
    :type command: str or list
    :param cpus: Number of CPUs to assign to the container.
        This value gets multiplied with 1024. See
        https://docs.docker.com/engine/reference/run/#cpu-share-constraint
    :type cpus: float
    :param docker_url: URL of the host running the docker daemon.
        Default is unix://var/run/docker.sock
    :type docker_url: str
    :param environment: Environment variables to set in the container.
    :type environment: dict
    :param force_pull: Pull the docker image on every run. Default is false.
    :type force_pull: bool
    :param mem_limit: Maximum amount of memory the container can use. Either a float value, which
        represents the limit in bytes, or a string like ``128m`` or ``1g``.
    :type mem_limit: float or str
    :param network_mode: Network mode for the container.
    :type network_mode: str
    :param tls_ca_cert: Path to a PEM-encoded certificate authority to secure the docker connection.
    :type tls_ca_cert: str
    :param tls_client_cert: Path to the PEM-encoded certificate used to authenticate docker client.
    :type tls_client_cert: str
    :param tls_client_key: Path to the PEM-encoded key used to authenticate docker client.
    :type tls_client_key: str
    :param tls_hostname: Hostname to match against the docker server certificate or False to
        disable the check.
    :type tls_hostname: str or bool
    :param tls_ssl_version: Version of SSL to use when communicating with docker daemon.
    :type tls_ssl_version: int
    :param tmp_dir: Mount point inside the container to a temporary directory created on the host by
        the operator. The path is also made available via the environment variable
        ``AIRFLOW_TMP_DIR`` inside the container.
    :type tmp_dir: str
    :param user: Default user inside the docker container.
    :type user: int or str
    :param volumes: List of volumes to mount into the container, e.g.
        ``['/host/path:/container/path', '/host/path2:/container/path2:ro']``.
    :param working_dir: Working directory to set on the container (equivalent to the -w switch
        the docker client)
    :type working_dir: str
    :param xcom_push: Does the stdout will be pushed to the next step using XCom.
           The default is False.
    :type xcom_push: bool
    :param xcom_all: Push all the stdout or just the last line. The default is False (last line).
    :type xcom_all: bool
    :param auto_remove: Automatically remove the container when it exits
    :type auto_remove: bool
    :param docker_conn_id: ID of the Airflow connection to use
    :type docker_conn_id: str
```

