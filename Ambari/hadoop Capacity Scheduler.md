# hadoop Capacity Scheduler



### Queue Properties

- Resource Allocation

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.<queue-path>.capacity`              | 以百分比（％）排队容量为浮点数（例如12.5）。 每个级别的所有队列的容量总和必须等于100.如果有空闲资源，则队列中的应用程序可能比队列容量消耗更多资源，从而提供弹性。 |
| `yarn.scheduler.capacity.<queue-path>.maximum-capacity`      | 最大队列容量，以百分比（％）表示为浮点数。 这限制了队列中应用程序的弹性。 默认为-1，禁用它。 |
| `yarn.scheduler.capacity.<queue-path>.minimum-user-limit-percent` | 如果存在资源需求，则每个队列对在任何给定时间分配给用户的资源百分比强制实施限制。 用户限制可以在最小值和最大值之间变化。 前者（最小值）设置为此属性值，后者（最大值）取决于已提交应用程序的用户数。 例如，假设此属性的值为25.如果两个用户已将应用程序提交到队列，则任何单个用户都不能使用超过50％的队列资源。 如果第三个用户提交应用程序，则任何单个用户都不能使用超过33％的队列资源。 对于4个或更多用户，没有用户可以使用超过25％的队列资源。 值100表示不强加用户限制。 默认值为100.值指定为整数。 |
| `yarn.scheduler.capacity.<queue-path>.user-limit-factor`     | 队列容量的倍数，可以配置为允许单个用户获取更多资源。 默认情况下，此值设置为1可确保单个用户永远不会超过队列配置的容量，无论群集的空闲程度如何。 值被指定为float。 |
| `yarn.scheduler.capacity.<queue-path>.maximum-allocation-mb` | 每个队列在资源管理器上分配给每个容器请求的最大内存限制。 此设置将覆盖群集配置`yarn.scheduler.maximum-allocation-mb`. 该值必须小于或等于群集最大值。 |
| `yarn.scheduler.capacity.<queue-path>.maximum-allocation-vcores` | 在资源管理器中分配给每个容器请求的虚拟核心的每个队列最大限制。 此设置将覆盖群集配置`yarn.scheduler.maximum-allocation-vcores`. 该值必须小于或等于群集最大值。 |
| `yarn.scheduler.capacity.<queue-path>.user-settings.<user-name>.weight` | 在计算队列中用户的用户限制资源值时，将使用此浮点值。 此值将使每个用户的权重大于或小于队列中的其他用户。 例如，如果用户A在队列中接收的资源比用户B和C多50％，则用户A的此属性将设置为1.5。用户B和C将默认为1.0。 |

- Running and Pending Application Limits运行和待定应用程序限制

CapacityScheduler支持以下参数来控制正在运行和挂起的应用程序：

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.maximum-applications` / `yarn.scheduler.capacity.<queue-path>.maximum-applications` | 系统中可以同时处于运行和挂起状态的最大应用程序数。 每个队列的限制与其队列容量和用户限制成正比。 这是一个硬限制，当达到此限制时提交的任何应用程序将被拒绝。 默认值为10000.可以为所有队列设置`yarn.scheduler.capacity.maximum-applications` 并且还可以通过设置在每个队列的基础上覆盖 `yarn.scheduler.capacity.<queue-path>.maximum-applications`. 预期的整数值。 |
| `yarn.scheduler.capacity.maximum-am-resource-percent` / `yarn.scheduler.capacity.<queue-path>.maximum-am-resource-percent` | 群集中可用于运行应用程序主机的最大资源百分比 - 控制并发活动应用程序的数量。 每个队列的限制与其队列容量和用户限制成正比。 指定为浮点数 - 即0.5 = 50％。 默认值为10％。 可以为所有队列设置`yarn.scheduler.capacity.maximum-am-resource-percent` 并且还可以通过设置在每个队列的基础上覆盖 `yarn.scheduler.capacity.<queue-path>.maximum-am-resource-percent` |

- Queue Administration & Permissions 队列管理和权限

