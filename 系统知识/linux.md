### 录屏
kazam 录屏

系统录屏：Ctrl + Alt + Shift + R

### 常用功能

```bash
# 查询端口占用
sudo lsof -i:<port>

# 查看进程详情
ps -p <pid>
cat /proc/<pid>/cmdline
cat /proc/<pid>/status

# 这里看的更清晰
htop
```

#### 换行符的问题

CR, Carriage Return
- 这个一般写做 `\r`
- 意思是回到本行的开头位置。
- ASCII 中符号序数为 13.

LF, Line Feed
- 一般写做 `\n`，换行,
- 意思是把光标移到下一行的同一个位置。
- ASCII 中符号序数为 10.


不同的操作系统中，用不同的换行符。
1. CRLF, \r\n，Windows和DOS默认用这个。
2. LF，\n, Unix / Linux / MacOS 下一般用这个。

VSCode 右下角会显示 CRLF/LF，可以直接改。


