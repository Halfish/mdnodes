
Celery + RabbitMQ
- Celery 负责异步任务，RabbitMQ 负责中间的消息队列。
- Celery Client 序列化异步任务，发送到 RabbitMQ 中；Celery Server 取出任务并执行；

Celery 分布式
- 不涉及共识算法，虽然是分布式的执行任务，但是不需要保持数据的一致性。
- 如发送邮件，生成报表，不需要保持数据的强一致性；

RabbitMQ 作为一个消息队列
- 采用主从复制来提高分布式的效率；