CapacityScheduler支持以下参数来管理队列：

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.<queue-path>.state`                 | 队列的状态。 可以是RUNNING或STOPPED之一。 如果队列处于STOPPED状态，则无法将新应用程序提交给自身或其任何子队列。 因此，如果根队列是STOPPED，则不能将任何应用程序提交给整个群集。 现有应用程序继续完成，因此可以优雅地排空队列。 值指定为枚举。 |
| `yarn.scheduler.capacity.root.<queue-path>.acl_submit_applications` | The *ACL* which controls who can *submit* applications to the given queue. If the given user/group has necessary ACLs on the given queue or *one of the parent queues in the hierarchy* they can submit applications. *ACLs* for this property *are* inherited from the parent queue if not specified. |
| `yarn.scheduler.capacity.root.<queue-path>.acl_administer_queue` | The *ACL* which controls who can *administer* applications on the given queue. If the given user/group has necessary ACLs on the given queue or *one of the parent queues in the hierarchy* they can administer applications. *ACLs* for this property *are* inherited from the parent queue if not specified. |

**Note:** An *ACL* is of the form *user1*,*user2* *space* *group1*,*group2*. The special value of * implies *anyone*. The special value of *space* implies *no one*. The default is * for the root queue if not specified.

- Queue Mapping based on User or Group

The `CapacityScheduler` supports the following parameters to configure the queue mapping based on user or group:

| Property                                                 | Description                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.queue-mappings`                 | This configuration specifies the mapping of user or group to a specific queue. You can map a single user or a list of users to queues. Syntax: `[u or g]:[name]:[queue_name][,next_mapping]*`. Here, *u or g* indicates whether the mapping is for a user or group. The value is *u* for user and *g* for group. *name*indicates the user name or group name. To specify the user who has submitted the application, %user can be used. *queue_name* indicates the queue name for which the application has to be mapped. To specify queue name same as user name, *%user* can be used. To specify queue name same as the name of the primary group for which the user belongs to, *%primary_group* can be used. |
| `yarn.scheduler.capacity.queue-mappings-override.enable` | This function is used to specify whether the user specified queues can be overridden. This is a Boolean value and the default value is *false*. |

Example:

```
 <property>
   <name>yarn.scheduler.capacity.queue-mappings</name>
   <value>u:user1:queue1,g:group1:queue2,u:%user:%user,u:user2:%primary_group</value>
   <description>
     Here, <user1> is mapped to <queue1>, <group1> is mapped to <queue2>, 
     maps users to queues with the same name as user, <user2> is mapped 
     to queue name same as <primary group> respectively. The mappings will be 
     evaluated from left to right, and the first valid mapping will be used.
   </description>
 </property>
```

