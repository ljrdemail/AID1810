# -*- coding:utf-8 -*-

def copy(source, dest):
    try:
        fr = open(source, "rb")
        fw = open(dest, "wb")
        while True:
            b = fr.read(4096)
            fw.write(b)
            fw.flush()
            if not b:
                print("复制完成")
                break;

    except OSError as err:
        print("拷贝过程中出错")
    except FileNotFoundError as err:
        print("文件不存在")
    finally:
        fw.close()
        fr.close()

copy("apache-tomcat-9.0.12-windows-x64.zip", "apache-tomcat-9.0.12-windows-x642.zip")
