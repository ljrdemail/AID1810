# -*- coding:utf-8 -*-
import bson
from pymongo import MongoClient

from_img = "登录逻辑.png"
to_img = "登录逻辑_new.png"

conn = MongoClient("127.0.0.1", 27017)
db = conn.gridfs  # 获取库对象
myset = db.image  # 获取集合对象 不用默认的 fs.chunks


def save_img(myset):  # 调用存文件
    f = open(from_img, "rb")
    data = f.read()
    content = bson.binary.Binary(data)
    myset.insert({'filename': from_img,
                  'data': content})  # 这里只存一个表 不像默认有file.fs 和file.chunks 这里结合两者 只保存filename 和 二进制话之后的 内容 不像原始分开两个表
    print("Save Done!")
    return

# use gridfs
# show tables
# db.image.find().pretty()


def get_img(myset):
    img = myset.find_one({"filename": from_img})
    with open(to_img, "wb") as f:
        f.write(img["data"])
        print("GET Done！")

        return


#save_img(myset)
get_img(myset)
conn.close()

