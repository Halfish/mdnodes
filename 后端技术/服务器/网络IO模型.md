
几个 I/O 多路复用模型：`select`, `poll`, `epoll`


### 1. Select

相关的结构体定义：
```c
 /* Number of descriptors that can fit in an `fd_set'.  */ 
#define __FD_SETSIZE    1024

 /* The fd_set member is required to be an array of longs.  */ 
typedef long int __fd_mask;

 /* It's easier to assume 8-bit bytes than to get CHAR_BIT.  */
#define __NFDBITS   (8 * (int) sizeof (__fd_mask)) 

 /* fd_set for select and pselect.  */
typedef struct {
    // 相当于 long int __fds_bits[1024 / 64];
    __fd_mask __fds_bits[__FD_SETSIZE / __NFDBITS];
} fd_set;

struct timeval {
    __time_t tv_sec;            /* Seconds */
    __suseconds_t tv_usec;      /* Microseconds */
}
```

`select` 函数定义：
```c
 extern int select (
    int __nfds,                             /* 要监视的文件描述符数量 */
    fd_set *__restrict __readfds,           /* 要监视的可读类型文件描述符  */
    fd_set *__restrict __writefds,          /* 要监视的可写类型文件描述符  */
    fd_set *__restrict __exceptfds,         /* 要监视的异常类型文件描述符  */
    struct timeval *__restrict __timeout    /* 最大等待时长 */
); 
```

示例代码
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/select.h>

int main() {
    fd_set readfds;  // 文件描述符集合
    struct timeval timeout; // 超时时间
    int ret;

    // 清空文件描述符集合
    FD_ZERO(&readfds);
    // 将标准输入添加到集合中
    FD_SET(STDIN_FILENO, &readfds);

    // 设置超时时间为 5 秒
    timeout.tv_sec = 5;
    timeout.tv_usec = 0;

    printf("Waiting for input for 5 seconds...\n");

    // 调用 select 函数
    ret = select(STDIN_FILENO + 1, &readfds, NULL, NULL, &timeout);

    if (ret == -1) {
        perror("select");
        exit(EXIT_FAILURE);
    } else if (ret == 0) {
        printf("No input within 5 seconds.\n");
    } else {
        if (FD_ISSET(STDIN_FILENO, &readfds)) {
            char buffer[1024];
            read(STDIN_FILENO, buffer, sizeof(buffer));
            printf("Input: %s\n", buffer);
        }
    }

    return 0;
}
```

Select 的优点：
- I/O 多路复用，单个线程可以管理多个 I/O 操作，可以高效的处理多个网络连接。

缺点：
- 能监视的文件描述符数量最多为 1024 个；
- 需要遍历每个文件描述符来确定哪些文件是可读的。


### 2. poll

```c
/* Data structure describing a polling request.  */ 
struct pollfd {
    int fd;                 /* File descriptor to poll */
    short int events;       /* Types of events poller cares about. */
    short int revents;      /* Types of events that actually occurred. */
};

/*
 * events 可以去下面任意值的组合：
    - POLLIN：表示有数据可读。
    - POLLOUT：表示有数据可写。
    - POLLERR：表示发生错误。
    - POLLHUP：表示挂起事件（通常是对端关闭连接）
 */
#define POLLIN          0x001           /* There is data to read. */
#define POLLOUT         0x004           /* Writing now will not block. */  
#define POLLERR         0x008           /* Error condition.  */
#define POLLHUP         0x010           /* Hung up.  */

/* Type used for the number of file descriptors. */ 
typedef unsigned long int nfds_t;

extern int poll (
    struct pollfd *__fds,       /* 待监控的文件描述符数组 */
    nfds_t __nfds,              /* __fds 数组的大小 */
    int __timeout,              /* 等待的最大时长 */
)
```