- Queue lifetime for applications

  The `CapacityScheduler` supports the following parameters to lifetime of an application:

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.<queue-path>.maximum-application-lifetime` | Maximum lifetime of an application which is submitted to a queue in seconds. Any value less than or equal to zero will be considered as disabled. This will be a hard time limit for all applications in this queue. If positive value is configured then any application submitted to this queue will be killed after exceeds the configured lifetime. User can also specify lifetime per application basis in application submission context. But user lifetime will be overridden if it exceeds queue maximum lifetime. It is point-in-time configuration. Note : Configuring too low value will result in killing application sooner. This feature is applicable only for leaf queue. |
| `yarn.scheduler.capacity.root.<queue-path>.default-application-lifetime` | Default lifetime of an application which is submitted to a queue in seconds. Any value less than or equal to zero will be considered as disabled. If the user has not submitted application with lifetime value then this value will be taken. It is point-in-time configuration. Note : Default lifetime can’t exceed maximum lifetime. This feature is applicable only for leaf queue. |

### Setup for application priority.

Application priority works only along with FIFO ordering policy. Default ordering policy is FIFO.

Default priority for an application can be at cluster level and queue level.

- Cluster-level priority : Any application submitted with a priority greater than the cluster-max priority will have its priority reset to the cluster-max priority. $HADOOP_HOME/etc/hadoop/yarn-site.xml is the configuration file for cluster-max priority.

| Property                                | Description                                        |
| --------------------------------------- | -------------------------------------------------- |
| `yarn.cluster.max-application-priority` | Defines maximum application priority in a cluster. |

- Leaf Queue-level priority : Each leaf queue provides default priority by the administrator. The queue’s default priority will be used for any application submitted without a specified priority. $HADOOP_HOME/etc/hadoop/capacity-scheduler.xml is the configuration file for queue-level priority.

| Property                                                     | Description                                           |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| `yarn.scheduler.capacity.root.<leaf-queue-path>.default-application-priority` | Defines default application priority in a leaf queue. |

**Note:** Priority of an application will not be changed when application is moved to different queue.

### Capacity Scheduler container preemption

The `CapacityScheduler` supports preemption of container from the queues whose resource usage is more than their guaranteed capacity. The following configuration parameters need to be enabled in yarn-site.xml for supporting preemption of application containers.

| Property                                          | Description                                                  |
| ------------------------------------------------- | ------------------------------------------------------------ |
| `yarn.resourcemanager.scheduler.monitor.enable`   | Enable a set of periodic monitors (specified in yarn.resourcemanager.scheduler.monitor.policies) that affect the scheduler. Default value is false. |
| `yarn.resourcemanager.scheduler.monitor.policies` | The list of SchedulingEditPolicy classes that interact with the scheduler. Configured policies need to be compatible with the scheduler. Default value is `org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.ProportionalCapacityPreemptionPolicy`which is compatible with `CapacityScheduler` |

The following configuration parameters can be configured in yarn-site.xml to control the preemption of containers when `ProportionalCapacityPreemptionPolicy` class is configured for `yarn.resourcemanager.scheduler.monitor.policies`

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.resourcemanager.monitor.capacity.preemption.observe_only` | If true, run the policy but do not affect the cluster with preemption and kill events. Default value is false |
| `yarn.resourcemanager.monitor.capacity.preemption.monitoring_interval` | Time in milliseconds between invocations of this ProportionalCapacityPreemptionPolicy policy. Default value is 3000 |
| `yarn.resourcemanager.monitor.capacity.preemption.max_wait_before_kill` | Time in milliseconds between requesting a preemption from an application and killing the container. Default value is 15000 |
| `yarn.resourcemanager.monitor.capacity.preemption.total_preemption_per_round` | Maximum percentage of resources preempted in a single round. By controlling this value one can throttle the pace at which containers are reclaimed from the cluster. After computing the total desired preemption, the policy scales it back within this limit. Default value is `0.1` |
| `yarn.resourcemanager.monitor.capacity.preemption.max_ignored_over_capacity` | Maximum amount of resources above the target capacity ignored for preemption. This defines a deadzone around the target capacity that helps prevent thrashing and oscillations around the computed target balance. High values would slow the time to capacity and (absent natural.completions) it might prevent convergence to guaranteed capacity. Default value is `0.1` |
| `yarn.resourcemanager.monitor.capacity.preemption.natural_termination_factor` | Given a computed preemption target, account for containers naturally expiring and preempt only this percentage of the delta. This determines the rate of geometric convergence into the deadzone (`MAX_IGNORED_OVER_CAPACITY`). For example, a termination factor of 0.5 will reclaim almost 95% of resources within 5 * #`WAIT_TIME_BEFORE_KILL`, even absent natural termination. Default value is `0.2` |

