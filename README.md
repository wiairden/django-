# Django任务平台网页  


## 使用教程:  

### 1. 安装django与python环境  

#### 1.1安装 Python  

访问 https://www.python.org/downloads/ 下载最新版本的 Python 并安装。
在安装过程中，勾选“Add Python x.x to PATH”选项，让 Python 在命令行中全局可用。  

#### 1.2安装 Django  

打开命令行（Windows 中使用 PowerShell 或 cmd，Mac 和 Linux 使用终端）。
使用 pip 工具安装 Django。运行以下命令：  

```pip install django```
#### 1.3安装MYSQL  

下载 MySQL 安装程序：前往 MySQL 官方网站 (https://dev.mysql.com/downloads/mysql/) 下载适用于你的操作系统的 MySQL 安装程序。  
运行安装程序：双击下载的安装程序并按照安装向导的指示进行操作。在安装过程中，你可以选择安装类型、安装位置和其他选项。
#### 1.4 安装pymysql  

```
pip install pymysql
```

#### 1.5创建数据库 
```
CREATE DATABASE root
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;
```
#### 非使用教程部分
查看数据库  

```
show databases;
```

选择数据库  

```
use +id  
```
删除数据库  
```
DROP DATABASE database_name;
```
查看表  
```
show tables;
```
查看表中字段  
```
desc +table_name
```

#### 非使用教程部分结束  

### 2.迁移数据库  
#### 2.1设置数据库：
在 Django 项目的 settings.py 文件中配置 MySQL 数据库信息，需要做以下几个步骤：  

打开 settings.py 文件：在 Django 项目中找到 settings.py 文件    

配置 DATABASES 设置：在 settings.py 文件中找到名为 DATABASES 的设置项，通常位于文件的顶部或底部。根据MySQL 数据库信息，配置 DATABASES 设置如下：  

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',      # 数据库名称
        'USER': 'myuser',          # 用户名
        'PASSWORD': 'mypassword',  # 密码
        'HOST': 'localhost',       # 主机地址，如果是本地数据库可以使用 localhost
        'PORT': '',                # 默认端口号
    }
}
```

本项目的DATABASES为:  
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'root', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
    }
}

```

根据实际 MySQL 数据库信息，修改上述代码中的 'NAME'、'USER'、'PASSWORD' 等键对应的值为数据库名称、用户名和密码，并根据需要修改 'HOST' 和 'PORT' 的值。  

保存文件：保存 settings.py 文件并关闭编辑器。  

#### 2.2运行迁移：
在命令行中执行 ```python manage.py makemigrations``` ```python manage.py makemigrations webapp01``` 和 ```python manage.py migrate``` 命令，创建数据库表结构和进行数据库迁移操作。  

### 3.启动 Django 项目
进入到刚刚创建的项目目录：  

```cd web```

运行以下命令启动开发服务器：  

```python manage.py runserver 8000```

在浏览器中访问 http://127.0.0.1:8000/ ，如果看到 项目页面，则说明项目已成功启动。  