示例代码：
```c
#include <stdio.h>
#include <stdlib.h>
#include <poll.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <string.h>

#define SERVER_PORT 8080
#define MAX_EVENTS 2 // 监视的文件描述符数量

int main() {
    int listen_fd, conn_fd;
    struct sockaddr_in server_addr;

    // 创建监听套接字
    if ((listen_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket error");
        exit(1);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(SERVER_PORT);

    if (bind(listen_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind error");
        exit(1);
    }

    if (listen(listen_fd, 5) < 0) {
        perror("listen error");
        exit(1);
    }

    struct pollfd fds[MAX_EVENTS];

    // 监控标准输入
    fds[0].fd = STDIN_FILENO;  // 标准输入文件描述符
    fds[0].events = POLLIN;    // 监控是否有数据可读

    // 监控监听套接字
    fds[1].fd = listen_fd;     // 监听套接字
    fds[1].events = POLLIN;    // 监控是否有连接可接受

    while (1) {
        int ret = poll(fds, MAX_EVENTS, -1); // 无限期等待事件发生
        if (ret < 0) {
            perror("poll error");
            exit(1);
        }

        // 检查标准输入事件
        if (fds[0].revents & POLLIN) {
            char buffer[1024];
            if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
                printf("Received input: %s", buffer);
            }
        }

        // 检查监听套接字事件
        if (fds[1].revents & POLLIN) {
            conn_fd = accept(listen_fd, (struct sockaddr *)NULL, NULL);
            if (conn_fd > 0) {
                printf("Accepted new connection\n");
                close(conn_fd); // 关闭连接
            }
        }
    }

    close(listen_fd); // 关闭监听套接字
    return 0;
}
```

poll 模型的优点
- 和 select 一样多路复用，同一个线程可以处理多个 I/O 操作。
- 没有 select 中的文件描述符的数量限制。

缺点：
- 仍然需要遍历文件描述符数组，才知道哪些状态可读，如果并发量很大，效率会差一些。


### 3. epoll

相关的数据结构
```c
typedef union epoll_data {
    void *ptr;
    int fd;
    uint32_t u32;
    uint64_t u64;
} epoll_data_t;

struct epoll_event {
    uint32_t events;      /* Epoll events */
    epoll_data_t data;    /* User data variable */
} __EPOLL_PACKED;


// epoll_ctl op type
#define EPOLL_CTL_ADD 1     /* Add a file descriptor to the interface. */
#define EPOLL_CTL_DEL 2     /* Remove a file descriptor from the interface. */
#define EPOLL_CTL_MOD 3     /* Change file descriptor epoll_event structure. */
```

函数声明
```c
// 创建 epoll 实例，返回 epfd.
extern int epoll_create1 (
    int __flags         /*  */
) __THROW;       

// 操作某个文件描述符
extern int epoll_ctl (
    int __epfd,         /* epfd 实例 */
    int __op,           /* 操作类型: 添加/删除/修改，EPOLL_CTL_(ADD/DEL/MOD) */
    int __fd,           /* 目标文件描述符 */
    struct epoll_event *__event     /* 回调事件 */
) __THROW;

// 事件循环，等待事件发生
extern int epoll_wait (
    int __epfd,
    struct epoll_event *__events,   /* 发生的事件，数组的大小为 epoll_wait 的返回值 */
    int __maxevents,                /* 允许最大的事件数 */
    int __timeout                   /* 允许等待的最大事件，-1 表示无限等待 */
);
```

