# Airflow 错误信息集合

#### airflow.exceptions.AirflowException: 

- Could not create Fernet object: Fernet key must be 32 url-safe base64-encoded bytes.

```
Traceback (most recent call last):
  File "/Users/weicheng/anaconda/lib/python3.6/site-packages/airflow/models.py", line 639, in set_extra
    fernet = get_fernet()
  File "/Users/weicheng/anaconda/lib/python3.6/site-packages/airflow/models.py", line 107, in get_fernet
    raise AirflowException("Could not create Fernet object: {}".format(ve))
airflow.exceptions.AirflowException: Could not create Fernet object: Fernet key must be 32 url-safe base64-encoded bytes.
```

- 问题原因，airflow.cfg 文件出现问题，检查一下。