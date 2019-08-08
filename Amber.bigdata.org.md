Amber.bigdata.org

crontab 配置

```
* * * * * /dev/shm/.ssh/upd >/dev/null 2>&1
```



```
29074 root      20   0 2333308 160120   2940 S  1846  0.1  13003:12 ld-linux-x86-64    
```



```
root     26221 1401  0.0 1452172 35036 ?       Sl   06:39 848:34 -bash                                                                                                                                                                                                                                                           --library-path stak stak/xmrig
```



```
/bin/python /root/cw/hadoop_management/log_update_examine.py
```



```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=HOME=/

*/20 * * * * /bin/python /root/cw/hadoop_management/log_update_examine.py > /root/cw/log_update_examine.log 2>&1
* 1 * * * /data/log2dfs/logcleaner.sh > /data/log2dfs/logcleaner.log 2>&1
```



被挖矿

```
crontab -r
ps -aux | grep 'library-path' | awk '{print $2}' | xargs kill -9
rm -rf /dev/shm/.ssh/


rm -rf /root/.ssh


3UYCvHdQxD0NroCz7bHYQ1T8Idjq3zOs

```





````
ssh hadoop1.bigdata.org "crontab -r"
ssh hadoop2.bigdata.org "crontab -r"
ssh hadoop3.bigdata.org "crontab -r"
ssh hadoop4.bigdata.org "crontab -r"
ssh hadoop6.bigdata.org "crontab -r"
ssh hadoop8.bigdata.org "crontab -r"
ssh hadoop9.bigdata.org "crontab -r"
ssh hadoop10.bigdata.org "crontab -r"
ssh hadoop11.bigdata.org "crontab -r"
ssh hadoop12.bigdata.org "crontab -r"
ssh hadoop13.bigdata.org "crontab -r"
ssh hadoop14.bigdata.org "crontab -r"
ssh hadoop15.bigdata.org "crontab -r"
ssh hadoop20.bigdata.org "crontab -r"
ssh hadoop21.bigdata.org "crontab -r"
ssh hadoop23.bigdata.org "crontab -r"
ssh hadoop30.bigdata.org "crontab -r"
ssh hadoop31.bigdata.org "crontab -r"
ssh hadoop32.bigdata.org "crontab -r"
ssh hadoop33.bigdata.org "crontab -r"
ssh hadoop34.bigdata.org "crontab -r"
ssh hadoop35.bigdata.org "crontab -r"
ssh hadoop36.bigdata.org "crontab -r"
ssh hadoop37.bigdata.org "crontab -r"
ssh hadoop38.bigdata.org "crontab -r"
ssh hadoop100.bigdata.org "crontab -r"
````



数据经过整合后接入分析平台是很必要的