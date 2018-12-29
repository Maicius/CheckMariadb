# CheckMariadb
一个用于检测数据库是否崩掉并重启的脚本(阿里云的轻量级服务器CentOS下的mariadb总是莫名奇妙的崩掉)

- 后台启动脚本并输出日志到指定文件

> nohup python -u check_mariadb.py > check_mariadb.log

- 关闭脚本：

> ps -aux 查看脚本pid
> kill pid