The `CapacityScheduler` supports the following configurations in capacity-scheduler.xml to control the preemption of application containers submitted to a queue.

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.<queue-path>.disable_preemption`    | This configuration can be set to `true` to selectively disable preemption of application containers submitted to a given queue. This property applies only when system wide preemption is enabled by configuring `yarn.resourcemanager.scheduler.monitor.enable` to *true* and `yarn.resourcemanager.scheduler.monitor.policies` to *ProportionalCapacityPreemptionPolicy*. If this property is not set for a queue, then the property value is inherited from the queue’s parent. Default value is false. |
| `yarn.scheduler.capacity.<queue-path>.intra-queue-preemption.disable_preemption` | This configuration can be set to *true* to selectively disable intra-queue preemption of application containers submitted to a given queue. This property applies only when system wide preemption is enabled by configuring `yarn.resourcemanager.scheduler.monitor.enable` to *true*, `yarn.resourcemanager.scheduler.monitor.policies` to *ProportionalCapacityPreemptionPolicy*, and `yarn.resourcemanager.monitor.capacity.preemption.intra-queue-preemption.enabled` to *true*. If this property is not set for a queue, then the property value is inherited from the queue’s parent. Default value is *false*. |

### Reservation Properties

- Reservation Administration & Permissions

The `CapacityScheduler` supports the following parameters to control the creation, deletion, update, and listing of reservations. Note that any user can update, delete, or list their own reservations. If reservation ACLs are enabled but not defined, everyone will have access. In the examples below, <queue> is the queue name. For example, to set the reservation ACL to administer reservations on the default queue, use the property `yarn.scheduler.capacity.root.default.acl_administer_reservations`

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.root.<queue>.acl_administer_reservations` | The ACL which controls who can *administer* reservations to the given queue. If the given user/group has necessary ACLs on the given queue or they can submit, delete, update and list all reservations. ACLs for this property *are not* inherited from the parent queue if not specified. |
| `yarn.scheduler.capacity.root.<queue>.acl_list_reservations` | The ACL which controls who can *list* reservations to the given queue. If the given user/group has necessary ACLs on the given queue they can list all applications. ACLs for this property *are not* inherited from the parent queue if not specified. |
| `yarn.scheduler.capacity.root.<queue>.acl_submit_reservations` | The ACL which controls who can *submit* reservations to the given queue. If the given user/group has necessary ACLs on the given queue they can submit reservations. ACLs for this property *are not* inherited from the parent queue if not specified. |

### Configuring `ReservationSystem` with `CapacityScheduler`

The `CapacityScheduler` supports the **ReservationSystem** which allows users to reserve resources ahead of time. The application can request the reserved resources at runtime by specifying the `reservationId` during submission. The following configuration parameters can be configured in yarn-site.xml for `ReservationSystem`.

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.resourcemanager.reservation-system.enable`             | *Mandatory* parameter: to enable the `ReservationSystem` in the **ResourceManager**. Boolean value expected. The default value is *false*, i.e. `ReservationSystem` is not enabled by default. |
| `yarn.resourcemanager.reservation-system.class`              | *Optional* parameter: the class name of the `ReservationSystem`. The default value is picked based on the configured Scheduler, i.e. if `CapacityScheduler` is configured, then it is `CapacityReservationSystem`. |
| `yarn.resourcemanager.reservation-system.plan.follower`      | *Optional* parameter: the class name of the `PlanFollower` that runs on a timer, and synchronizes the `CapacityScheduler` with the `Plan` and viceversa. The default value is picked based on the configured Scheduler, i.e. if `CapacityScheduler` is configured, then it is `CapacitySchedulerPlanFollower`. |
| `yarn.resourcemanager.reservation-system.planfollower.time-step` | *Optional* parameter: the frequency in milliseconds of the `PlanFollower` timer. Long value expected. The default value is *1000*. |

The `ReservationSystem` is integrated with the `CapacityScheduler` queue hierachy and can be configured for any **LeafQueue** currently. The `CapacityScheduler` supports the following parameters to tune the `ReservationSystem`:

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.<queue-path>.reservable`            | *Mandatory* parameter: indicates to the `ReservationSystem` that the queue’s resources is available for users to reserve. Boolean value expected. The default value is *false*, i.e. reservations are not enabled in *LeafQueues* by default. |
| `yarn.scheduler.capacity.<queue-path>.reservation-agent`     | *Optional* parameter: the class name that will be used to determine the implementation of the `ReservationAgent` which will attempt to place the user’s reservation request in the `Plan`. The default value is *org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.AlignedPlannerWithGreedy*. |
| `yarn.scheduler.capacity.<queue-path>.reservation-move-on-expiry` | *Optional* parameter to specify to the `ReservationSystem` whether the applications should be moved or killed to the parent reservable queue (configured above) when the associated reservation expires. Boolean value expected. The default value is *true* indicating that the application will be moved to the reservable queue. |
| `yarn.scheduler.capacity.<queue-path>.show-reservations-as-queues` | *Optional* parameter to show or hide the reservation queues in the Scheduler UI. Boolean value expected. The default value is *false*, i.e. reservation queues will be hidden. |
| `yarn.scheduler.capacity.<queue-path>.reservation-policy`    | *Optional* parameter: the class name that will be used to determine the implementation of the `SharingPolicy` which will validate if the new reservation doesn’t violate any invariants.. The default value is *org.apache.hadoop.yarn.server.resourcemanager.reservation.CapacityOverTimePolicy*. |
| `yarn.scheduler.capacity.<queue-path>.reservation-window`    | *Optional* parameter representing the time in milliseconds for which the `SharingPolicy` will validate if the constraints in the Plan are satisfied. Long value expected. The default value is one day. |
| `yarn.scheduler.capacity.<queue-path>.instantaneous-max-capacity` | *Optional* parameter: maximum capacity at any time in percentage (%) as a float that the `SharingPolicy` allows a single user to reserve. The default value is 1, i.e. 100%. |
| `yarn.scheduler.capacity.<queue-path>.average-capacity`      | *Optional* parameter: the average allowed capacity which will aggregated over the *ReservationWindow* in percentage (%) as a float that the `SharingPolicy` allows a single user to reserve. The default value is 1, i.e. 100%. |
| `yarn.scheduler.capacity.<queue-path>.reservation-planner`   | *Optional* parameter: the class name that will be used to determine the implementation of the *Planner* which will be invoked if the `Plan` capacity fall below (due to scheduled maintenance or node failuers) the user reserved resources. The default value is *org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.SimpleCapacityReplanner* which scans the `Plan` and greedily removes reservations in reversed order of acceptance (LIFO) till the reserved resources are within the `Plan` capacity |
| `yarn.scheduler.capacity.<queue-path>.reservation-enforcement-window` | *Optional* parameter representing the time in milliseconds for which the `Planner` will validate if the constraints in the Plan are satisfied. Long value expected. The default value is one hour. |

