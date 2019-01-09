# hive 常见语句



**NVL(expr1, expr2)**：

如果expr1为NULL，返回值为 expr2，否则返回expr1。 expr1和expr2的数据类型必须为同类型。

--------------------------------------------------------------------

语法: if(boolean testCondition, T valueTrue, T valueFalseOrNull)

返回值: T

说明:  当条件testCondition为TRUE时，返回valueTrue；否则返回valueFalseOrNull

```
insert overwrite table bi.base_data_onlyid_rday1
select nvl(t2.ymd, t1.ymd) ymd,
nvl(t2.kind, t1.kind) kind, 
'NEW' imei_type,  -- 设置默认值
'ALL' appversionname,
'ALL' channelid,
'ALL' islocklocation,
'ALL' devicebrand,
'ALL' systemversion,
nvl(t2.imei, t1.imei) as imei,
if(nvl(t2.day1,0)=0, t1.day1, t2.day1) day1,
if(nvl(t2.day2,0)=0, t1.day2, t2.day2) day2,
if(nvl(t2.day3,0)=0, t1.day3, t2.day3) day3,
if(nvl(t2.day4,0)=0, t1.day4, t2.day4) day4,
if(nvl(t2.day5,0)=0, t1.day5, t2.day5) day5,

if(nvl(t2.rate1,0)=0, t1.rate1, t2.rate1) rate1,
if(nvl(t2.rate2,0)=0, t1.rate2, t2.rate2) rate2,
if(nvl(t2.rate3,0)=0, t1.rate3, t2.rate3) rate3,
if(nvl(t2.rate4,0)=0, t1.rate4, t2.rate4) rate4,
if(nvl(t2.rate5,0)=0, t1.rate5, t2.rate5) rate5
from bi.base_data_onlyid_rday1 t1
full outer join 
(select a.ymd,
a.kind,
count(distinct a.imei) imei,
count(distinct if(a.ymd = '${DATE_2D}', b.imei, null)) day1,
count(distinct if(a.ymd = '${DATE_3D}', b.imei, null)) day2,
count(distinct if(a.ymd = '${DATE_4D}', b.imei, null)) day3,
count(distinct if(a.ymd = '${DATE_5D}', b.imei, null)) day4,
count(distinct if(a.ymd = '${DATE_6D}', b.imei, null)) day5,

count(distinct if(a.ymd = '${DATE_2D}', b.imei, null))/count(distinct a.imei) rate1,
count(distinct if(a.ymd = '${DATE_3D}', b.imei, null))/count(distinct a.imei) rate2,
count(distinct if(a.ymd = '${DATE_4D}', b.imei, null))/count(distinct a.imei) rate3,
count(distinct if(a.ymd = '${DATE_5D}', b.imei, null))/count(distinct a.imei) rate4,
count(distinct if(a.ymd = '${DATE_6D}', b.imei, null))/count(distinct a.imei) rate5
from 
    (select distinct a1.ymd, a1.kind, a1.imei from 
        (select distinct ymd, kind, imei from dw.base_data_onlyid
        where ymd in ('${DATE_1D}','${DATE_2D}','${DATE_3D}','${DATE_4D}','${DATE_5D}','${DATE_6D}')) a1
    inner join 
        (select distinct ymd, imei from dw.meta_new_imei
        where ymd in ('${DATE_1D}','${DATE_2D}','${DATE_3D}','${DATE_4D}','${DATE_5D}','${DATE_6D}')) a2
    on a1.ymd = a2.ymd and a1.imei = a2.imei) a
left outer join 
    (select distinct b1.imei from 
        (select distinct imei from dw.meta_play_game
        where ymd = '${DATE_1D}' and playtime > 0
        union all
        select distinct imei from dw.meta_app_time
        where ymd = '${DATE_1D}' and playtime > 0) b1 
    ) b 
on a.imei = b.imei
group by a.ymd, a.kind) t2 
on t1.ymd = t2.ymd and t1.kind = t2.kind;
```

distinct

能使用`group by`代替`distinc`就不要使用`distinct`,

set mapred.reduce.tasks=100；



删除表

```
DROP TABLE IF EXISTS employee;
```