# flask-restful后端APIDemo
---
一个带数据库迁移的用蓝图组织的flask-restful大型项目架构的demo

### 项目目录
- app #蓝图模板
  - device
    
    - __init__.py #控制该模块导出的内容 
    
    - view.py #restful class和视图函数放置的地方
  - __init__.py #初始化flask应用对象，插件等的地方
  - models.py orm对象
  - utils.py 全局公共工具函数，封装了一个dto(data transfer object)
- migrations #数据库迁移目录
- .env flask #环境变量
- config.py #不同环境配置的类
- manage.py #用命令行启动项目的入口文件
- requirement.txt #需要安装的包
### 初始化
  1. 创建虚拟环境和切换到虚拟环境
  ```bash
  python -m venv venv
  cd venv/Scripts
  activate
  ```
  2. 安装依赖
  ```bash
  pip install -r requirement.txt
  ```
### 运行
根目录下运行 `python manage.py runserver`

### 数据库

- 连接配置: `config.py`内
- 初始化数据库： 根目录下运行 `python manage.py db init`
- 迁移： 根目录下运行 `python manage.py db migrate -m '描述'`
- 更新： 根目录下运行 `python manage.py db upgrade`

**Note：**
1. 每次在运行完`migrate -m`命令后，在`/migrations/versions`下的对应文件中可以看到
2. alembic自动生成的修改检测，需要自己手动检查下，类似字段长度和类型的修改可能检测不到
3. [alembic 能自动生成的类型和配置方法](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)








