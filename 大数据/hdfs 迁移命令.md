# HDFS 数据迁移

```
hadoop distcp hftp://NameNode01:50070/old  hdfs://NEWNameNode01/new
```



迁移计划

```
1, 生成迁移任务列表。
2，生成任务 进行数据迁移
3，补充缺失数据
4，完成数据迁移
```



```
1）相同版本

#hadoop  distcp  -p  -skipcrccheck  -update –m 10 \

  hdfs://spark:9000/data/metastore/userlogs \

  hdfs://backup:9000/data/userlogs \

参数解释：

-p：带权限复制

-skipcrccheck: 跳过hdfs检查

-update: 比较两边文件的大小，如果不一样就更新，相同就不操作。如果不是追加数据，而是修改的数据，并且数据大小没有变，那就要结合-overwrite、-delete来使用
```



草稿

```
hadoop distcp -Ddistcp.bytes.per.map=1073741824 -Dmapreduce.job.queuename=hive -Dmapreduce.job.name=cpdata hdfs://hadoop10.bigdata.org/jars    hdfs://hadoop35.bigdata.org/jars 


hadoop distcp -Ddistcp.bytes.per.map=1073741824 -Dmapreduce.job.queuename=hive -Dmapreduce.job.name=cpdata /jars    hdfs://hadoop35.bigdata.org/jars 

hadoop distcp -Ddistcp.bytes.per.map=1073741824 -Dmapreduce.job.queuename=hive -Dmapreduce.job.name=cpdata /hive/warehouse/userdb.db  hdfs://hadoop35.bigdata.org/hive/warehouse/userdb.db
```



```
208.8 G  /hive/warehouse/bi.db
0        /hive/warehouse/ds.db
9.4 T    /hive/warehouse/dw.db
4.4 T    /hive/warehouse/log.db
7.1 G    /hive/warehouse/mid.db
29.0 G   /hive/warehouse/userdb.db
```

```
3.0 G    /hive/warehouse/dw.db/az_meta_active_imei
112.0 M  /hive/warehouse/dw.db/az_meta_app_time
18.5 M   /hive/warehouse/dw.db/az_meta_play_game
1.9 G    /hive/warehouse/dw.db/base_data_onlyid
1.6 G    /hive/warehouse/dw.db/imei_d
199.5 M  /hive/warehouse/dw.db/imei_m
500.7 M  /hive/warehouse/dw.db/imei_w
3.1 T    /hive/warehouse/dw.db/meta
4.0 T    /hive/warehouse/dw.db/meta_active_imei
284.7 G  /hive/warehouse/dw.db/meta_active_imei_20190403
6.2 G    /hive/warehouse/dw.db/meta_active_imei_copy
326.8 G  /hive/warehouse/dw.db/meta_active_imei_islogin
47.5 G   /hive/warehouse/dw.db/meta_ad
371.1 M  /hive/warehouse/dw.db/meta_app_crash_log
85.3 G   /hive/warehouse/dw.db/meta_app_detail
369.2 G  /hive/warehouse/dw.db/meta_app_time
65.6 G   /hive/warehouse/dw.db/meta_click_download
9.9 G    /hive/warehouse/dw.db/meta_collar_red_receive_success
43.5 G   /hive/warehouse/dw.db/meta_download
9.3 G    /hive/warehouse/dw.db/meta_event_gamein_video_play_success
31.6 M   /hive/warehouse/dw.db/meta_event_ranking_click
35.0 M   /hive/warehouse/dw.db/meta_event_split_mentorship_playtime
35.4 M   /hive/warehouse/dw.db/meta_event_split_on_mentorship_create
285.6 M  /hive/warehouse/dw.db/meta_event_youji_tab_click
684.4 K  /hive/warehouse/dw.db/meta_force_login_phone_success
6.2 M    /hive/warehouse/dw.db/meta_force_login_qq_success
3.0 M    /hive/warehouse/dw.db/meta_force_login_wechat_success
74.7 G   /hive/warehouse/dw.db/meta_launch
119.4 G  /hive/warehouse/dw.db/meta_native_crash_log
12.0 G   /hive/warehouse/dw.db/meta_new_imei
820.8 M  /hive/warehouse/dw.db/meta_new_imei_tmp
435.0 G  /hive/warehouse/dw.db/meta_onstart
834.1 M  /hive/warehouse/dw.db/meta_phone_sdcard_memory_space
279.2 G  /hive/warehouse/dw.db/meta_play_game
74.4 M   /hive/warehouse/dw.db/meta_plugin_crash_log
27.3 G   /hive/warehouse/dw.db/meta_show_mytask_page
84.9 G   /hive/warehouse/dw.db/meta_start_launch
5.2 G    /hive/warehouse/dw.db/meta_url_statistic
4.9 G    /hive/warehouse/dw.db/meta_v_activity_pause
5.0 G    /hive/warehouse/dw.db/meta_v_activity_resume
4.9 G    /hive/warehouse/dw.db/meta_v_start_launch
```

