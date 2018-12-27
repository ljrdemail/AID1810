from multiprocessing import Lock
from multiprocessing import Process
from multiprocessing import Value


def floatdemo(data):
    print(data.value)


def chardemo(data):
    print(data.value)


if __name__ == "__main__":
    sharedata = Value("c", b'h')
    sharedata2 = Value("f", 5.5)
    lock = Lock()

    p = Process(target=chardemo, args=(sharedata,))
    p2 = Process(target=floatdemo, args=(sharedata2,))
    p.start()
    p2.start()
    p.join()
    p2.join()
