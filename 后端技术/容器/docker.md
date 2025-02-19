# Docker
- [官网文档](https://docs.docker.com/get-started/overview/)
- [关于 docker 的隔离级别](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504)
- [Docker 命令大全](https://docs.docker.com/engine/reference/run/)

## 1 什么是 docker
docker 创建了一个独立，干净的系统环境，能够让应用程序在不同的机器、系统等环境中正常运行，而不用操心外部环境和依赖等问题导致程序不可用。

可以把 docker 看作一个为目标应用程序创建的干净的小型操作系统。

## 2. Docker 名词解释
docker 架构相关的概念
- **docker daemon (dockerd)**
    - 运行在后台的 docker 进程 ，通过监听 restful 接口管理 docker 对象
- **dockerd object** 主要包括 images，containers，networks，volumes 等；
    - dockerd 也可以和其他 dockerd 通信
- **docker client**
    - 和用户交互，把命令发送到 dockerd；
- **docker registries**
    - 可以理解为仓库，存放 docker images 的地方。
    - 比如 Docker Hub 就是公共仓库，存放许多公用的镜像。
    - 可以通过 docker pull / run / push 来拉取、运行、推送镜像

docker 常用的一些概念

- **docker images** 镜像
    - 镜像是只读的指令模板，用于创建容器。
    - 一般来说，一个镜像是基于另一个镜像创建的，比如基于 ubuntu 镜像构建自己的应用。
    - docker 用 Dockerfile 来描述镜像，构建结束需要推送到 docker registries 里。
- **docker containers** 容器
    - 容器是镜像的一个运行实例，可以 create/start/stop/move/delete 一个容器。
    - 当容器被删除后，容器里面所有的内容和数据都会消失。
- **docker volumns 卷**（物体的三维空间）
    - container 每次从 images 中创建时，都会清空状态；
    - volumns 提供了保留镜像状态的机制。


## 3. 安装 docker
参考：
- http://wiki.baidu.com/pages/viewpage.action?pageId=418343555
- http://docker.baidu.com/guide

```
# 1. 给 work 账户添加权限（否则只有 root 用户能用 docker 命令）
groupadd docker    # 添加用户组
gpasswd -a work docker    # 把 work 添加到用户组里

# 2. 登录，需要先去改密码
docker login -u zhangxiaobin04 -p Dqxxxxx iregistry.baidu-int.com

# 3. 重新登录后，work 账户也能用 docker 了
docker version
docker info

# 4. 启动后台 daemon 进程，这里的网址请用 iregistry.baidu-int.com
/usr/bin/dockerd -bip=10.0.4.1/24 -H unix:///var/run/docker.sock --insecure-registry iregistry.baidu-int.com
```

修改配置文件
```
# vim /etc/docker/daemon.json

{
  "graph" : "/home/disk0/work/docker/",
  "insecure-registries": [
        "iregistry.baidu-int.com"
    ]
}
```

## 4. 常用命令
**通用**
- `docker login`
- `docker version` 查看版本
- `docker info` 查看相关信息

**镜像**
- `docker pull` 从仓库中心拉取镜像到本地
- `docker push` 从本地推送镜像到仓库中心
- `docker build [OPTIONS] PATH | URL | -` 构建镜像
    - `PATH` 指的是要构建的镜像的 Dockerfile 文件所在的路径
    - `-t, --tag list`，镜像名和标签，如 name:tag 
- `docker images` 查看所有的镜像

**容器**
- `docker ps` 查看所有的容器
- `docker port` 查看容器的公开端口
- `docker container` 容器相关操作
- `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`
    - `-d / --detach` 用分离模式运行，即在后台运行；
    - `-p / --publish list` 把容器的端口发布到宿主机上；如 -p 8080:4001，其中 8080 是 docker 内部端口；
- `docker rm/stop [OPTIONS] CONTAINER [CONTAINER...]` 删除/停止一个容器
- `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]`
    - 在某个容器里执行命令；如 `docker exec -it container_name bash`
    - `-i, --interactive` 交互式的模式，会一直接受用户的输入
    - `-t, --tty` 分配一个伪终端
- `docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH`
    - 在容器和本地之间传输文件

**清理磁盘**
- `docker system df` 查看磁盘运行情况
- `docker system prune -a` 清理磁盘

## 5. Dockerfile
参考官方文档：
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- https://docs.docker.com/engine/reference/builder/

参数：
- `FROM <基础镜像>`
    从一个基础镜像中构建，比如：FROM: ubuntu:18.04
- `ENV <环境变量>`
- `COPY [--chown=<user>:<group>] ["<源路径1>",...  "<目标路径>"]`
    - 从 docker 客户端所在的目录，拷贝文件到目标路径，如：COPY . /app
    - 在 multistage 阶段，COPY 能把上个阶段的产物拷贝到另一个镜像中
- `ADD [--chown=<user>:<group>] <src>... <dest>`
    - 类似 COPY，拷贝文件用，支持正则表达式
    - 此外，ADD 能解压缩文件到镜像中，能拷贝 URL 文件到镜像中；
    - 个人建议用 COPY 更清晰一些。
- `RUN <命令行命令>`
    - 构建命令，如： RUN make /app，在构建镜像时使用
- `USER <用户名>[:<用户组>]`
- `WORKDIR`
- `CMD ["<可执行文件或命令>","<param1>","<param2>",...]`
    - 类似于 RUN，但是 RUN 在 docker build （构建镜像）时运行，CMD 在 docker run （构建容器）时运行
- `ENTRYPOINT ["<可执行文件或命令>","<param1>","<param2>",...]`
    - 定义为镜像的主命令，一般是入口脚本

## 6. 安装 nvidia-container-toolkit

如果需要在 docker 中调用 GPU 资源，需要安装 NVIDIA Container Toolkit（nvidia-docker2）。

参考官网：[Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

注意不要安装 nvidia-docker 或者 nvidia-docker2，这些是老版本，已经不支持了。

测试下是否安装成功：

```bash
# 指定所有的卡
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi

# 指定两张卡
docker run --rm --runtime=nvidia --gpus 2 ubuntu nvidia-smi

# 指定第0,2两张卡
docker run --rm --runtime=nvidia --gpus '"device=0,2"' ubuntu nvidia-smi
```

这里的 `--runtime=nvidia` 可以省略
