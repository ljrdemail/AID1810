def myzip(iterable1, iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    while True:
        try:
            v1 = next(it1) #À≠œ»µΩÀ≠¥•∑¢stopiteration
            v2 = next(it2)
        except StopIteration:
            return
        yield (v1, v2)


d = dict(myzip("ABC", "123"))
print(d)
