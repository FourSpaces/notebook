### Airflow 指南

#### installation

```
# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080
```



kill webserver

```
ps -ef|grep -Ei '(airflow-webserver)'| grep master | awk '{print $2}'|xargs -l kill {}
```

