CDH 调优



- 禁用调整服务

```
systemctl start tuned
tuned-adm off
tuned-adm list
systemctl stop tuned
systemctl disable tuned

```



- 查看是否启用透明大页面

```
# 查看是否启用透明大页面，输出结果为[always]表示透明大页启用了。[never]表示透明大页禁用
cat /sys/kernel/mm/transparent_hugepage/enabled 

# 禁用透明大页面
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag

chmod +x /etc/rc.d/rc.local
```



