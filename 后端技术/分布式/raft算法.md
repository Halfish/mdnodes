# RAFT 算法

raft 算法是经典的分布式一致性算法。相比较于 paxos 算法，raft算法更容易理解和实现。


raft 把分布式有一致性问题分成了三个子问题：
1. Leader选举
2. 日志同步
3. 安全性保证


## Leader选举

每个机器或者节点都属于三种决策中的一个：`Leader`，`Candidate`，`Follower`，整个集群里同一时刻最多只能有一个 `Leader`，如果没有，则需要根据多数票原则选举出一个新的。

选举的步骤
1. 结点定时器超时，没有收到 Leader 的消息，结点转为 Candidate；
2. Candidate 向其他结点发送请求投票的请求（RequestVote）
3. 其他节点投票（根据 Term，即任期值来判断）
4. 超过半票时，Candidate 成为新的 Leader


## 日志同步

## 安全性保障

Raft 算法引入了两条规则来去报
1. 已经 commit 的消息，一定会存在于后续的 Leader节点，不会被删除
2. 未 commit 的消息可能会丢失

