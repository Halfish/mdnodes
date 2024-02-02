

[Docker 命令大全](https://docs.docker.com/engine/reference/run/)




```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

# 进入某个容器
#   --interactive , -i
#   --tty , -t	
docker exec -it CONTAINER /bin/bash
```

```bash
# 从容器里下载文件
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-

# 上传文件到容器里
docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
```

docker 清除缓存
```
docker system prune -a
```