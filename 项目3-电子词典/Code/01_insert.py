import pymysql

db = pymysql.connect("127.0.0.1", "root", "123456", 'dict', charset="utf8")
curs = db.cursor()
i = 1
with open("dict.txt", 'r') as f:
    while True:
        oneLine = f.readline()
        if not oneLine:
            break;
        word = oneLine.split()[0]
        interpret = ' '.join(oneLine.split()[1:])
        ins = 'insert into words(word,interpret) values(%s,%s)'
        curs.execute(ins, [word, interpret])
        db.commit()
        print("第%d条存入成功" % i)
        i += 1;