### Other Properties

- Resource Calculator

| Property                                      | Description                                                  |
| --------------------------------------------- | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.resource-calculator` | ResourceCalculator实现，用于比较调度程序中的资源。 默认情况下，即org.apache.hadoop.yarn.util.resource.DefaultResourceCalculator仅使用Memory，而DominantResourceCalculator使用Dominant-resource来比较多维资源，如内存，CPU等。需要Java ResourceCalculator类名。 |

- Data Locality

| Property                                      | Description                                                  |
| --------------------------------------------- | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.node-locality-delay` | 丢失的调度机会数，之后CapacityScheduler尝试调度机架本地容器。 通常，应将其设置为群集中的节点数。 默认情况下，设置一个机架中的大约节点数为40.预期为正整数值。 |

- Container Allocation per NodeManager Heartbeat

The `CapacityScheduler` supports the following parameters to control how many containers can be allocated in each NodeManager heartbeat.

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `yarn.scheduler.capacity.per-node-heartbeat.multiple-assignments-enabled` | Whether to allow multiple container assignments in one NodeManager heartbeat. Defaults to true. |
| `yarn.scheduler.capacity.per-node-heartbeat.maximum-container-assignments` | If `multiple-assignments-enabled` is true, the maximum amount of containers that can be assigned in one NodeManager heartbeat. Defaults to -1, which sets no limit. |
| `yarn.scheduler.capacity.per-node-heartbeat.maximum-offswitch-assignments` | If `multiple-assignments-enabled` is true, the maximum amount of off-switch containers that can be assigned in one NodeManager heartbeat. Defaults to 1, which represents only one off-switch allocation allowed in one heartbeat. |

### Reviewing the configuration of the CapacityScheduler

Once the installation and configuration is completed, you can review it after starting the YARN cluster from the web-ui.

- Start the YARN cluster in the normal manner.
- Open the `ResourceManager` web UI.
- The */scheduler* web-page should show the resource usages of individual queues.