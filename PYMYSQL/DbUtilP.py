# -*- coding:utf-8 -*-
class DbUtil:
    def __init__(self, host, user, password, database, charset, port):
        import pymysql

        self.conn = pymysql.connect(host, user, password, database, charset=charset, port=port)
        self.cur = self.conn.cursor()

    def DML(self, sql, L=[]):
        try:
            self.cur.execute(sql, L)
            self.conn.commit()
            print("数据操作成功！")
        except Exception as e:
            self.conn.rollback()
            print("数据操作错误，原因是:", e)

    def DQL(self, sql, L=[]):
        self.cur.execute(sql, L)
        return self.cur.fetchall()

    def __del__(self):

        self.cur.close()
        self.conn.close()

#
# if __name__ == '__main__':
#     du = DbUtil("176.136.16.13", "tiger", "123", "db5", "utf8", 3306)
#     lineall = du.DQL("select * from t1")
#     for x in lineall:
#       print("姓名:", x[1], end=",")
#       print("分数:", x[2])
#
#     name = input("请输入要查询的姓名：")
#     lineone = du.DQL("select * from t1 where name=%s", [name])
#     for x in lineone:
#       print("姓名:", x[1], end=",")
#       print("分数:", x[2])
#
#     du.DML("insert into t1 values(6,'李清照',88)")
#     du.DML("insert into t1 values(%s,%s,%s)", [9, '张三', 99])
#     du.DML("update t1 set name='苏轼' where name=%s", ['欧阳修'])