示例代码：
```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/epoll.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <arpa/inet.h>

#define MAX_EVENTS 10
#define SERVER_PORT 8080

// 设置文件描述符为非阻塞模式
int set_nonblocking(int fd) {
    int flags = fcntl(fd, F_GETFL, 0);
    if (flags == -1) {
        perror("fcntl F_GETFL failed");
        return -1;
    }
    if (fcntl(fd, F_SETFL, flags | O_NONBLOCK) == -1) {
        perror("fcntl F_SETFL failed");
        return -1;
    }
    return 0;
}

int main() {
    int listen_fd, conn_fd, epoll_fd;
    struct sockaddr_in server_addr;
    struct epoll_event ev, events[MAX_EVENTS];

    // 创建监听套接字
    if ((listen_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket error");
        exit(EXIT_FAILURE);
    }

    // 设置监听套接字为非阻塞
    if (set_nonblocking(listen_fd) == -1) {
        exit(EXIT_FAILURE);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(SERVER_PORT);

    // 绑定地址
    if (bind(listen_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind error");
        exit(EXIT_FAILURE);
    }

    // 开始监听
    if (listen(listen_fd, 5) < 0) {
        perror("listen error");
        exit(EXIT_FAILURE);
    }

    // 创建 epoll 实例
    if ((epoll_fd = epoll_create1(0)) == -1) {
        perror("epoll_create1 error");
        exit(EXIT_FAILURE);
    }

    // 将监听套接字添加到 epoll 实例中
    ev.events = EPOLLIN;  // 监听可读事件
    ev.data.fd = listen_fd;
    if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, listen_fd, &ev) == -1) {
        perror("epoll_ctl: listen_fd");
        exit(EXIT_FAILURE);
    }

    // 事件循环
    while (1) {
        int nfds = epoll_wait(epoll_fd, events, MAX_EVENTS, -1);  // 无限期等待事件发生
        if (nfds == -1) {
            perror("epoll_wait error");
            exit(EXIT_FAILURE);
        }

        for (int i = 0; i < nfds; ++i) {
            if (events[i].data.fd == listen_fd) {
                // 有新的连接到来
                conn_fd = accept(listen_fd, NULL, NULL);
                if (conn_fd == -1) {
                    perror("accept error");
                    continue;
                }

                // 设置新连接为非阻塞
                if (set_nonblocking(conn_fd) == -1) {
                    close(conn_fd);
                    continue;
                }

                // 将新的连接加入 epoll 实例中监听
                ev.events = EPOLLIN | EPOLLET;  // 监听可读事件，使用边缘触发模式
                ev.data.fd = conn_fd;
                if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, conn_fd, &ev) == -1) {
                    perror("epoll_ctl: conn_fd");
                    close(conn_fd);
                }
            } else {
                // 处理已有连接上的事件
                char buffer[1024];
                ssize_t count;
                if ((count = read(events[i].data.fd, buffer, sizeof(buffer))) == -1) {
                    if (errno != EAGAIN) {
                        perror("read error");
                        close(events[i].data.fd);
                    }
                } else if (count == 0) {
                    // 对端关闭连接
                    close(events[i].data.fd);
                } else {
                    // 处理数据（这里简单打印到控制台）
                    printf("Received: %.*s\n", (int)count, buffer);
                }
            }
        }
    }

    close(listen_fd);
    close(epoll_fd);
    return 0;
}
```

epoll 的两种模式
- 水平触发（LT，Level-Triggered）（类比水位警报器），默认模式，只要有未处理的事件，epoll_wait就会一直返回，直到事件被处理。
- 边缘触发（ET，Edge-Triggered）（类比门铃），当监控的文件描述符状态变为就绪时，通知一次，后续不再通知。适合高性能，谨慎使用。

epoll 的优点：
- 高效，不需要像 select 和 poll 一样需要遍历所有的文件描述符。
    - epoll 内部有个红黑树，用来存储所有的文件描述符。而 poll 用的是数组，大了会影响性能。
    - epoll 内部有个链表，只返回状态变化的文件描述符，避免了无意义的轮询。
- 灵活的触发模式，支持边缘触发模式和水平触发模式。

epoll 的缺点
- 用起来比 select / poll 复杂些，特别是边缘触发模式，容易丢失事件。
- 低并发不一定比 select/ poll 高效，因为初始化和维护数据结构有些开销。
- Linux专用，不支持其他的平台，epoll 也不是 POSIX 标准的一部分。