```
5.8 M     /hive/warehouse/bi.db/active_natural_month
1.8 M     /hive/warehouse/bi.db/active_natural_month1
4.2 M     /hive/warehouse/bi.db/active_natural_month2
1.0 M     /hive/warehouse/bi.db/active_natural_month3
2.1 M     /hive/warehouse/bi.db/active_natural_month4
765.1 K   /hive/warehouse/bi.db/active_natural_month5
1.6 M     /hive/warehouse/bi.db/active_natural_month6
11.3 M    /hive/warehouse/bi.db/active_natural_week
3.1 M     /hive/warehouse/bi.db/active_natural_week1
8.1 M     /hive/warehouse/bi.db/active_natural_week2
1.7 M     /hive/warehouse/bi.db/active_natural_week3
4.5 M     /hive/warehouse/bi.db/active_natural_week4
1.3 M     /hive/warehouse/bi.db/active_natural_week5
3.3 M     /hive/warehouse/bi.db/active_natural_week6
125.0 M   /hive/warehouse/bi.db/active_roll_month
46.8 M    /hive/warehouse/bi.db/active_roll_month1
90.1 M    /hive/warehouse/bi.db/active_roll_month2
23.9 M    /hive/warehouse/bi.db/active_roll_month3
49.9 M    /hive/warehouse/bi.db/active_roll_month4
16.6 M    /hive/warehouse/bi.db/active_roll_month5
35.4 M    /hive/warehouse/bi.db/active_roll_month6
77.5 M    /hive/warehouse/bi.db/active_roll_week
21.4 M    /hive/warehouse/bi.db/active_roll_week1
55.5 M    /hive/warehouse/bi.db/active_roll_week2
12.3 M    /hive/warehouse/bi.db/active_roll_week3
31.1 M    /hive/warehouse/bi.db/active_roll_week4
9.1 M     /hive/warehouse/bi.db/active_roll_week5
22.7 M    /hive/warehouse/bi.db/active_roll_week6
93.9 M    /hive/warehouse/bi.db/active_user_currency_amount
45.2 M    /hive/warehouse/bi.db/active_user_currency_statistic
4.5 G     /hive/warehouse/bi.db/ad2_stat_query_pvdim
684.1 M   /hive/warehouse/bi.db/ad2_stat_query_pvdim_copy
4.4 G     /hive/warehouse/bi.db/ad2_stat_query_uvdim
682.0 M   /hive/warehouse/bi.db/ad2_stat_query_uvdim_copy
172.9 M   /hive/warehouse/bi.db/ad_in_game_active_uv
231.1 M   /hive/warehouse/bi.db/ad_in_game_active_uv2
262.0 M   /hive/warehouse/bi.db/ad_in_game_all
67.9 M    /hive/warehouse/bi.db/ad_in_game_new
249.7 M   /hive/warehouse/bi.db/ad_in_game_old
950.1 M   /hive/warehouse/bi.db/ad_in_game_query_stat
179.4 M   /hive/warehouse/bi.db/ad_in_game_query_stat2
144.5 M   /hive/warehouse/bi.db/ad_in_game_stat2
893.0 M   /hive/warehouse/bi.db/ad_other_query_pvdim
886.7 M   /hive/warehouse/bi.db/ad_other_query_uvdim
82.4 M    /hive/warehouse/bi.db/ad_play_cnt_active_uv
233.8 M   /hive/warehouse/bi.db/ad_play_cnt_all
1.1 G     /hive/warehouse/bi.db/ad_play_cnt_dist
60.7 M    /hive/warehouse/bi.db/ad_play_cnt_new
226.9 M   /hive/warehouse/bi.db/ad_play_cnt_old
213.0 M   /hive/warehouse/bi.db/ad_stat_query_all
1.5 G     /hive/warehouse/bi.db/ad_stat_query_all_pv
1.5 G     /hive/warehouse/bi.db/ad_stat_query_all_uv
61.3 M    /hive/warehouse/bi.db/ad_stat_query_new
451.4 M   /hive/warehouse/bi.db/ad_stat_query_new_pv
448.3 M   /hive/warehouse/bi.db/ad_stat_query_new_uv
221.4 M   /hive/warehouse/bi.db/ad_stat_query_old
1.4 G     /hive/warehouse/bi.db/ad_stat_query_old_pv
1.4 G     /hive/warehouse/bi.db/ad_stat_query_old_uv
294.8 M   /hive/warehouse/bi.db/ad_stat_query_pvdim
307.1 M   /hive/warehouse/bi.db/ad_stat_query_uvdim
269.1 M   /hive/warehouse/bi.db/app_time_cnt_uv_dist
1.9 G     /hive/warehouse/bi.db/appname_firstplay_app_rday
1.1 G     /hive/warehouse/bi.db/appname_firstplay_app_rday1
141.5 M   /hive/warehouse/bi.db/appname_firstplay_app_rday2
854.4 M   /hive/warehouse/bi.db/appname_firstplay_app_rday3
29.3 M    /hive/warehouse/bi.db/appname_firstplay_app_rday4
1.9 G     /hive/warehouse/bi.db/appname_firstplay_game_rday
916.0 M   /hive/warehouse/bi.db/appname_firstplay_game_rday1
92.0 M    /hive/warehouse/bi.db/appname_firstplay_game_rday2
654.4 M   /hive/warehouse/bi.db/appname_firstplay_game_rday3
13.8 M    /hive/warehouse/bi.db/appname_firstplay_game_rday4
43.4 M    /hive/warehouse/bi.db/appversionname_channelid_islocklocation_active_uv
560.2 M   /hive/warehouse/bi.db/base_data_onlyid_app_time_play_time
1.3 G     /hive/warehouse/bi.db/base_data_onlyid_rday
184.9 K   /hive/warehouse/bi.db/base_data_onlyid_rday1
928.6 K   /hive/warehouse/bi.db/base_data_onlyid_rday10
1.7 M     /hive/warehouse/bi.db/base_data_onlyid_rday11
2.3 M     /hive/warehouse/bi.db/base_data_onlyid_rday12
1.6 M     /hive/warehouse/bi.db/base_data_onlyid_rday13
4.6 M     /hive/warehouse/bi.db/base_data_onlyid_rday14
189.9 K   /hive/warehouse/bi.db/base_data_onlyid_rday15
3.8 M     /hive/warehouse/bi.db/base_data_onlyid_rday16
9.5 M     /hive/warehouse/bi.db/base_data_onlyid_rday17
4.9 M     /hive/warehouse/bi.db/base_data_onlyid_rday18
26.9 M    /hive/warehouse/bi.db/base_data_onlyid_rday19
1.3 M     /hive/warehouse/bi.db/base_data_onlyid_rday2
15.6 M    /hive/warehouse/bi.db/base_data_onlyid_rday20
35.4 M    /hive/warehouse/bi.db/base_data_onlyid_rday21
69.1 M    /hive/warehouse/bi.db/base_data_onlyid_rday211
1.7 M     /hive/warehouse/bi.db/base_data_onlyid_rday22
1.7 M     /hive/warehouse/bi.db/base_data_onlyid_rday23
9.9 M     /hive/warehouse/bi.db/base_data_onlyid_rday24
14.7 M    /hive/warehouse/bi.db/base_data_onlyid_rday25
17.7 M    /hive/warehouse/bi.db/base_data_onlyid_rday26
45.5 M    /hive/warehouse/bi.db/base_data_onlyid_rday27
383.1 M   /hive/warehouse/bi.db/base_data_onlyid_rday28
189.8 K   /hive/warehouse/bi.db/base_data_onlyid_rday29
3.1 M     /hive/warehouse/bi.db/base_data_onlyid_rday3
3.9 M     /hive/warehouse/bi.db/base_data_onlyid_rday30
9.6 M     /hive/warehouse/bi.db/base_data_onlyid_rday31
5.1 M     /hive/warehouse/bi.db/base_data_onlyid_rday32
27.7 M    /hive/warehouse/bi.db/base_data_onlyid_rday33
15.9 M    /hive/warehouse/bi.db/base_data_onlyid_rday34
35.8 M    /hive/warehouse/bi.db/base_data_onlyid_rday35
71.1 M    /hive/warehouse/bi.db/base_data_onlyid_rday351
1.7 M     /hive/warehouse/bi.db/base_data_onlyid_rday36
1.7 M     /hive/warehouse/bi.db/base_data_onlyid_rday37
9.9 M     /hive/warehouse/bi.db/base_data_onlyid_rday38
14.9 M    /hive/warehouse/bi.db/base_data_onlyid_rday39
1.2 M     /hive/warehouse/bi.db/base_data_onlyid_rday4
17.9 M    /hive/warehouse/bi.db/base_data_onlyid_rday40
45.7 M    /hive/warehouse/bi.db/base_data_onlyid_rday41
395.6 M   /hive/warehouse/bi.db/base_data_onlyid_rday42
4.5 M     /hive/warehouse/bi.db/base_data_onlyid_rday5
2.0 M     /hive/warehouse/bi.db/base_data_onlyid_rday6
4.5 M     /hive/warehouse/bi.db/base_data_onlyid_rday7
5.6 M     /hive/warehouse/bi.db/base_data_onlyid_rday71
631.1 K   /hive/warehouse/bi.db/base_data_onlyid_rday8
720.0 K   /hive/warehouse/bi.db/base_data_onlyid_rday9
5.2 M     /hive/warehouse/bi.db/crash_stat_app_crash_log
25.1 M    /hive/warehouse/bi.db/crash_stat_app_play_time
50.3 M    /hive/warehouse/bi.db/crash_stat_app_pv
63.8 M    /hive/warehouse/bi.db/crash_stat_app_uv
18.8 M    /hive/warehouse/bi.db/crash_stat_crash_count
11.1 M    /hive/warehouse/bi.db/crash_stat_native_crash_log
3.3 M     /hive/warehouse/bi.db/crash_stat_plugin_crash_log
12.4 M    /hive/warehouse/bi.db/crash_stat_plugin_or_native_crash_log
15.2 M    /hive/warehouse/bi.db/crash_stat_v_start_launch
5.1 M     /hive/warehouse/bi.db/currency_record_recordtype_currencytype
392.9 M   /hive/warehouse/bi.db/currency_record_type_amount
88.3 M    /hive/warehouse/bi.db/currency_record_type_amount_all
0         /hive/warehouse/bi.db/currency_record_type_amount_base
22.6 M    /hive/warehouse/bi.db/currency_record_type_amount_new
86.8 M    /hive/warehouse/bi.db/currency_record_type_amount_old
8.8 M     /hive/warehouse/bi.db/event_mentor_apprentice_relation
1.7 M     /hive/warehouse/bi.db/event_mentor_apprentice_uv
524.2 K   /hive/warehouse/bi.db/event_mentor_apprentice_uv_week
3.5 M     /hive/warehouse/bi.db/event_rday
201.0 K   /hive/warehouse/bi.db/event_rday_all1
1.5 M     /hive/warehouse/bi.db/event_rday_all2
181.6 K   /hive/warehouse/bi.db/event_rday_new1
739.2 K   /hive/warehouse/bi.db/event_rday_new2
192.4 K   /hive/warehouse/bi.db/event_rday_old1
1.4 M     /hive/warehouse/bi.db/event_rday_old2
207.1 M   /hive/warehouse/bi.db/event_start_launch_game_success
406.7 M   /hive/warehouse/bi.db/game_crash_app_pv
260.0 M   /hive/warehouse/bi.db/game_crash_app_uv
4.4 G     /hive/warehouse/bi.db/game_crash_crash_count
380.2 M   /hive/warehouse/bi.db/game_crash_crash_count1
1.8 G     /hive/warehouse/bi.db/game_crash_crash_count2
47.5 M    /hive/warehouse/bi.db/game_crash_crash_count3
245.8 M   /hive/warehouse/bi.db/game_crash_crash_count4
2.0 G     /hive/warehouse/bi.db/game_crash_crash_count5
521.4 M   /hive/warehouse/bi.db/game_crash_native_crash_log
3.9 G     /hive/warehouse/bi.db/game_crash_play_game
35.1 M    /hive/warehouse/bi.db/game_crash_plugin_crash_log
547.5 M   /hive/warehouse/bi.db/game_crash_plugin_or_native_crash_log
3.9 G     /hive/warehouse/bi.db/game_crash_v_start_launch
6.7 G     /hive/warehouse/bi.db/game_dim_event_start_launch_game_success
1.8 G     /hive/warehouse/bi.db/game_dim_event_start_launch_game_success2
190.9 M   /hive/warehouse/bi.db/gamein_video_play
40.5 K    /hive/warehouse/bi.db/imei_active_rday
69.3 K    /hive/warehouse/bi.db/imei_new_rday
201       /hive/warehouse/bi.db/imei_new_rmonth
66        /hive/warehouse/bi.db/imei_new_rmonth1
44        /hive/warehouse/bi.db/imei_new_rmonth2
22        /hive/warehouse/bi.db/imei_new_rmonth3
39        /hive/warehouse/bi.db/imei_new_rmonth4
2.3 K     /hive/warehouse/bi.db/imei_new_rweek
437       /hive/warehouse/bi.db/imei_new_rweek1
414       /hive/warehouse/bi.db/imei_new_rweek2
464       /hive/warehouse/bi.db/imei_new_rweek3
457       /hive/warehouse/bi.db/imei_new_rweek4
335       /hive/warehouse/bi.db/imei_new_rweek5
451       /hive/warehouse/bi.db/imei_new_rweek6
447       /hive/warehouse/bi.db/imei_new_rweek7
444       /hive/warehouse/bi.db/imei_new_rweek8
447.0 M   /hive/warehouse/bi.db/islogin_imei_stat
109.9 M   /hive/warehouse/bi.db/islogin_stat_imei
1.9 G     /hive/warehouse/bi.db/kind_uv_pv
796.9 M   /hive/warehouse/bi.db/kind_uv_pv_copy
64.5 M    /hive/warehouse/bi.db/luckyday_stat_query
109.2 M   /hive/warehouse/bi.db/luckyday_stat_query_all
18.2 M    /hive/warehouse/bi.db/luckyday_stat_query_new
52.8 M    /hive/warehouse/bi.db/luckyday_stat_query_old
84.9 M    /hive/warehouse/bi.db/luckyday_stat_query_pvdim
80.8 M    /hive/warehouse/bi.db/luckyday_stat_query_uvdim
3.7 K     /hive/warehouse/bi.db/meta_dau_dnu_game
37.9 M    /hive/warehouse/bi.db/natural_week_active_game_login_stat
28.1 M    /hive/warehouse/bi.db/natural_week_active_stat
5.3 M     /hive/warehouse/bi.db/natural_week_login_7day_sum
6.7 M     /hive/warehouse/bi.db/natural_week_login_stat
3.2 M     /hive/warehouse/bi.db/network_speed_detail
1.2 K     /hive/warehouse/bi.db/onstart_cnt_dist
333.6 M   /hive/warehouse/bi.db/play_game_app_time_out2s_imei_stat
166.6 M   /hive/warehouse/bi.db/play_game_cnt_uv_dist
73.8 M    /hive/warehouse/bi.db/play_game_cnt_uv_dist_all
21.4 M    /hive/warehouse/bi.db/play_game_cnt_uv_dist_new
71.5 M    /hive/warehouse/bi.db/play_game_cnt_uv_dist_old
189.3 M   /hive/warehouse/bi.db/play_time_cnt_uv_dist
1.1 G     /hive/warehouse/bi.db/product2_stat_query_pvdim
619.1 M   /hive/warehouse/bi.db/product2_stat_query_pvdim_copy
401.2 M   /hive/warehouse/bi.db/product2_stat_query_uvdim
640.4 M   /hive/warehouse/bi.db/product2_stat_query_uvdim_copy
642.7 M   /hive/warehouse/bi.db/product3_stat_query_pvdim
113.8 M   /hive/warehouse/bi.db/product3_stat_query_pvdim_copy
390.0 M   /hive/warehouse/bi.db/product3_stat_query_uvdim
238.2 M   /hive/warehouse/bi.db/product3_stat_query_uvdim_copy
39        /hive/warehouse/bi.db/product_check
1.3 G     /hive/warehouse/bi.db/product_stat_query_all_pv1
1.3 G     /hive/warehouse/bi.db/product_stat_query_all_pv2
1.3 G     /hive/warehouse/bi.db/product_stat_query_all_pv3
1.1 G     /hive/warehouse/bi.db/product_stat_query_all_pv4
383.2 M   /hive/warehouse/bi.db/product_stat_query_all_uv1
380.6 M   /hive/warehouse/bi.db/product_stat_query_all_uv2
1.5 M     /hive/warehouse/bi.db/product_stat_query_all_uv2_demo
388.6 M   /hive/warehouse/bi.db/product_stat_query_all_uv3
237.6 M   /hive/warehouse/bi.db/product_stat_query_all_uv4
90.2 M    /hive/warehouse/bi.db/product_stat_query_new_pv1
88.6 M    /hive/warehouse/bi.db/product_stat_query_new_pv2
89.0 M    /hive/warehouse/bi.db/product_stat_query_new_pv3
64.9 M    /hive/warehouse/bi.db/product_stat_query_new_pv4
89.5 M    /hive/warehouse/bi.db/product_stat_query_new_uv1
88.9 M    /hive/warehouse/bi.db/product_stat_query_new_uv2
90.6 M    /hive/warehouse/bi.db/product_stat_query_new_uv3
64.4 M    /hive/warehouse/bi.db/product_stat_query_new_uv4
365.9 M   /hive/warehouse/bi.db/product_stat_query_old_pv1
359.7 M   /hive/warehouse/bi.db/product_stat_query_old_pv2
361.9 M   /hive/warehouse/bi.db/product_stat_query_old_pv3
225.3 M   /hive/warehouse/bi.db/product_stat_query_old_pv4
363.4 M   /hive/warehouse/bi.db/product_stat_query_old_uv1
360.9 M   /hive/warehouse/bi.db/product_stat_query_old_uv2
368.6 M   /hive/warehouse/bi.db/product_stat_query_old_uv3
224.9 M   /hive/warehouse/bi.db/product_stat_query_old_uv4
570.3 M   /hive/warehouse/bi.db/product_stat_query_pvdim
799.0 M   /hive/warehouse/bi.db/product_stat_query_pvdim_copy
222.4 M   /hive/warehouse/bi.db/product_stat_query_uvdim
816.6 M   /hive/warehouse/bi.db/product_stat_query_uvdim_copy
115.7 M   /hive/warehouse/bi.db/push_show_receive_click_rate
24.9 M    /hive/warehouse/bi.db/pushfrom_active_uv
24.1 M    /hive/warehouse/bi.db/pushfrom_stat_query
36.9 M    /hive/warehouse/bi.db/pushfrom_stat_query_dim
9.7 M     /hive/warehouse/bi.db/req_dur_slow_url_statistic
41.3 M    /hive/warehouse/bi.db/scratcher_show_reward_active_uv
38.8 M    /hive/warehouse/bi.db/scratcher_show_reward_dist
92.3 M    /hive/warehouse/bi.db/scratcher_show_reward_query
1.5 M     /hive/warehouse/bi.db/serch_key_click_rate
0         /hive/warehouse/bi.db/split_stat_query
425.2 M   /hive/warehouse/bi.db/split_stat_query_pv
188.0 M   /hive/warehouse/bi.db/split_stat_query_pv_all
48.7 M    /hive/warehouse/bi.db/split_stat_query_pv_new
188.4 M   /hive/warehouse/bi.db/split_stat_query_pv_old
388.9 M   /hive/warehouse/bi.db/split_stat_query_uv
72.1 K    /hive/warehouse/bi.db/stat_imei_new_rday
112.4 M   /hive/warehouse/bi.db/stat_query_app_detail
510.8 M   /hive/warehouse/bi.db/stat_query_app_play_time
638.1 M   /hive/warehouse/bi.db/stat_query_basic_pvdim
416.9 M   /hive/warehouse/bi.db/stat_query_basic_pvdim_copy
967.5 M   /hive/warehouse/bi.db/stat_query_basic_uvdim
631.0 M   /hive/warehouse/bi.db/stat_query_basic_uvdim_copy
105.7 M   /hive/warehouse/bi.db/stat_query_click_download
164.7 M   /hive/warehouse/bi.db/stat_query_download
79.7 M    /hive/warehouse/bi.db/stat_query_failed_stat
70.1 M    /hive/warehouse/bi.db/stat_query_game_launch
61.9 M    /hive/warehouse/bi.db/stat_query_gamedata_play_game_time
61.9 M    /hive/warehouse/bi.db/stat_query_gamedata_play_game_time_nopartition
7.9 G     /hive/warehouse/bi.db/stat_query_gamedim_app_detail
1.4 G     /hive/warehouse/bi.db/stat_query_gamedim_app_detail2
5.6 G     /hive/warehouse/bi.db/stat_query_gamedim_begin_download
1021.7 M  /hive/warehouse/bi.db/stat_query_gamedim_begin_download2
5.6 G     /hive/warehouse/bi.db/stat_query_gamedim_click_download
998.4 M   /hive/warehouse/bi.db/stat_query_gamedim_click_download2
6.9 G     /hive/warehouse/bi.db/stat_query_gamedim_fail_launch
1.3 G     /hive/warehouse/bi.db/stat_query_gamedim_fail_launch2
11.1 G    /hive/warehouse/bi.db/stat_query_gamedim_play_game
2.0 G     /hive/warehouse/bi.db/stat_query_gamedim_play_game2
7.1 G     /hive/warehouse/bi.db/stat_query_gamedim_start_launch
1.4 G     /hive/warehouse/bi.db/stat_query_gamedim_start_launch2
7.3 G     /hive/warehouse/bi.db/stat_query_gamedim_success_interrupt_failed_download
1.3 G     /hive/warehouse/bi.db/stat_query_gamedim_success_interrupt_failed_download2
7.3 G     /hive/warehouse/bi.db/stat_query_gamedim_success_launch
1.6 G     /hive/warehouse/bi.db/stat_query_gamedim_success_launch2
21.2 G    /hive/warehouse/bi.db/stat_query_gdim_appname_pvdim
2.0 G     /hive/warehouse/bi.db/stat_query_gdim_appname_pvdim_copy
16.9 G    /hive/warehouse/bi.db/stat_query_gdim_appname_uvdim
4.2 G     /hive/warehouse/bi.db/stat_query_gdim_appname_uvdim2
1.5 G     /hive/warehouse/bi.db/stat_query_gdim_appname_uvdim_copy
222.7 M   /hive/warehouse/bi.db/stat_query_imei_num
97.4 M    /hive/warehouse/bi.db/stat_query_imei_num_all
31.5 M    /hive/warehouse/bi.db/stat_query_imei_num_new
93.8 M    /hive/warehouse/bi.db/stat_query_imei_num_old
130.8 M   /hive/warehouse/bi.db/stat_query_launch
109.7 M   /hive/warehouse/bi.db/stat_query_launch_fail
168.1 M   /hive/warehouse/bi.db/stat_query_onstart_imei
239.2 M   /hive/warehouse/bi.db/stat_query_play_game_time
136.1 M   /hive/warehouse/bi.db/stat_query_start_launch
103       /hive/warehouse/bi.db/test
171.5 M   /hive/warehouse/bi.db/time_imei_rday
51.7 K    /hive/warehouse/bi.db/time_imei_rday1
1.4 M     /hive/warehouse/bi.db/time_imei_rday10
1.3 M     /hive/warehouse/bi.db/time_imei_rday11
1.4 M     /hive/warehouse/bi.db/time_imei_rday12
3.7 M     /hive/warehouse/bi.db/time_imei_rday13
8.4 M     /hive/warehouse/bi.db/time_imei_rday14
52.4 K    /hive/warehouse/bi.db/time_imei_rday15
1.7 M     /hive/warehouse/bi.db/time_imei_rday16
8.9 M     /hive/warehouse/bi.db/time_imei_rday17
1.4 M     /hive/warehouse/bi.db/time_imei_rday18
25.8 M    /hive/warehouse/bi.db/time_imei_rday19
767.4 K   /hive/warehouse/bi.db/time_imei_rday2
5.2 M     /hive/warehouse/bi.db/time_imei_rday20
17.3 M    /hive/warehouse/bi.db/time_imei_rday21
25.7 M    /hive/warehouse/bi.db/time_imei_rday22
283.4 K   /hive/warehouse/bi.db/time_imei_rday23
1.7 M     /hive/warehouse/bi.db/time_imei_rday24
3.4 M     /hive/warehouse/bi.db/time_imei_rday25
3.3 M     /hive/warehouse/bi.db/time_imei_rday26
9.8 M     /hive/warehouse/bi.db/time_imei_rday27
69.1 M    /hive/warehouse/bi.db/time_imei_rday28
52.4 K    /hive/warehouse/bi.db/time_imei_rday29
3.6 M     /hive/warehouse/bi.db/time_imei_rday3
1.7 M     /hive/warehouse/bi.db/time_imei_rday30
9.1 M     /hive/warehouse/bi.db/time_imei_rday31
1.5 M     /hive/warehouse/bi.db/time_imei_rday32
26.2 M    /hive/warehouse/bi.db/time_imei_rday33
5.3 M     /hive/warehouse/bi.db/time_imei_rday34
17.9 M    /hive/warehouse/bi.db/time_imei_rday35
26.4 M    /hive/warehouse/bi.db/time_imei_rday36
288.4 K   /hive/warehouse/bi.db/time_imei_rday37
1.7 M     /hive/warehouse/bi.db/time_imei_rday38
3.4 M     /hive/warehouse/bi.db/time_imei_rday39
469.7 K   /hive/warehouse/bi.db/time_imei_rday4
3.5 M     /hive/warehouse/bi.db/time_imei_rday40
10.3 M    /hive/warehouse/bi.db/time_imei_rday41
63.5 M    /hive/warehouse/bi.db/time_imei_rday42
5.6 M     /hive/warehouse/bi.db/time_imei_rday5
1.3 M     /hive/warehouse/bi.db/time_imei_rday6
5.7 M     /hive/warehouse/bi.db/time_imei_rday7
6.9 M     /hive/warehouse/bi.db/time_imei_rday8
261.7 K   /hive/warehouse/bi.db/time_imei_rday9
340.1 K   /hive/warehouse/bi.db/tmp
82.4 M    /hive/warehouse/bi.db/use_days_stat
20.4 M    /hive/warehouse/bi.db/use_days_stat1
12.1 M    /hive/warehouse/bi.db/use_days_stat10
3.1 M     /hive/warehouse/bi.db/use_days_stat11
8.8 M     /hive/warehouse/bi.db/use_days_stat12
19.4 M    /hive/warehouse/bi.db/use_days_stat3
19.5 M    /hive/warehouse/bi.db/use_days_stat4
15.6 M    /hive/warehouse/bi.db/use_days_stat5
12.3 M    /hive/warehouse/bi.db/use_days_stat6
11.5 M    /hive/warehouse/bi.db/use_days_stat7
12.7 M    /hive/warehouse/bi.db/use_days_stat8
13.1 M    /hive/warehouse/bi.db/use_days_stat9
955.0 M   /hive/warehouse/bi.db/week_add_log_active_login_play_uv
230.7 M   /hive/warehouse/bi.db/week_add_log_uv
191.9 M   /hive/warehouse/bi.db/week_add_login_uv
455.1 M   /hive/warehouse/bi.db/week_add_play_uv
```





```
['CREATE TABLE `base_data_onlyid`(', '  `kind` string, ', '  `appversionname` string, ', '  `channelid` string, ', '  `devicebrand` string, ', '  `systemversion` string, ', '  `islocklocation` string, ', '  `imei` string)', 'PARTITIONED BY ( ', '  `ymd` string)', 'ROW FORMAT SERDE ', "  'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' ", 'STORED AS INPUTFORMAT ', "  'org.apache.hadoop.mapred.TextInputFormat' ", 'OUTPUTFORMAT ', "  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'", 'LOCATION', "  'hdfs://myha01/hive/warehouse/dw.db/base_data_onlyid'", 'TBLPROPERTIES (', "  'transient_lastDdlTime'='1556274761')"]
```

