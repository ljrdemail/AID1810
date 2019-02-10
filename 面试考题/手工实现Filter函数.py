def myfilter(fn, iterable):


    for i in iterable:
        if (fn(i) == True):

            yield i



for x in myfilter(lambda y: y % 2 == 1, range(10)):
    #print(myfilter(lambda y: y % 2 == 1, range(10)))
    print(x)
