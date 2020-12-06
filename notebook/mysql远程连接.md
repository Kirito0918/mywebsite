进入mysql
```
mysql -u root -p
```

使用mysql数据库
```
use mysql;
```

将user表root的Host字段改为%
```
update user set Host='%' where User='root';
```

更新权限
```
flush privileges;
```

更改配置文件,将/etc/mysql/mysql.conf.d/mysqld.cnf中bind-address这一行注释掉
```
# bind-address		= 127.0.0.1
```

重启mysql
```
sudo /etc/init.d/mysql restart
```

远程连接
```
mysql -h host -P 3306 -u root -p
```
