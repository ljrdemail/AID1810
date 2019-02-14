# 启动和管理项目的操作代码
# 导入app 中的create_app 用于启动
from app import *
# 通过manager()管理项目 并增加数据迁移指令
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# 导入所有的实体类方便使用db指令做迁移
from app import create_app, db

# 调用create _app得到app


app = create_app()
# 创建Manager 实例用于托管app
manager = Manager(app)
# 创建Migrate对象用于关联要管理的app和db
migrate = Migrate(app, db)
# 再通过Manager对象增加db 迁移指令
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    # app.run()
    # 通过manager 实例来启动程序
    manager.run()

# 在Terminal中在项目目录下执行以下命令
# 1 python manage.py db init
# 2 python manage.py db migrate
# 3 python manage.py db upgrade
# 会在项目目录下添加 migrations 子目录并在数据中添加alembic_version表
